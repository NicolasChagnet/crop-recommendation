import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate

from src import config, io
from src.models.model_definitions import models_to_compare


def train(
    name,
    model_class,
    features,
    hyperparameters={},
    scoring="roc_auc_ovr_weighted",
    cv=5,
    verbose=True,
):
    """Cross-validates a model for a given set of features and hyperparameters. Outputs a report to file and stdout.

    Args:
        name (str): Name of model
        model_class (sklearn.base.BaseEstimator): Model to use for cross-validation
        features (list(str)): List of features to include
        hyperparameters (dict, optional): Dictionary of hyperparameters to feed to the model. Defaults to {}.
        scoring (str, optional): Scoring method to use for cross-validation. Defaults to "roc_auc_ovr_weighted".
        cv (int, optional): Number of Kfold splits. Defaults to 5.
        verbose (bool, optional): Whether to print the output to stdout. Defaults to True.

    Returns:
        pandas.DataFrame: Scores and fitting time for each iteration of the model cross-validation.
    """
    print(f"Training {name}...")
    df_train = pd.read_csv(config.data_path_train)
    X_train = df_train[features]
    y_train = df_train[config.target]
    # We compute the score of the model on each fold
    cv_results = cross_validate(
        model_class(**hyperparameters),
        X_train,
        y_train,
        cv=cv,
        scoring=scoring,
        return_train_score=True,
    )
    cv_results["name"] = name
    cv_results["metric"] = scoring
    cv_results_df = pd.DataFrame(cv_results)
    io.write_report_comparison(name, cv_results_df, suffix="training", verbose=verbose)
    return cv_results_df


def compare_models():
    """Compare the various models and store the comparison to file."""
    trainings = [
        train(
            name,
            val["model"],
            val["features"],
            hyperparameters=val["hyperparameters"],
            verbose=False,
        )
        for name, val in models_to_compare.items()
    ]
    cv_results_all = pd.concat(trainings)
    io.write_report_comparison("comparison", cv_results_all, suffix="training")
