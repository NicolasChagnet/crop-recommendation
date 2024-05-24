import pandas as pd
from ydata_profiling import ProfileReport

from src import config


def make_report_eda_raw():
    """Generates a complete EDA report of the raw dataset"""
    data = pd.read_csv(config.data_path_raw)
    ProfileReport(df=data, type_schema={"Crop": "categorical"}).to_file(
        config.eda_profile_raw
    )
