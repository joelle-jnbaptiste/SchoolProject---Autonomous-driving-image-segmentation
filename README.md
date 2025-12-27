[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">


  <h1 align="center">🏰 SchoolProject — Autonomous Driving Image Segmentation</h1>

  <p align="center">
    🪄 End-to-end image segmentation system for autonomous driving — from model training to an inference API and a visualization web app, designed with embedded computer vision constraints in mind.
    <br />
    <br />
    🗺️ <a href="https://www.cityscapes-dataset.com/dataset-overview/"><strong>Dataset (Cityscapes) »</strong></a>
    ·
    🧙 <a href="#"><strong>Project Repository</strong></a>
  </p>
</div>

---

## ✨ About The Project

Welcome, traveler.

This repository is a **full end-to-end semantic segmentation platform** built for an autonomous driving use case.  
It unifies three core pillars into a single, coherent project:

- 🧠 **Modelisation** — train and evaluate segmentation models (PyTorch and TensorFlow notebooks)
- 🏹 **Backend** — serve predictions through a FastAPI inference API
- 🪄 **Frontend** — visualize predictions with a Streamlit web interface

The mission is to transform raw road scene images into **semantic maps**, enabling a system to understand the environment (road, vehicles, pedestrians, buildings, vegetation, etc.).  
The implementation is deliberately structured with a production mindset: **reproducible training**, **portable inference**, and **user-facing visualization**.

---

## ⚔️ Built With

<!-- Badge-style "gommettes" (vignettes) -->
![Python][python-shield]
![PyTorch][pytorch-shield]
![TensorFlow][tensorflow-shield]
![FastAPI][fastapi-shield]
![Streamlit][streamlit-shield]
![Docker][docker-shield]
![GitHub Actions][gha-shield]

---

## 🗺️ Project Structure

    SchoolProject---Autonomous-driving-image-segmentation/
    │
    ├── back/                          # 🏹 FastAPI inference backend
    │   ├── .github/workflows/          # ⚙️ CI pipelines
    │   │   └── master_onboard-system-api.yml
    │   ├── model/                      # 🧪 Inference artifacts (TFLite)
    │   │   └── model_quant.tflite
    │   ├── main.py                     # ⚡ API entrypoint
    │   ├── requirements.txt            # 📦 Backend deps
    │   ├── install-app.sh              # 🧰 Setup helper
    │   └── install-conda.sh            # 🧰 Setup helper
    │
    ├── front/                          # 🪄 Streamlit visualization app
    │   ├── app.py                      # 🎨 Frontend app
    │   ├── requirements.txt            # 📦 Frontend deps
    │   ├── install-app.sh              # 🧰 Setup helper
    │   └── install-conda.sh            # 🧰 Setup helper
    │
    ├── modelisation/                   # 🧠 Training & experiments
    │   ├── modelisationPytorch.ipynb
    │   ├── modelisationTensorflow.ipynb
    │   └── README.md
    │
    └── README.md

---

## 🗃️ Dataset

This project is based on an autonomous driving semantic segmentation benchmark dataset:

- 🏙️ **Cityscapes — Dataset Overview**: https://www.cityscapes-dataset.com/dataset-overview/

The dataset provides urban street scene images and pixel-level annotations for multiple semantic classes (road, cars, pedestrians, buildings, vegetation, sky, etc.).  
In this project, the dataset is used to train segmentation models and validate qualitative/quantitative performance.

---

## 🧠 Modelisation

Inside `modelisation/`, you’ll find notebooks covering:

- 🧪 Dataset loading & preprocessing (resize, normalization, augmentation if applicable)
- 📉 Training loops / training strategy (loss tracking, validation monitoring)
- 🧭 Evaluation (mIoU / IoU, qualitative mask visualization)
- 🧩 Cross-framework experimentation:
  - 🔥 PyTorch notebook for training & evaluation
  - 🌀 TensorFlow notebook for alternative training and/or export compatibility

---

## 🏹 Backend — FastAPI Inference API

The `back/` domain exposes a lightweight prediction service:

- Accepts an input image via HTTP
- Applies preprocessing
- Runs inference using a **quantized TFLite model** (`model_quant.tflite`)
- Produces a segmentation mask (and optional color mapping / encoding)
- Returns the predicted mask to the client

### ✅ Main Endpoint (example)
- `POST /predict` — upload an image and receive the predicted segmentation output

---

## 🪄🎨 Frontend — Streamlit App

The `front/` domain is a simple interactive app to:

- Upload an image
- Send it to the backend API
- Display the original + segmentation prediction
- Quickly test the system end-to-end

---

## 🧭 Quickstart

### 🏹 Run the Backend (FastAPI)

    cd back
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload

### 🪄 Run the Frontend (Streamlit)

    cd front
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    streamlit run app.py

---

## 🎓 What This Project Demonstrates

- 🧠 End-to-end ML thinking (training → serving → UX)
- 🗺️ Semantic segmentation fundamentals
- 🏹 Inference API design (FastAPI)
- 🪄 A lightweight visualization layer (Streamlit)
- 🧰 Engineering hygiene (clear structure, scripts, CI-ready layout)

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🔮 Contact

Joëlle JEAN-BAPTISTE — via LinkedIn: [LinkedIn][linkedin-url]

---

<!-- MARKDOWN LINKS & IMAGES (shields / badges) -->
[stars-shield]: https://img.shields.io/github/stars/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation.svg?style=for-the-badge
[stars-url]: https://github.com/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation/stargazers
[issues-shield]: https://img.shields.io/github/issues/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation.svg?style=for-the-badge
[issues-url]: https://github.com/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation/issues
[license-shield]: https://img.shields.io/github/license/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation.svg?style=for-the-badge
[license-url]: https://github.com/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/

[python-shield]: https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white
[pytorch-shield]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[tensorflow-shield]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[fastapi-shield]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[streamlit-shield]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[docker-shield]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[gha-shield]: https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white
