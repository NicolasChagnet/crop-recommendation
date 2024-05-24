import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from src import config

# List of models to compare
models_to_compare = {
    "Dummy": {
        "model": DummyClassifier,
        "hyperparameters": {},
        "features": config.features,
    },
    "DecisionTree": {
        "model": DecisionTreeClassifier,
        "hyperparameters": {},
        "features": config.features,
    },
    "RandomForest": {
        "model": RandomForestClassifier,
        "hyperparameters": {},
        "features": config.features,
    },
    "NaiveBayesGaussian": {
        "model": GaussianNB,
        "hyperparameters": {},
        "features": config.features,
    },
}

hyperparameters_range = {
    "RandomForest": {
        "bootstrap": [True, False],
        "max_depth": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
        "max_features": ["auto", "sqrt"],
        "min_samples_leaf": [1, 2, 4],
        "min_samples_split": [2, 5, 10],
        "n_estimators": [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],
    }
}
