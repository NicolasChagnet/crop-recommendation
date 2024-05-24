import pandas as pd
from ydata_profiling import ProfileReport

from src.config import eda_profile_raw
from src.data.load_data import check_existing_data, load_dataset_raw


def make_report_eda_raw():
    """Generates a complete EDA report of the raw dataset"""
    check_existing_data()
    data = load_dataset_raw()
    ProfileReport(df=data, type_schema={"Crop": "categorical"}).to_file(eda_profile_raw)
