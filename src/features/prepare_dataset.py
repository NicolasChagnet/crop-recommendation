import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    LabelEncoder,
    MinMaxScaler,
    RobustScaler,
    StandardScaler,
)

import src.config as config


def split_dataset(df, features, test_size=0.33):
    """Splits a dataset into training and validation datasets.

    Args:
        df (pd.DataFrame): Dataset to split.
        features (list(str)): List of columns to keep as features
        test_size (float, optional): Relative size of the validation dataset. Defaults to 0.33.

    Returns:
        (pd.DataFrame, pd.DataFrame, pd.Series, pd.Series): Training and validation splits.
    """
    # Split the dataset into features,target
    X = df[features]
    y = df[config.target]

    # First we separate the data into training and validation datasets
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=test_size, random_state=config.random_state
    )
    # Apply transformations to features and target
    X_train, X_val = scale_features(X_train, X_val, features)
    y_train, y_val = encode_target(y_train, y_val)
    # Merge back and save to file
    df_train = pd.concat([X_train, y_train], axis=1)
    df_val = pd.concat([X_val, y_val], axis=1)
    # Export training and validation sets
    df_train.to_csv(config.data_path_train, index=False)
    df_val.to_csv(config.data_path_val, index=False)


def encode_target(y_train, y_val):
    """Encodes the n labels of the target to integers between 0 and n-1

    Args:
        y_train (pd.Series): Target of the training set
        y_val (pd.Series): Target of the validation set

    Returns:
        (pd.Series, pd.Series): Encoded targets of training and validation sets
    """
    y_train = y_train.map(config.labels_map)
    y_val = y_val.map(config.labels_map)
    return y_train, y_val


def scale_features(X_train, X_val, features):
    """Generates rescaled features for each numerical columns.

    Args:
        X_train (pd.DataFrame): Training features.
        X_val (pd.DataFrame): Validation features.
        feature (list(str)): List of features to scale.

    Returns:
        (pd.DataFrame, pd.DataFrame): DataFrames with additional rescaled features.
    """
    # Generate a new column for each scaling type
    for col in features:
        sscaler = StandardScaler()
        mmscaler = MinMaxScaler()
        rscaler = RobustScaler()
        for scaler in [sscaler, mmscaler, rscaler]:
            scaler.set_output(transform="pandas")
        X_train[col + "_std"] = sscaler.fit_transform(X_train[[col]])
        X_val[col + "_std"] = sscaler.transform(X_val[[col]])
        X_train[col + "_minmax"] = mmscaler.fit_transform(X_train[[col]])
        X_val[col + "_minmax"] = mmscaler.transform(X_val[[col]])
    return X_train, X_val


def generate_split(path):
    df = pd.read_csv(config.data_path_renamed)
    # Here is where we would usually call feature engineering functions, for now we will simply keep it simple.
    split_dataset(df, config.features)
