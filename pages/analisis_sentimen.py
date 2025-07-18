import streamlit as st
import pandas as pd
import pickle
import numpy as np
from utils.preprocessing import clean_text
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

# Load model dan tokenizer
model = load_model('model/model_sentimen_lstm.h5')
with open('model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Fungsi prediksi
def predict_sentiment(texts):
    # Bersihkan teks sebelum prediksi
    cleaned_texts = [clean_text(text) for text in texts]
    sequences = tokenizer.texts_to_sequences(cleaned_texts)
    padded = pad_sequences(sequences, maxlen=100)
    preds = model.predict(padded)
    labels = ['Negatif', 'Netral', 'Positif']
    return [labels[np.argmax(p)] for p in preds]

# UI Streamlit
st.set_page_config(page_title="Analisis Sentimen", layout="wide")
st.markdown('<div class="title">Analisis Sentimen Pengunjung Hotel</div>', unsafe_allow_html=True)
st.markdown("""
    <hr style="
        border: none;
        height: 4px; /* tebal garis */
        background-color: black; /* warna garis */
        margin-top: -10px;
        margin-bottom: 20px;
    ">
""", unsafe_allow_html=True)
# Input teks manual
ulasan = st.text_area("Masukkan teks ulasan")
if st.button("Analisis"):
    if ulasan.strip() == "":
        st.warning("⚠️ Mohon masukkan ulasan terlebih dahulu.")
    else:
        hasil = predict_sentiment([ulasan])
        st.success(f"Hasil Sentimen: **{hasil[0]}**")


# Upload CSV
file = st.file_uploader("Unggah file CSV (catatan: file harus berisi kolom ulasan)", type=["csv"])
if file is not None:
    try:
        df = pd.read_csv(file)
        if 'ulasan' in df.columns:
            df['sentimen'] = predict_sentiment(df['ulasan'].astype(str))
            st.success("✅ Analisis berhasil!")
            st.write("📊 Pratinjau data hasil analisis:")
            st.dataframe(df.head(5))
            df.to_csv("data/uploaded_data.csv", index=False)
        else:
            st.error("❌ Kolom 'ulasan' tidak ditemukan dalam file.")
    except Exception as e:
        st.error(f"Terjadi error saat membaca file: {e}")
