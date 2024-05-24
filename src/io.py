import json

from src import config


def write_report_comparison(name, result, suffix="", verbose=True):
    """Write result of training a model to string

    Args:
        name (str): Name of the model trained
        result (pandas.DataFrame): Result of cross-validation
        verbose (bool, optional): Whether to print the output to stdout. Defaults to True.
    """
    with open(config.report_dir / f"{name}_{suffix}_summary.md", "w") as file:
        num_columns = result.select_dtypes("number").columns
        description = (
            result.groupby("name")[num_columns]
            .mean()
            .sort_values(by="test_score", ascending=False)
        )
        if verbose:
            print(result)
            print(description)
        file.write("# Mean results per algorithm\n")
        file.write(description.to_markdown())
        file.write("\n\n")
        file.write("# Iterations\n")
        file.write(result.to_markdown())


def write_hyperparameters(name, hyperparameters):
    """Writes tuned choice of hyperparameters to file

    Args:
        name (str): Name of the model trained
        hyperparameters (dict): Dictionary of optimized hyperparameters
    """
    with open(config.path_hyperparameters / f"{name}.json", "w") as file:
        json.dump(hyperparameters, file)
