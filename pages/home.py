import streamlit as st
import base64

st.set_page_config(page_title="Home", layout="wide")

st.markdown('<div class="title">Home</div>', unsafe_allow_html=True)
st.markdown("""
    <hr style="
        border: none;
        height: 4px; 
        background-color: black; 
        margin-top: -10px;
        margin-bottom: 20px;
    ">
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='font-family:Arial; color:#333;'>SELAMAT DATANG!</h3>

<span style='font-size:15px;'>Ini adalah</span></p> <p><strong style='font-size:16px;'>Sistem Analisis Sentimen Pengunjung Hotel Bahasa Indonesia</strong><br> <span style='font-size:15px;'>yang dikembangkan sebagai bagian dari penelitian tugas akhir yang bertujuan untuk mengidentifikasi dan mengklasifikasikan opini pengunjung hotel berdasarkan ulasan teks dari berbagai platform digital.</span></p>            

<span style='font-size:15px;'>Sistem ini menggunakan algoritma Long Short-Term Memory (LSTM), sebuah metode deep learning yang efektif dalam memproses data urutan (sequential data) seperti teks. 
            Model dilatih menggunakan 8.829 data ulasan berbahasa Indonesia yang telah melalui tahap pre-processing.
            Model memiliki akurasi validasi sebesar 86.19% dan akurasi data uji sebesar 86.79% </span></p>            
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='font-family:Arial; color:#333;'>Fitur Utama</h3>

<p><strong style='font-size:16px;'>1. Analisis Sentimen Teks</strong><br>
<span style='font-size:14px;'>Melakukan analisis terhadap ulasan secara manual (input teks) atau masif (upload file CSV). Untuk analisis secara manual (input teks), sistem hanya menampilkan hasil analisis saja.</span></p>

<p><strong style='font-size:16px;'>2. Visualisasi Hasil Analisis</strong><br>
<span style='font-size:14px;'>Menampilkan hasil analisis dalam bentuk grafik distribusi sentimen dan word cloud untuk masing-masing sentimen. Data yang divisualisasikan adalah data hasil ulasan dari dokumen CSV yang diunggah sebelumnya.</span></p>

<p><strong style='font-size:16px;'>3. Rekapitulasi Data Ulasan</strong><br>
<span style='font-size:14px;'>Menyajikan data hasil ulasan dengan label sentimen.</span></p>
""", unsafe_allow_html=True)
