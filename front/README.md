<p align="center">
  <img src="https://img.shields.io/github/license/joelle-jnbaptiste/SchoolProject---Autonomous-driving-image-segmentation?style=for-the-badge" />
  <img src="https://img.shields.io/badge/School%20Project-Computer%20Vision-blueviolet?style=for-the-badge" />
</p>

<h1 align="center">✨ Streamlit Image Segmentation Frontend ✨</h1>

<div align="center">
  <em>
    Visualizing machine perception, one pixel at a time
  </em>
  </br>

  <b>
    Streamlit frontend application to interact with a FastAPI image segmentation backend
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
    <li>Getting Started</li>
    <li>Repository Structure</li>
    <li>License</li>
    <li>Contact</li>
  </ol>
</details>

---

### ✨ Built With

[![Python][Python-shield]][Python-url]
[![Streamlit][Streamlit-shield]][Streamlit-url]
[![NumPy][NumPy-shield]][NumPy-url]
[![Pillow][Pillow-shield]][Pillow-url]
[![Requests][Requests-shield]][Requests-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🎯 About The Project

This frontend application provides a simple web interface to test an image segmentation API.

It allows users to:
- Upload an image from their local machine
- Send the image to a FastAPI backend
- Display the original image
- Display the predicted semantic segmentation mask

The frontend is designed to validate the full end-to-end pipeline from image input to model inference.

---

## 🗃️ Dataset

The project is based on the **Cityscapes** dataset, a reference dataset for urban scene understanding.

Dataset overview:

    https://www.cityscapes-dataset.com/dataset-overview/

The dataset includes:
- Urban street images
- Pixel-level semantic annotations
- Multiple object classes such as road, vehicles, pedestrians, buildings, and vegetation

---

## 🏰 System Architecture

The frontend acts as a client layer in the system:

- Streamlit provides the user interface
- Images are uploaded through the browser
- Requests are sent to the FastAPI backend
- The backend returns a segmentation mask
- The frontend displays both input and output images

---

## ⚔️ Getting Started

### 1. Create and activate a virtual environment

    python -m venv env

    source env/bin/activate        # Linux / macOS
    env\Scripts\activate           # Windows

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Run the Streamlit application

    streamlit run app.py

### 4. Access the application

    Open your browser at:
        http://localhost:8501

Ensure that the FastAPI backend is running before using the frontend.

---

## 🗺️ Repository Structure

    front/
    ├── app.py                 # Streamlit application
    ├── requirements.txt       # Python dependencies
    ├── install-app.sh
    ├── install-conda.sh
    ├── .gitignore
    └── README.md

---

## ✒️ License

This project is intended for educational and demonstration purposes.

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

[Streamlit-shield]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/

[NumPy-shield]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[Pillow-shield]: https://img.shields.io/badge/Pillow-8A2BE2?style=for-the-badge
[Pillow-url]: https://python-pillow.org/

[Requests-shield]: https://img.shields.io/badge/Requests-2C2C2C?style=for-the-badge
[Requests-url]: https://docs.python-requests.org/
