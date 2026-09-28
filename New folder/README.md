# AQI Monitoring and Prediction Dashboard

## Project Description

The Air Quality Index Monitoring and Prediction Dashboard
is a Python-based web application that estimates air quality
using machine learning.

Users can enter pollutant values and view the predicted AQI,
air quality category, pollutant chart, and prediction history.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib

## Machine Learning Algorithm

Random Forest Regressor

## Input Features

- PM2.5
- PM10
- NO2
- SO2
- CO
- O3

## Project Structure

AQI_Monitoring_Dashboard/
|
|-- app.py
|-- train_model.py
|-- prediction.py
|-- requirements.txt
|-- README.md
|
|-- data/
|   |-- aqi_data.csv
|
|-- model/
    |-- aqi_model.pkl

## Installation

Install the required libraries:

pip install -r requirements.txt

## Train the Model

python train_model.py

## Run the Dashboard

python -m streamlit run app.py

## Features

1. AQI prediction
2. Pollutant monitoring
3. Interactive charts
4. AQI category display
5. Prediction history
6. CSV download

## Dataset

The included dataset contains synthetic sample readings
for educational demonstration.

The predicted AQI is not an official government measurement.