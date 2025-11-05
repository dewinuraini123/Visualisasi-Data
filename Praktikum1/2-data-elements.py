# import library
import streamlit as st
import pandas as pd            # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np             # untuk membuat data numerik acak
import altair as alt           # untuk membuat chart interaktif

# menampilkan judul dan deskripsi
st. title("Praktikum 1 - Visualisasi Data")                 # Menampilkan judul utama di halaman
st.caption("Bagian 2: Data Elements")                       # Menampilkan keterangan bagian

# st.markdown digunakan untuk menampilkan teks dengan format markdown (bullet list, bold, italic, dll)
st.markdown("""
1. Dewi Nuraini - 0110122122
2. Muhammad Saputra Adi Firmansyah - 0110222105
3. Muhammad Daffa Shafwan - 0110222275
""")

# DataFrame : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# menampilkan dataframe
st.dataframe(df)

# highlight nilai minimun
st.subheader("Highlight Minimun Value di DataFrame")

# highlight nilai terkecil di setiap kolom dataframe
#axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

# tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# menampilkan tabel statis
st.table(df)

# Matrics: komponen tampilan angka penting
st.subheader("Matrics")
st.metric(label="Temperature", value="31 C", delta="1.2 C") #kenaikan 1.2 C

# Metrics sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubahan:
# - "normal" (default): naik --> hijau, turun --> merah
# - "Inverse": kebalikannya (naik --> merah)
# - "off": tidak menampilkan warna perubahan

# definisikan variabel metrics
col1, col2, col3 =  st.columns(3)

# menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",
delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10,
delta_color="off") # netral (tidak baik, tidak buruk)

#menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) # kosong naik
st.metric("Trees", "91456", "-1132649") # penurunan

# The write() Function as a Superfunction

