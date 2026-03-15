import streamlit as st
import torch
from PIL import Image
import torch.nn.functional as F

from model_loader import load_model
from preprocess import preprocess_image
from agent import waste_agent

# Page configuration
st.set_page_config(
    page_title="Upyog - Waste Classification Agent",
    page_icon="♻️",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>

.big-title {
    font-size:50px !important;
    font-weight:700;
    text-align:center;
    color:#2E8B57;
}

.subtitle {
    text-align:center;
    font-size:18px;
    color:gray;
}

.prediction-box {
    background-color:#f0f8f5;
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-size:20px;
    color:black;   /* FIX */
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-title">♻️ Upyog</p>', unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">AI Powered Waste Classification & Disposal Assistant</p>',
unsafe_allow_html=True
)

st.write("")
st.write("Upload an image of waste and the AI agent will classify it and suggest the correct disposal method.")

# Load model
model = load_model()

classes = [
'cardboard',
'glass',
'metal',
'paper',
'plastic',
'trash'
]

st.divider()

# Upload section
uploaded_file = st.file_uploader(
    "Upload Waste Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file:

    col1, col2 = st.columns(2)

    image = Image.open(uploaded_file)

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    img = preprocess_image(image)

    with torch.no_grad():

        outputs = model(img)

        probs = F.softmax(outputs[0], dim=0)

        confidence, pred = torch.max(probs, 0)

        label = classes[pred]

    action = waste_agent(label)

    with col2:

        st.subheader("Prediction Result")

        st.markdown(
             f"""
             <div class="prediction-box">
                Waste Type: {label.capitalize()} <br>
                Confidence: {confidence.item()*100:.2f}%
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.subheader("AI Agent Recommendation")

        st.success(action)

st.divider()

st.caption("Upyog • AI Waste Classification Agent")
