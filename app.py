import streamlit as st
from datetime import datetime
import os

st.title("Lab Reports Name Formatter")

uploaded_file = st.file_uploader("Upload report PDF", type=["pdf"])

labs = ["Vermicon", "GBA", "Plenum"]

if uploaded_file:
    uploaded_file_name = os.path.basename(uploaded_file.name)
    base_name = os.path.splitext(uploaded_file_name)[0]  # remove .pdf
    st.success(f"File uploaded: {uploaded_file_name}")

    number = st.selectbox("How many SKUs in file?", list(range(1, 10)))
    date_input = st.date_input("Select Date")
    date_str = date_input.strftime("%d.%m.%Y")
    lab = st.selectbox("Select Lab", labs)

    if number > 1:
        sku_input = st.text_input("Enter SKUs separated by commas (e.g., N8673C,N8717C)", max_chars=100)
        skus = [sku.strip() for sku in sku_input.split(",") if sku.strip()]
    else:
        sku_input = st.text_input("Enter SKU", max_chars=20)
        skus = [sku_input.strip()] if sku_input.strip() else []

    if skus:
        sku_part = "&".join(skus)
        new_filename = f"{base_name}_{sku_part}_{lab}_{date_str}.pdf"
        st.write("### New File Name:")
        st.code(new_filename)

        # Optionally, provide a download button (without saving to disk)
        st.download_button(
            label="Download Renamed File",
            data=uploaded_file.getvalue(),
            file_name=new_filename,
            mime="application/pdf"
        )
    else:
        st.warning("Please enter at least one SKU.")
else:
    st.info("Please upload a PDF file.")
