import streamlit as st
import pandas as pd

st.title("Program Komplain Masyarakat")

# Menambahkan form input untuk informasi keluhan
st.subheader("Formulir Keluhan")
nama = st.text_input("Nama")
alamat = st.text_input("Alamat")
nomor_telepon = st.text_input("Nomor Telepon")
jenis_keluhan = st.selectbox("Jenis Keluhan", ["Pelayanan Publik", "Lingkungan Hidup", "Kesehatan", "Pendidikan", "Keamanan"])
deskripsi_keluhan = st.text_area("Deskripsi Keluhan")

# Menambahkan tombol submit untuk mengirimkan keluhan
submit_button = st.button("Kirim Keluhan")

# Membuat dataframe untuk menyimpan data keluhan
df = pd.DataFrame(columns=["Nama", "Alamat", "Nomor Telepon", "Jenis Keluhan", "Deskripsi Keluhan"])

# Jika tombol submit ditekan, tambahkan data keluhan ke dataframe
if submit_button:
    df = df.append({"Nama": nama, "Alamat": alamat, "Nomor Telepon": nomor_telepon, "Jenis Keluhan": jenis_keluhan, "Deskripsi Keluhan": deskripsi_keluhan}, ignore_index=True)
    st.success("Keluhan Anda telah berhasil dikirim.")

    # Mengirim notifikasi otomatis ke fakultas/instansi terkait
    if jenis_keluhan == "Pelayanan Publik":
        st.write("Notifikasi telah dikirim ke Fakultas/Instansi terkait: Fakultas/Instansi Pelayanan Publik")
    elif jenis_keluhan == "Lingkungan Hidup":
        st.write("Notifikasi telah dikirim ke Fakultas/Instansi terkait: Fakultas/Instansi Lingkungan Hidup")
    elif jenis_keluhan == "Kesehatan":
        st.write("Notifikasi telah dikirim ke Fakultas/Instansi terkait: Fakultas/Instansi Kesehatan")
    elif jenis_keluhan == "Pendidikan":
        st.write("Notifikasi telah dikirim ke Fakultas/Instansi terkait: Fakultas/Instansi Pendidikan")
    elif jenis_keluhan == "Keamanan":
        st.write("Notifikasi telah dikirim ke Fakultas/Instansi terkait: Fakultas/Instansi Keamanan")

# Menampilkan daftar keluhan yang telah dikirim
st.subheader("Daftar Keluhan")
st.write(df)
