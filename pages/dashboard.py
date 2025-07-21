import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from wordcloud import WordCloud
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

st.set_page_config(page_title="Hasil Analisis Sentimen", layout="wide")
st.markdown('<div class="title">Hasil Analisis Sentimen Pengunjung Hotel</div>', unsafe_allow_html=True)
st.markdown("""
    <hr style="
        border: none;
        height: 4px; /* tebal garis */
        background-color: black; /* warna garis */
        margin-top: -10px;
        margin-bottom: 20px;
    ">
""", unsafe_allow_html=True)

try:
    df = pd.read_csv("data/uploaded_data.csv")

    # Hitung distribusi sentimen
    distribusi = df['sentimen'].value_counts()
    total = len(df)
    positif = distribusi.get('Positif', 0)
    netral = distribusi.get('Netral', 0)
    negatif = distribusi.get('Negatif', 0)

    # CSS dan box tampil horizontal
    st.markdown("""
        <style>
        .card {
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 10px;
            text-align: center;
            margin-bottom: 10px;
            font-family: 'Poppins', sans-serif;
        }
        .total { background-color: #BCCCDC; }
        .positif { background-color: #a3f7b5; }
        .netral { background-color: #add8ff; }
        .negatif { background-color: #ffb3b3; }
        .judul { 
                background-color: #BCCCDC;
                font-size: 20px; 
                font-weight: bold;}
        .value {
            font-size: 36px;
            font-weight: bold;
            margin-top: -10px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(f"""
            <div class='card total'>
                <div>Total Ulasan</div>
                <div class='value'>{total}</div>
            </div>
            <div class='card positif'>
                <div>Positif</div>
                <div class='value'>{positif}</div>
            </div>
            <div class='card netral'>
                <div>Netral</div>
                <div class='value'>{netral}</div>
            </div>
            <div class='card negatif'>
                <div>Negatif</div>
                <div class='value'>{negatif}</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class='card judul'>
                <div>Distribusi Sentimen</div>
            </div>
        """, unsafe_allow_html=True)
        distribusi = distribusi.reindex(['Positif', 'Netral', 'Negatif'])
        colors = {
            'Positif': "#43df64",
            'Netral': "#4492db",
            'Negatif': "#c94f4f"
        }
        labels = distribusi.index.tolist()
        color_list = [colors.get(k, "#cccccc") for k in labels]

        fig, ax = plt.subplots(figsize=(4, 4))
        wedges, texts, autotexts = ax.pie(
            distribusi.values,
            labels=labels,
            autopct='%1.0f %%',
            startangle=90,
            colors=color_list,
            textprops={'fontsize': 14}
        )
        for text in texts:
            text.set_fontsize(10)  

        for autotext in autotexts:
            autotext.set_fontsize(14)
        ax.axis('equal')
        st.pyplot(fig)
    

    # WORDCLOUD
    factory = StopWordRemoverFactory()
    stopword_remover = factory.create_stop_word_remover()

    st.markdown(f"""
            <div class='card judul'>
                <div>Wordcloud</div>
            </div>
        """, unsafe_allow_html=True)

    for label in ["Positif", "Netral", "Negatif"]:
        bg_color = colors.get(label, "#cccccc")
        st.markdown(f"<h4 style='text-align: center; color: {bg_color};'>{label}</h4>", unsafe_allow_html=True)

        ulasan_list = df[df['sentimen'] == label]['ulasan'].dropna().astype(str).tolist()
        teks_bersih = " ".join([stopword_remover.remove(u) for u in ulasan_list])

        if teks_bersih.strip():
            wc = WordCloud(
                width=800,
                height=250,
                background_color='#F8FAFC',
                colormap='Greens' if label == 'Positif' else 'Blues' if label == 'Netral' else 'Reds',
                max_words=100
            ).generate(teks_bersih)

            fig, ax = plt.subplots(figsize=(8, 3))
            ax.imshow(wc, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.info(f"Tidak ada data ulasan untuk label {label}.")


    st.markdown(f"""
            <div class='card judul'>
                <div>Data Hasil Analisis Sentimen</div>
            </div>
        """, unsafe_allow_html=True)
    st.dataframe(df)

except FileNotFoundError: 
    st.warning("⚠️ Belum ada data yang diunggah dan dianalisis.")
