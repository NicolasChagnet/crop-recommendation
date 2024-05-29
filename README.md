# Crop Recommendation analysis

#### -- Project Status: [ On-Hold ]

## Project Intro/Objective
his project contains some code meant to analyse the dataset [varshitanalluri/crop-recommendation-dataset](https://www.kaggle.com/datasets/varshitanalluri/crop-recommendation-dataset) classifying which kind of crop is recommended depending on the nature of the soil and other environmental factors. This is a multiclass classification question.

<!--
### Collaborators
|Name     |  Github Page   |  Personal Website  |
|---------|-----------------|--------------------|
|Nicolas Chagnet | [NicolasChagnet](https://github.com/NicolasChagnet)| [nicolaschagnet.github.io](https://nicolaschagnet.github.io)  | -->

### Methods Used
* Data Analysis
* Machine Learning
* Data Visualization
* Predictive Modeling

### Technologies
* Python
* Pandas, Scikit-learn, numpy

## Project Description
This project contains some code meant to analyse the dataset [varshitanalluri/crop-recommendation-dataset](https://www.kaggle.com/datasets/varshitanalluri/crop-recommendation-dataset) classifying which kind of crop is recommended depending on the nature of the soil and other environmental factors. This is a multiclass classification question.

This dataset is very clean, all features are numerical and there are no missing values. This means that the data wrangling part of the process is simplified. I have used this dataset as a simple case to study how to properly package and dockerize a complete data science project.

To run this code, first build the docker image, then run it. This will run a comparison of various models (Decision tree, Random forest, Gaussian Bayesian classifiers) on a training dataset using cross-validation and will use the Dummy random classifier as a baseline for comparison. Then one of these (Random Forest) is chosen for its high score, its hyperparameters will be tuned through RandomSearch cross-validation and the model, on optimal hyperparameters, will be further tested on a separated test dataset.

The output of all these steps and of the Exploratory Data Analysis is logged in files, jupyter notebooks and the optimal hyperparameters are stored in a .json file. The produced output from these steps is in the folders `reports` and `models` which should therefore be bound when running the container.


## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](data/raw) within this repo.
3. Data processing/transformation scripts are being kept [here](src/).
4. Exploratory data analysis can be found in a Jupyter notebook [here](notebooks/0_Exploratory_Data_Analysis.ipynb) and in an HTML report [here](reports/profile_eda_raw.html).

To run the main analysis build the container using
```bash
docker build -t IMAGE_NAME .
```
and then run the image while binding the output folders
```bash
docker run -v $PWD/reports:/reports -v $PWD/models:/models --rm IMAGE_NAME
```


<!-- ## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](#)
* [Notebook/Markdown/Slide DeckTitle](#)
* [Blog Post](#) -->
