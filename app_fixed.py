 
import streamlit as st

# App Title
st.title("🌿 AI-Powered Biodiversity Restorer - MVP")

# Team Information
st.sidebar.header("🚀 Team Details")
st.sidebar.write("**Team Name:** NovaForge")
st.sidebar.write("**Team Leader:** Mushahidha Kani K.")

# Problem Statement
st.header("🌎 Problem Statement")
st.write(
    "Biodiversity loss due to habitat destruction, climate change, and pollution threatens ecosystems worldwide. "
    "An AI-powered biodiversity restorer can analyze degraded ecosystems, recommend species-specific interventions, "
    "and monitor progress using real-time data, ensuring targeted and scalable restoration efforts."
)

# Solution Overview
st.header("🤖 AI-Powered Biodiversity Restoration")
st.write(
    "This system uses artificial intelligence to monitor, analyze, and restore ecosystems by improving biodiversity. "
    "It integrates:
"
    "- **Ecosystem Monitoring** with IoT sensors & drones
"
    "- **AI-Driven Analysis** for predictive modeling & real-time decision-making
"
    "- **Autonomous Restoration** via robots & drones
"
    "- **Community Science** through citizen engagement"
)

# Key Features
st.header("🔑 Key Features")
features = [
    "Ecosystem Monitoring & Analysis",
    "AI-Driven Data Analysis & Prediction",
    "Habitat Reforestation",
    "Wildlife Conservation & Protection",
    "Sustainable Agriculture & Land Management",
    "Community Engagement & Citizen Science"
]
for feature in features:
    st.write(f"✅ {feature}")

# Architecture Overview
st.header("🛠 Architecture & Technologies")

st.subheader("🔹 Hardware Components")
hardware = [
    "IoT Sensors (LoRa, Zigbee, MQTT) for environmental monitoring",
    "Drones (DJI, Parrot) with Computer Vision for species detection",
    "Satellite Data (NASA Earth Observation, Sentinel-2) for land tracking",
    "Edge Computing (NVIDIA Jetson, Raspberry Pi) for real-time AI inference",
    "Autonomous Robots (Boston Dynamics, Agility Robotics) for intervention"
]
for item in hardware:
    st.write(f"🔸 {item}")

st.subheader("🔹 Software & AI Components")
software = [
    "Computer Vision for species identification",
    "GIS for ecosystem mapping",
    "Predictive AI for biodiversity forecasting",
    "Real-time dashboards & mobile apps"
]
for item in software:
    st.write(f"🔹 {item}")

st.subheader("🔹 Cloud & Data Infrastructure")
cloud = [
    "Cloud Platforms: AWS, GCP, Azure",
    "Databases: PostgreSQL (PostGIS), MongoDB, Google BigQuery",
    "Stream Processing: Apache Kafka, Apache Spark",
    "Data Storage: S3, Google Cloud Storage, Azure Blob Storage"
]
for item in cloud:
    st.write(f"☁️ {item}")

# User Interaction (Future Scope)
st.header("📊 Future Scope: Live Ecosystem Analysis")
st.write("🚀 In future versions, users will be able to upload ecosystem data and get AI-driven restoration recommendations!")

st.success("🎉 MVP Ready! Deploy on Streamlit for a live version.")
