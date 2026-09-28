import streamlit as st
import pandas as pd
import plotly.express as px

from prediction import (
    predict_aqi,
    get_aqi_category,
    get_health_message
)

# Page configuration
st.set_page_config(
    page_title="AQI Monitoring Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    color: #176B87;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 Air Quality Index Monitoring & Prediction")
st.write("Monitor pollutant levels and estimate air quality using Machine Learning.")

st.divider()

# Sidebar
st.sidebar.header("📍 Monitoring Details")

city = st.sidebar.text_input(
    "Enter City Name",
    value="Kakinada"
)

st.sidebar.info(
    "Enter pollutant readings to estimate the AQI."
)

# Main input section
st.subheader("Enter Air Pollutant Values")

col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input(
        "PM2.5 (µg/m³)",
        min_value=0.0,
        max_value=1000.0,
        value=25.0
    )

    pm10 = st.number_input(
        "PM10 (µg/m³)",
        min_value=0.0,
        max_value=1000.0,
        value=50.0
    )

with col2:
    no2 = st.number_input(
        "NO2 (µg/m³)",
        min_value=0.0,
        max_value=1000.0,
        value=20.0
    )

    so2 = st.number_input(
        "SO2 (µg/m³)",
        min_value=0.0,
        max_value=1000.0,
        value=10.0
    )

with col3:
    co = st.number_input(
        "CO (mg/m³)",
        min_value=0.0,
        max_value=100.0,
        value=0.5
    )

    o3 = st.number_input(
        "O3 (µg/m³)",
        min_value=0.0,
        max_value=1000.0,
        value=30.0
    )

# Prediction button
if st.button("🔍 Predict AQI", type="primary"):

    if not city.strip():
        st.warning("Please enter a city name.")

    else:
        aqi = predict_aqi(
            pm25, pm10, no2, so2, co, o3
        )

        category = get_aqi_category(aqi)

        message = get_health_message(category)

        # Save prediction history
        if "history" not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append({
            "City": city,
            "AQI": aqi,
            "Category": category
        })

        st.divider()

        st.subheader("📊 AQI Prediction Results")

        metric1, metric2, metric3 = st.columns(3)

        metric1.metric("Predicted AQI", aqi)

        metric2.metric("Air Quality", category)

        metric3.metric("Monitoring Location", city)

        # AQI category message
        if aqi <= 50:
            st.success(f"🟢 {message}")

        elif aqi <= 100:
            st.info(f"🟡 {message}")

        elif aqi <= 200:
            st.warning(f"🟠 {message}")

        else:
            st.error(f"🔴 {message}")

        # Pollutant chart
        pollutant_data = pd.DataFrame({
            "Pollutant": [
                "PM2.5", "PM10", "NO2",
                "SO2", "CO", "O3"
            ],
            "Value": [
                pm25, pm10, no2,
                so2, co, o3
            ]
        })

        st.subheader("Pollutant Levels")

        fig = px.bar(
            pollutant_data,
            x="Pollutant",
            y="Value",
            color="Pollutant",
            title="Measured Pollutant Values",
            text_auto=True
        )

        st.plotly_chart(fig, use_container_width=True)

# Prediction history
st.divider()

st.subheader("📈 Prediction History")

if "history" in st.session_state and st.session_state.history:

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True
    )

    # History chart
    fig_history = px.line(
        history_df,
        x=history_df.index,
        y="AQI",
        markers=True,
        title="AQI Prediction Trend"
    )

    fig_history.update_layout(
        xaxis_title="Prediction Number",
        yaxis_title="AQI"
    )

    st.plotly_chart(
        fig_history,
        use_container_width=True
    )

    # Download history
    csv = history_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Prediction History",
        data=csv,
        file_name="aqi_prediction_history.csv",
        mime="text/csv"
    )

else:
    st.info("No predictions available yet. Enter values and click Predict AQI.")

# Footer
st.divider()

st.caption(
    "AQI Monitoring and Prediction Dashboard | "
    "Machine Learning College Project"
)

st.caption(
    "Educational demonstration using a synthetic dataset. "
    "Predictions are not official air-quality readings."
)