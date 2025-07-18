import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64

st.markdown("""
    <style>
    body {
        background-color: #FFFFFF;
        color: #222;
    }
    .stButton>button {
        background-color: #FFFCFB;
        color: #093FB4;
    }
    .stSidebar {
        background-color: #D6EAF8;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- PAGE SETUP ---
home_page = st.Page(
    "pages/home.py",
    title=" Home",
    icon=":material/home:",
    default=True,
)
analisis_page = st.Page(
    "pages/analisis_sentimen.py",
    title=" Analisis Sentimen",
    icon=":material/query_stats:",
)
dashboard_page = st.Page(
    "pages/dashboard.py",
    title=" Hasil Analisis Sentimen",
    icon=":material/bar_chart:",
)

# --- NAVIGATION SETUP ---

pg = st.navigation(pages=[home_page, analisis_page, dashboard_page])


# --- RUN SETUP ---
pg.run()

# --- FOOTER SETUP ---
st.sidebar.markdown(
    """
    <style>
    .sidebar-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 14rem; /* default lebar sidebar Streamlit */
        padding: 10px;
        text-align: center;
        font-size: 12px;
        color: gray;
    }
    @media screen and (max-width: 768px) {
        .sidebar-footer {
            display: none; /* Sembunyikan di mobile */
        }
    }
    </style>

    <div class="sidebar-footer">
        © 2025<br>Dikembangkan oleh <b>Anita</b>
    </div>
    """,
    unsafe_allow_html=True
)