import streamlit as st
import cv2
import numpy as np
import pytesseract

st.title("Reconocimiento óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    blurred = cv2.GaussianBlur(thresh, (5, 5), 0)

    img_rgb = cv2.cvtColor(blurred, cv2.COLOR_GRAY2RGB)
    text = pytesseract.image_to_string(img_rgb)
    st.write(text)
    st.image(blurred, caption = "Imagen procesada", use_column_width=True)
    


