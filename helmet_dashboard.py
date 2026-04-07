import streamlit as st
import random
import time

st.set_page_config(page_title="RoadSense Helmet Dashboard", layout="wide")

st.title("🪖 RoadSense Smart Helmet Dashboard")

st.sidebar.title("Simulation Controls")

scenario = st.sidebar.selectbox(
    "Scenario",
    ["Normal Ride", "Crash Event", "Gas Leak", "High Heart Rate"]
)

gas_threshold = st.sidebar.slider("Gas Alert Threshold", 100, 600, 300)
bpm_threshold = st.sidebar.slider("Heart Rate Warning", 100, 180, 140)

def simulate_data(mode):

    if mode == "Normal Ride":
        return {"status":"SAFE","bpm":72,"gas":120,"tilt":"Stable"}

    if mode == "Crash Event":
        return {"status":"CRASH","bpm":110,"gas":140,"tilt":"Critical"}

    if mode == "Gas Leak":
        return {"status":"SAFE","bpm":75,"gas":420,"tilt":"Stable"}

    if mode == "High Heart Rate":
        return {"status":"SAFE","bpm":165,"gas":130,"tilt":"Stable"}

data = simulate_data(scenario)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Helmet Status",data["status"])
col2.metric("Heart Rate",f'{data["bpm"]} BPM')
col3.metric("Gas Level",data["gas"])
col4.metric("Tilt",data["tilt"])

st.divider()

st.subheader("System Alerts")

if data["status"]=="CRASH":
    st.error("🚨 Accident Detected – Emergency Alert Sent")

elif data["gas"]>gas_threshold:
    st.warning("⚠ Gas Level Above Safe Threshold")

elif data["bpm"]>bpm_threshold:
    st.warning("💓 Abnormal Heart Rate Detected")

else:
    st.success("✔ All Systems Normal")

st.divider()

st.subheader("Event Log")

st.write("System Monitoring Started")
st.write("Sensors Active")
st.write("ESP32 Connected")

time.sleep(1)
