import torch
import torch.nn as nn
from torchvision import models
import requests
import os
import streamlit as st

MODEL_PATH = "waste_classifier.pth"

# Replace this with your GitHub release file link
MODEL_URL = "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/releases/download/v1.0/waste_classifier.pth"


def download_model():
    
    if not os.path.exists(MODEL_PATH):

        response = requests.get(MODEL_URL)

        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)


@st.cache_resource
def load_model():

    download_model()

    model = models.resnet18(weights=None)

    model.fc = nn.Linear(model.fc.in_features, 6)

    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))

    model.eval()

    return model
