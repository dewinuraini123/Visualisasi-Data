import streamlit as st
import matplotlib.pyplot as plt

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 250, 180]

# Judul aplikasi
st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')

#Identitas kelompok 
st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("""
Kelomppok 19 :
            -Dewi Nuraini-0110122122
            -Muhammad Daffa Shafwan-0110222275
            -Muhammad Saputra Adi Firmansyah-0110222105
""")

# Scatter Plot menggunakan Matplotlib
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='blue')
ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
ax.set_xlabel('Suhu (C)')
ax.set_ylabel('Penjualan Es Krim')

# Tampilkan di Streamlit
st.pyplot(fig)

# Kustomisasi scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='orange', s=100, edgecolors='black', alpha=0.7)
ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
ax.set_xlabel('Suhu (C)')
ax.set_ylabel('Penjualan Es Krim')
ax.grid(True)

# Tampilkan di Streamlit
st.pyplot(fig)

# Data Tambahan unutk Kategori Hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 90, 100, 110, 120, 140, 160]

# Multiple Scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Hari Kerja', s=80)
ax.set_title('Penjualan Es Krim Berdasarkan Hari')
ax.set_xlabel('Suhu (c)')
ax.set_ylabel('Penjualan Es Krim')
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)
