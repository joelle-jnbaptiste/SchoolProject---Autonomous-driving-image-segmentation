import streamlit as st
from PIL import Image
import numpy as np
import requests
import io

st.title("Démo de segmentation")

uploaded_file = st.file_uploader(
    "Choisis une image :", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Image d’origine", use_container_width=True
             )

    if st.button("Lancer la prédiction"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(
            "http://3.82.102.173:8000/predict", files={"file": files["file"]})

        if response.status_code == 200:
            pred_image = Image.open(io.BytesIO(response.content))
            st.image(pred_image, caption="Image prédite",
                     use_container_width=True
                     )
        else:
            st.error("Erreur pendant la prédiction.")
