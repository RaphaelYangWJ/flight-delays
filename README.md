# US Flight Delays Prediction Using Spark Machine Learning

## Project Overview
This project focuses on predicting flight delays in the US using big data and machine learning at scale. It leverages PySpark for data processing and Azure for distributed data processing, incorporating a wide range of data sources from 2015-2018 to train logistic regression, perceptron, and neural network models.

### Key Features
- **Big Data Cleaning and Processing**: Merged and processed vast datasets using PySpark, including flight information, weather, holiday, and natural disaster data.
- **Machine Learning Modeling**: Utilized Spark on Azure for distributed data processing, experimenting with various models to predict flight delays.

## Directory Structure
1. **Phase 1**
   - Contains Exploratory Data Analysis (EDA) and project planning documents.
2. **Phase 2**
   - Includes notebooks for dataset EDA, feature processing, data cleaning, Principal Component Analysis (PCA), and logistic regression modeling.
3. **Phase 3**
   - Houses notebooks for data concatenation, XGBoost, Multilayer Perceptron (MLP), and neural network modeling.

## Implementation Details

### Big Data Cleaning and Processing
- **Techniques**: Employed data concatenation, deduplication, missing value removal, and outlier exclusion.
- **Feature Selection**: Chose 19 effective features from a pool of 200 for modeling.

### Machine Learning Modeling
- **Models**: Experimented with logistic regression, perceptron, and neural network models on Spark.
- **Input Features**: Included departure and arrival airports, taxi-out time, aircraft carriers, and weather conditions.
- **Performance**: Achieved an 83.9% accuracy on the model's validation set.
