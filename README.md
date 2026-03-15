# ♻️ Upyog – AI Waste Classification Agent

Upyog is an AI-powered waste classification system that identifies different types of waste from images and suggests the correct disposal method.

The goal of this project is to promote better waste management by helping users quickly determine how to dispose of everyday waste items.

---

## 🚀 Features

* Upload an image of waste
* AI model classifies the waste type
* AI agent suggests proper disposal methods
* Clean web interface built with Streamlit
* Model automatically downloaded from GitHub Release
* Fast predictions using PyTorch

---

## 🧠 Waste Categories

The model is trained on the **Garbage Classification Dataset** with the following classes:

| Waste Type | Images |
| ---------- | ------ |
| Cardboard  | 393    |
| Glass      | 491    |
| Metal      | 400    |
| Paper      | 584    |
| Plastic    | 472    |
| Trash      | 127    |

---

## 🛠 Tech Stack

* Python
* PyTorch
* Streamlit
* Google Colab (for training)
* GitHub (for deployment & model hosting)

---

## 📂 Project Structure

```
upyog
│
├── app.py                # Streamlit web app
├── model_loader.py       # Downloads and loads trained model
├── preprocess.py         # Image preprocessing
├── agent.py              # AI waste recommendation agent
├── requirements.txt      # Python dependencies
└── README.md
```

---

## ⚙️ How the System Works

1. User uploads an image through the Streamlit web app.
2. The image is preprocessed.
3. The trained PyTorch model predicts the waste type.
4. The AI agent provides a disposal recommendation.
5. The result is displayed in the web interface.

---

## 🧪 Model Training

The model is trained in **Google Colab** using PyTorch.

Steps:

1. Upload dataset to Colab
2. Train CNN model
3. Save model as `.pth`
4. Upload model to GitHub Releases
5. App downloads the model automatically when running

---

## 💻 Running the Project Locally

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/upyog.git
cd upyog
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit app:

```
streamlit run app.py
```

---

## 🌐 Deployment

The project is deployed using Streamlit Cloud.

Steps:

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy the app
4. Model downloads automatically from GitHub Releases

---

## 📷 Example Workflow

1. Upload an image of waste
2. Model predicts the category
3. AI agent suggests proper disposal method

Example output:

```
Waste Type: Plastic
Confidence: 92.3%

Recommendation:
Send to plastic recycling facility
```

---

## 🌍 Purpose

Improper waste disposal is a major environmental issue.
Upyog aims to make waste identification easier using AI and encourage responsible recycling habits.

---

## 🔮 Future Improvements

* More waste categories
* Real-time camera detection
* Mobile application
* Recycling center locator
* Environmental impact score

---

## 📜 License

This project is for educational and research purposes.
