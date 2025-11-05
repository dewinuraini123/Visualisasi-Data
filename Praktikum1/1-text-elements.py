# import library yang dibutuhkan
import streamlit as st

# text element
st.header("Ini header") # header - untuk membuat tulisan header
st.subheader("Ini sub header") # untuk membuat subjudul yang lebih kecil
st.text("Ini teks biasa tanpa format") # unutk membuat teks polos tanpa format
st.markdown("**ini teks bold** dan *ini teks italic*") # markdown untuk memformat teks tebal/miring
st.markdown("""
- ini baris 1
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan markdown multibaris
""")
st.caption("ini caption") # teks kecil dibawah elemen (untuk penjelasan)
st.title("Ini Judul")

#coba mandiri
#tuliskan:
#1. Judul Praktikum pakai title()
st.title("Bagian 1 Praktikum Visualisasi Data")
#2. bagian praktikum pakai subheader()
st.subheader("Berikut ini merupakan anggota kelompok 19")
#3. nama lengkap anggota - nim pakai markdown multibaris """
st.markdown("""
1. Dewi Nuraini - 0110122122
2. Muhammad Saputra Adi Firmansyah - 0110222105
3. Muhammad Daffa Shafwan - 0110222275
""")

# Bagian 2: Menampilkan Rumus (LaTex)
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumus kuadrat binominal

# Bagian 3: Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("python Code")

# simpan ke variable
code = '''
def hello():
    print("Hello, streamlit!)
'''

# st.code() menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language="python")

st.subheader("Java Code")
st.code("""
    public class GFG {
        public static void main (String arg[]) {
            System.out.printIn("Hello World!);
        }
}
""", language='java')
#fungsi st.code() bisa digunakan untuk bahasa pemrograman lain sperti java, javascript, c++, html, dll

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome guest!); // kesalahan ketik (addalaert) sengaja  dibuat untuk menimbulkan error
}
catch(err) {
        document.getElementById("demo").innerHTML = err.message; //
        menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language='javascript')
# Kode ini menunjukkan contoh bagaimana menangani error (exception) di JavaScript
# Hasilnya tidak dijalankan di Streamlit, tapi ditampilkan sebagai contoh kode.