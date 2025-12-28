<p align="center">
  <img src="https://img.shields.io/github/license/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation?style=for-the-badge" />
  <img src="https://img.shields.io/badge/School%20Project-Computer%20Vision%20%26%20ML-blueviolet?style=for-the-badge" />
</p>

<h1 align="center">✨ Autonomous Driving Image Segmentation ✨</h1>

<div align="center">
  <em>
     *Teaching machines to see the road through pixels and patterns*
  </em>
</br>

 <b>End-to-end semantic segmentation system for autonomous driving, from model training to real-time inference and visualization</b>
</br>
</br>
🗃️ **Dataset**  
https://www.cityscapes-dataset.com/dataset-overview/
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>🧭 Table of Contents</summary>
  <ol>
    <li>About The Project</li>
    <li>Dataset</li>
    <li>System Architecture</li>
    <li>Models & Training</li>
    <li>Evaluation</li>
    <li>Repository Structure</li>
    <li>Getting Started</li>
  </ol>
</details>

---

### ✨ Built With

[![Python][Python-shield]][Python-url]
[![PyTorch][PyTorch-shield]][PyTorch-url]
[![TensorFlow][TensorFlow-shield]][TensorFlow-url]
[![FastAPI][FastAPI-shield]][FastAPI-url]
[![Streamlit][Streamlit-shield]][Streamlit-url]
[![Docker][Docker-shield]][Docker-url]
[![GitHub Actions][GHA-shield]][GHA-url]

<p align="right">(<a href="#top">back to top</a>)</p>

---

## 🎯 About The Project

This project implements a **full end-to-end semantic segmentation pipeline** designed for an autonomous driving use case.

It is structured into three complementary components:

- **Modelisation** – training and evaluation of segmentation models
- **Backend** – FastAPI inference service for image segmentation
- **Frontend** – Streamlit interface to visualize predictions

The project follows a **production-oriented approach**, focusing on reproducibility, modularity, and deployment constraints.

---

## 🗃️ Dataset

This project is based on the **Cityscapes** dataset, a large-scale benchmark designed for urban scene understanding in autonomous driving.

https://www.cityscapes-dataset.com/dataset-overview/

### Dataset Overview

The dataset contains high-resolution street-view images with fine-grained pixel-level annotations, including:

- Roads
- Cars
- Pedestrians
- Buildings
- Vegetation
- Sky
- Traffic signs and objects

### Usage in This Project

In this project, the dataset is used to:

- Train semantic segmentation models
- Evaluate qualitative and quantitative performance
- Demonstrate an end-to-end computer vision pipeline
- Validate inference constraints for embedded or production environments

Only a subset of the dataset is used for experimentation and demonstration purposes.


---

## 🏰 System Architecture

The system follows a simple but realistic architecture:

- Training and experimentation performed offline in notebooks
- Export of a trained segmentation model
- Inference served through a FastAPI backend
- Visualization and testing via a Streamlit frontend

This separation allows independent iteration on modeling, inference, and user interaction layers.

---

## 🪄 Models & Training

Inside the `modelisation/` directory, notebooks cover:

- Dataset loading and preprocessing
- Data augmentation and normalization
- Model training and validation
- Quantitative and qualitative evaluation
- Cross-framework experiments (PyTorch and TensorFlow)

The final model is exported in a lightweight format suitable for inference.

---

## 👑 Evaluation

Model performance is assessed using:
- Visual inspection of predicted segmentation masks
- Comparison with ground-truth annotations
- Qualitative analysis of class-wise behavior

The focus is placed on **interpretability and robustness**, rather than raw benchmark optimization.

---

## 🗺️ Repository Structure

    SchoolProject---Autonomous-driving-image-segmentation/
    ├── back/                     # FastAPI inference backend
    │   ├── api/
    │   ├── model/
    │   ├── main.py
    │   └── requirements.txt
    │
    ├── front/                    # Streamlit visualization app
    │   ├── app.py
    │   └── requirements.txt
    │
    ├── modelisation/             # Training & experiments
    │   ├── notebooks
    │   └── README.md
    │
    └── README.md

---

## ⚔️ Getting Started

This project is composed of three independent parts:
- model training and experimentation
- a FastAPI inference backend
- a Streamlit visualization frontend

You can run each component separately depending on your objective.

---

### 1️⃣ Model Training & Experiments (optional)

If you want to explore or retrain the segmentation models:

    cd modelisation
    python -m venv .venv
    source .venv/bin/activate        # Linux / macOS
    .venv\Scripts\activate           # Windows

    pip install -r requirements.txt

Open the notebooks to:
- load and preprocess the Cityscapes dataset
- train segmentation models
- evaluate predictions visually
- export a trained model for inference

---

### 2️⃣ Run the Backend (FastAPI)

The backend exposes an HTTP API for image segmentation.

    cd back
    python -m venv .venv
    source .venv/bin/activate        # Linux / macOS
    .venv\Scripts\activate           # Windows

    pip install -r requirements.txt

Start the API server:

    uvicorn main:app --reload

The API will be available locally and ready to receive image requests.

---

### 3️⃣ Run the Frontend (Streamlit)

The frontend allows you to test the system end-to-end through a web interface.

    cd front
    python -m venv .venv
    source .venv/bin/activate        # Linux / macOS
    .venv\Scripts\activate           # Windows

    pip install -r requirements.txt

Launch the Streamlit app:

    streamlit run app.py

You can then:
- upload an image
- send it to the backend API
- visualize the predicted segmentation mask

---

### 4️⃣ Full End-to-End Test

To test the complete pipeline:

1. Start the FastAPI backend
2. Launch the Streamlit frontend
3. Upload an image in the UI
4. Inspect the segmentation output

This simulates a simplified production workflow:
**model → API → user interface**


---

## ✒️ License

This project is provided for educational purposes only.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## 🕊️ Contact

Joëlle JEAN BAPTISTE  
LinkedIn:

    https://fr.linkedin.com/in/jo%C3%ABllejnbaptiste

Project Repository:

    https://github.com/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation

<p align="right">(<a href="#top">back to top</a>)</p>

---

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[PyTorch-shield]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[PyTorch-url]: https://pytorch.org/

[TensorFlow-shield]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/

[FastAPI-shield]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/

[Streamlit-shield]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/

[Docker-shield]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[GHA-shield]: https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white
[GHA-url]: https://github.com/features/actions
