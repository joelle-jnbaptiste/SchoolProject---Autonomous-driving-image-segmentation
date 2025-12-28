<p align="center">
  <img src="https://img.shields.io/github/license/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation?style=for-the-badge" />
  <img src="https://img.shields.io/badge/School%20Project-Computer%20Vision-blueviolet?style=for-the-badge" />
</p>

<h1 align="center">✨ FastAPI Image Segmentation API ✨</h1>

<div align="center">
  <em>
    Turning raw images into semantic understanding
  </em>
  </br>

  <b>
    FastAPI backend providing semantic image segmentation inference for autonomous driving use cases
  </b>
  </br>
  </br>

  🗃️ <b>Dataset</b>

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
    <li>API Endpoint</li>
    <li>Getting Started</li>
    <li>Repository Structure</li>
    <li>License</li>
    <li>Contact</li>
  </ol>
</details>

---

### ✨ Built With

[![Python][Python-shield]][Python-url]
[![FastAPI][FastAPI-shield]][FastAPI-url]
[![TensorFlow][TensorFlow-shield]][TensorFlow-url]
[![NumPy][NumPy-shield]][NumPy-url]
[![Pillow][Pillow-shield]][Pillow-url]
[![Uvicorn][Uvicorn-shield]][Uvicorn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🎯 About The Project

This backend service exposes a FastAPI application that performs semantic image segmentation
using a pretrained deep learning model.

The API is designed to:
- Accept RGB images via HTTP requests
- Apply preprocessing (resize and normalization)
- Run inference using a trained segmentation model
- Return a colorized segmentation mask

The service is intended to be used as part of an end-to-end autonomous driving system.

---

## 🗃️ Dataset

This project is based on the **Cityscapes** dataset, a benchmark dataset for urban scene understanding.

Dataset overview:

    https://www.cityscapes-dataset.com/dataset-overview/

The dataset provides:
- Street-level images captured in urban environments
- Pixel-level annotations for semantic segmentation
- Multiple semantic classes such as road, cars, pedestrians, buildings, and vegetation

---

## 🏰 System Architecture

The backend is a standalone inference service:

- FastAPI handles HTTP requests
- An image preprocessing pipeline prepares inputs
- A trained TensorFlow/Keras model performs segmentation
- Postprocessing converts model output into a visual mask
- The result is returned as a PNG image

---

## 🪄 API Endpoint

### POST /predict

Upload an image and receive the predicted segmentation mask.

**Request**
- Method: POST
- Content-Type: multipart/form-data
- Parameter:
  
      file: RGB image (PNG or JPG)

**Response**
- PNG image representing the predicted segmentation mask

---

## ⚔️ Getting Started

### 1. Create and activate a virtual environment

    python -m venv env

    source env/bin/activate        # Linux / macOS
    env\Scripts\activate           # Windows

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Run the API server

    uvicorn main:app --reload

### 4. Access the API

    API root:
        http://127.0.0.1:8000

    Interactive documentation:
        http://127.0.0.1:8000/docs

---

## 🗺️ Repository Structure

    back/
    ├── main.py               # FastAPI application entrypoint
    ├── model/
    │   └── your_model.keras  # Trained segmentation model
    ├── requirements.txt
    ├── install-app.sh
    ├── install-conda.sh
    └── README.md

---

## ✒️ License

This project is provided for educational purposes.

---

## 🕊️ Contact

Joëlle JEAN BAPTISTE  
LinkedIn:

    https://fr.linkedin.com/in/joëllejnbaptiste

Project Link:

    https://github.com/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[FastAPI-shield]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/

[TensorFlow-shield]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/

[NumPy-shield]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[Pillow-shield]: https://img.shields.io/badge/Pillow-8A2BE2?style=for-the-badge
[Pillow-url]: https://python-pillow.org/

[Uvicorn-shield]: https://img.shields.io/badge/Uvicorn-2C2C2C?style=for-the-badge
[Uvicorn-url]: https://www.uvicorn.org/
