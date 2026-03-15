import torch
import os
import requests
import torch.nn as nn
from torchvision import models

MODEL_PATH = "waste_classifier.pth"

FILE_ID = "https://drive.google.com/file/d/1poyQwfmxso842-2MeB8UOYmI61IJouxQ/view?usp=drive_link"

DOWNLOAD_URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"


def download_model():

    if not os.path.exists(MODEL_PATH):

        response = requests.get(DOWNLOAD_URL)

        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)


def load_model():

    download_model()

    model = models.resnet18(pretrained=False)

    model.fc = nn.Linear(model.fc.in_features, 6)

    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))

    model.eval()

    return model
