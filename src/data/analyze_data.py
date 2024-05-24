import pandas as pd


def is_outlier(series):
    q3 = series.quantile(0.75)
    q1 = series.quantile(0.25)
    iqr = q3 - q1
    return (series < q1 - 1.5 * iqr, series > q3 + 1.5 * iqr)
