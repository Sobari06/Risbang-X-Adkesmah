import streamlit as st
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



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

smtp_server = "smtp.gmail.com"
smtp_port = 587
email_pengirim = "email@gmail.com"  # Masukkan email pengirim
password = "password"  # Masukkan password email pengirim
def kirim_notifikasi_email(penerima, subjek, isi_email):
    try:
        # Membuat objek pesan email
        msg = MIMEMultipart()
        msg['From'] = email_pengirim
        msg['To'] = penerima
        msg['Subject'] = subjek

        # Menambahkan isi pesan email
        body = isi_email
        msg.attach(MIMEText(body, 'plain'))

        # Mengirim email menggunakan SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_pengirim, password)
        text = msg.as_string()
        server.sendmail(email_pengirim, penerima, text)
        server.quit()

        print("Email notifikasi berhasil dikirim ke", penerima)
    except Exception as e:
        print("Error:", e) 
        
penerima = "email_penerima@example.com"
subjek = "Notifikasi keluhan diterima"
isi_email = "Dear pengguna, keluhan Anda sudah kami terima dan akan segera ditindaklanjuti."
kirim_notifikasi_email(penerima, subjek, isi_email)

