import json

import numpy as np
import pandas as pd
from sklearn.metrics import get_scorer, roc_auc_score
from sklearn.model_selection import RandomizedSearchCV

from src import config, io
from src.models.model_definitions import hyperparameters_range, models_to_compare


def test(
    name,
    model_class,
    features,
    hyperparameters={},
    scoring="roc_auc_ovr_weighted",
    verbose=True,
):
    """Trains a model on the entire training dataset and scores the model on the test dataset.

    Args:
        name (str): Name of model
        model_class (sklearn.base.BaseEstimator): Model to use for cross-validation
        features (list(str)): List of features to include
        hyperparameters (dict, optional): Dictionary of hyperparameters to feed to the model. Defaults to {}.
        scoring (str, optional): Scoring method to use for cross-validation. Defaults to "roc_auc_ovr_weighted".
        verbose (bool, optional): Whether to print the output to stdout. Defaults to True.

    Returns:
        pandas.DataFrame: Result of training and testing for the model.
    """
    print(f"Testing {name}...")
    # Load data
    df_train = pd.read_csv(config.data_path_train)
    df_val = pd.read_csv(config.data_path_val)
    X_train = df_train[features]
    y_train = df_train[config.target]
    X_val = df_val[features]
    y_val = df_val[config.target]

    # Train the model on the entire training set
    model = model_class(**hyperparameters)
    model.fit(X_train, y_train)
    y_predict_train = model.predict_proba(X_train)
    y_predict_val = model.predict_proba(X_val)

    # Scores
    # metric = get_scorer(scoring)
    # TO FIX: temporarily had to hardcode the metric here
    metric = roc_auc_score
    score_train = metric(
        y_train.to_numpy(), y_predict_train, multi_class="ovr", average="weighted"
    )
    score_val = metric(
        y_val.to_numpy(), y_predict_val, multi_class="ovr", average="weighted"
    )

    # Output preparation
    result = pd.DataFrame(
        {
            "name": name,
            "metric": scoring,
            "train_score": score_train,
            "test_score": score_val,
            "hyperparameters": [hyperparameters],
        }
    )
    io.write_report_comparison(name, result, suffix="testing", verbose=verbose)
    return result


def hyperparameters_tuning(
    name,
    model_class,
    features,
    scoring="roc_auc_ovr_weighted",
    cv=3,
    n_iter=100,
    verbose=True,
):
    """Tuning of hyperparameters for a given using Random combinations

    Args:
        name (str): Name of model
        model_class (sklearn.base.BaseEstimator): Model to use for cross-validation
        features (list(str)): List of features to include
        scoring (str, optional): Scoring method to use for cross-validation. Defaults to "roc_auc_ovr_weighted".
        cv (int, optional): Number of Kfold splits. Defaults to 5.
        n_iter (int, optional): Number of iterations in the random search. Defaults to 100.
        verbose (bool, optional): Whether to print the output to stdout. Defaults to True.

    Returns:
        sklearn.model_selection.RandomizedSearchCV: Result of random search
    """
    print(f"Tuning {name}...")
    # Randomized Grid search of hyperparameters
    model_random = RandomizedSearchCV(
        model_class(),
        param_distributions=hyperparameters_range[name],
        random_state=config.random_state,
        scoring=scoring,
        n_iter=n_iter,
        cv=cv,
        n_jobs=-1,
        verbose=2,
    )
    df_train = pd.read_csv(config.data_path_train)
    X_train = df_train[features]
    y_train = df_train[config.target]
    model_random.fit(X_train, y_train)
    return model_random


def test_model(name):
    model_details = models_to_compare[name]
    file_hyperparameters = config.path_hyperparameters / f"{name}.json"
    if not file_hyperparameters.exists():
        print("Missing hyperparameter file! Tune the model first...")
        return None
    with open(file_hyperparameters, "r") as file:
        hyperparameters = json.load(file)
    result_test = test(
        name, model_details["model"], config.features, hyperparameters=hyperparameters
    )


def tune_model(name):
    model_details = models_to_compare[name]
    # Tune model
    result_random = hyperparameters_tuning(
        name, model_details["model"], config.features
    )
    io.write_hyperparameters(name, result_random.best_params_)
