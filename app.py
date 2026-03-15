import streamlit as st
import torch
from PIL import Image
import torch.nn.functional as F

from model_loader import load_model
from preprocess import preprocess_image
from agent import waste_agent

st.title("♻️ AI Waste Classification Agent")

st.write("Upload an image of waste")

classes = [
'cardboard',
'glass',
'metal',
'paper',
'plastic',
'trash'
]

model = load_model()

file = st.file_uploader("Upload Image",type=["jpg","png","jpeg"])

if file:

    image = Image.open(file)

    st.image(image,width=300)

    img = preprocess_image(image)

    with torch.no_grad():

        outputs = model(img)

        probs = F.softmax(outputs[0],dim=0)

        confidence,pred = torch.max(probs,0)

        label = classes[pred]

    st.success(f"Prediction: {label}")

    st.write("Confidence:",float(confidence)*100,"%")

    action = waste_agent(label)

    st.info("Agent Recommendation:")

    st.write(action)
