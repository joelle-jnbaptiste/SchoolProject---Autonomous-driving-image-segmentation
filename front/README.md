```markdown
# Streamlit Frontend for Image Segmentation API

This is a simple Streamlit web app that allows users to upload an image, send it to a FastAPI backend for semantic segmentation, and display the predicted output image.

---

## 🚀 Features

- Upload a local `.png`, `.jpg`, or `.jpeg` image
- Displays the original uploaded image
- Sends the image to a FastAPI backend via HTTP POST
- Displays the predicted segmentation mask received from the API

---

## 🧱 Project Structure

```
ONBOARDSYSTEM_FRONT/
│
├── app.py             # Streamlit frontend code
├── requirements.txt   # Python dependencies
└── .gitignore         # Ignore env folder and cache
```

---

## ⚙️ Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate       # Linux/macOS
env\Scripts\activate          # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Streamlit App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🔁 Backend Configuration

The app sends the image to this backend endpoint:

```python
"http://127.0.0.1:8000/predict"
```

Make sure your FastAPI backend is running before using the app.

---

## 🧾 License

This project is intended for demonstration and educational use. You are free to modify and adapt it to your needs.
```
