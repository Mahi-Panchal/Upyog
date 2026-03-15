import torch
import gdown
import os
import torch.nn as nn
from torchvision import models

MODEL_PATH = "waste_classifier.pth"

def download_model():

    if not os.path.exists(MODEL_PATH):

        file_id = "PASTE_DRIVE_FILE_ID"

        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(url,MODEL_PATH,quiet=False)

def load_model():

    download_model()

    model = models.resnet18(pretrained=False)

    model.fc = nn.Linear(model.fc.in_features,6)

    model.load_state_dict(torch.load(MODEL_PATH,map_location="cpu"))

    model.eval()

    return model
