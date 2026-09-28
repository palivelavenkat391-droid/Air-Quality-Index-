import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/aqi_model.pkl")

# Input feature names
FEATURES = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]


def predict_aqi(pm25, pm10, no2, so2, co, o3):

    input_data = pd.DataFrame(
        [[pm25, pm10, no2, so2, co, o3]],
        columns=FEATURES
    )

    prediction = model.predict(input_data)[0]

    return max(0, round(float(prediction)))


def get_aqi_category(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderate"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    else:
        return "Severe"


def get_health_message(category):

    messages = {
        "Good": "Air quality is satisfactory.",
        "Satisfactory": "Minor breathing discomfort may occur in sensitive people.",
        "Moderate": "Sensitive individuals should reduce prolonged outdoor exertion.",
        "Poor": "Reduce prolonged outdoor exertion.",
        "Very Poor": "Avoid prolonged outdoor exertion.",
        "Severe": "Limit outdoor exposure and follow local health advisories."
    }

    return messages.get(category, "Check local air-quality guidance.")