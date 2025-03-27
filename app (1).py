
import streamlit as st

st.title("MVP Web App")

# Add user instructions
st.write("This is a prototype web app based on your notebook.")

# Run the notebook code
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from torchvision import datasets
from PIL import Image
import requests
from io import BytesIO
import json
import numpy as np
from tqdm import tqdm
from loguru import logger

# Load Pretrained Model Efficiently
logger.info("Loading pre-trained model...")
model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
model.eval()

# Define Image Processing Transform
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load and Process Image Efficiently
def load_image(image_url, backup_url=None):
    try:
        logger.info(f"Downloading image from: {image_url}")
        response = requests.get(image_url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert('RGB')
        return transform(image).unsqueeze(0)
    except requests.RequestException as e:
        logger.error(f"Failed to download image: {e}")
        if backup_url:
            logger.info(f"Trying backup image: {backup_url}")
            return load_image(backup_url)  # Recursive call with backup URL
        return None
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        return None

# Image Classification Function
def classify_image(image_tensor):
    if image_tensor is None:
        return "No valid image provided."
    with torch.no_grad():
        output = model(image_tensor)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    class_index = torch.argmax(probabilities).item()
    return f"Predicted Class Index: {class_index}"

# Sample Image URL (Replaced broken URL with a working one)
image_url = "https://upload.wikimedia.org/wikipedia/commons/4/4c/Push_van_cat.jpg"  # New valid image (a cat)
backup_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"  # Backup image
image_tensor = load_image(image_url, backup_url)
print(classify_image(image_tensor))

# Simulated Sensor Data Handling
def process_sensor_data():
    sensor_data = {
        "temperature": np.random.uniform(20, 30),
        "humidity": np.random.uniform(50, 70),
        "soil_moisture": np.random.uniform(30, 50)
    }
    logger.info("Processing sensor data...")
    return json.dumps({"message": "Sensor data received", "data": sensor_data}, indent=4)

print(process_sensor_data())

