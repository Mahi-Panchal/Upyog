import torch
import gdown
import os
import torch.nn as nn
from torchvision import models

MODEL_PATH = "waste_classifier.pth"

def download_model():

    if not os.path.exists(MODEL_PATH):

        file_id = "YOUR_FILE_ID_HERE"

        url = f"https://drive.google.com/uc?id=https://drive.google.com/file/d/1poyQwfmxso842-2MeB8UOYmI61IJouxQ/view?usp=drive_link"

        gdown.download(url, MODEL_PATH, quiet=False, fuzzy=True)

def load_model():

    download_model()

    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 6)

    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))

    model.eval()

    return model
