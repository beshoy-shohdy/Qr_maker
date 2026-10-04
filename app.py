import streamlit as st
import qrcode
from io import BytesIO

st.title("QR Code Generator")

data = st.text_input("Enter text")

if st.button("Generate QR Code"):
    qr = qrcode.make(data)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    st.image(buffer.getvalue())

    st.download_button(
        label="Download QR Code",
        data=buffer.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )