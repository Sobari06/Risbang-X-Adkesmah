import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from streamlit_lottie import st_lottie
import requests 
# Google Sheets authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('united-option-379311-32c22a337d18.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets file
sheet = client.open('Keluhan Mahasiswa').sheet1
sheet1 = client.open('KepuasanUser').sheet1
#data = sheet.get_all_records()
# Define the sidebar menu options
menu = ['Halaman Utama', 'Identitas Penerima Keluhan', 'Survei Kepuasan', 'Frequently Asked Questions', 'Akses Keluhan', 'Complaint Analytics']
choice = st.sidebar.selectbox('Menu', menu)

# Define function for adding complaint to the Google Sheets file
def add_complaint(nama, nim, wa, tanggal, jenis_keluhan, deskripsi_keluhan):
    time_sent = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [nama, nim, wa, tanggal, jenis_keluhan, deskripsi_keluhan, time_sent, '', '', '']
    sheet.insert_row(data, index=2)

# Define function for updating the status of a complaint
def update_status(row, status):
    col = 9 if status == 'diterima' else 10
    sheet.update_cell(row, col, pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))

# Define function for getting the complaint data from the Google Sheets file
def get_complaints():
    data = sheet.get_all_values()[1:]
    df = pd.DataFrame(data, columns=['Nama', 'NIM', 'No WA', 'Tanggal', 'Jenis Keluhan', 'Deskripsi Keluhan', 'Waktu Pengiriman', 'Diterima', 'Ditolak', 'Selesai'])
    df['Waktu Pengiriman'] = pd.to_datetime(df['Waktu Pengiriman'])
    df['Diterima'] = pd.to_datetime(df['Diterima'], errors='coerce')
    df['Ditolak'] = pd.to_datetime(df['Ditolak'], errors='coerce')
    df['Selesai'] = pd.to_datetime(df['Selesai'], errors='coerce')
    return df

if choice == 'Halaman Utama':
     #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets8.lottiefiles.com/packages/lf20_km5er2un.json"

    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    st.title("Chat Gantari")
    st.title('Input Keluhan Mahasiswa')

    # Get input from user
    nama = st.text_input('Nama')
    nim = st.text_input('NIM')
    wa = st.text_input('No WA')
    tanggal = st.date_input('Tanggal')
    jenis_keluhan = st.selectbox('Jenis Keluhan', ['Akademik', 'Non-Akademik'])
    deskripsi_keluhan = st.text_area('Deskripsi Keluhan')

    # Add complaint to Google Sheets file
    # Add complaint to Google Sheets file
    if st.button('Kirim Keluhan'):
        if not nama:
            st.warning('Harap isi Nama.')
        elif not nim:
            st.warning('Harap isi NIM.')
        elif not wa:
            st.warning('Harap isi No WA.')
        elif not jenis_keluhan:
            st.warning('Harap pilih Jenis Keluhan.')
        elif not deskripsi_keluhan:
            st.warning('Harap isi Deskripsi Keluhan.')
        else:
            add_complaint(nama, nim, wa, str(tanggal), jenis_keluhan, deskripsi_keluhan)
            st.success('Keluhan berhasil dikirim.')

  
if choice == 'Identitas Penerima Keluhan':
    #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets3.lottiefiles.com/packages/lf20_KU3FGB47d6.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    st.title('Identitas Penerima Keluhan')

    st.write('1. Nama Penerima Keluhan')
    st.write('2. NIM Penerima')

# Survei Kepuasan
if choice == 'Survei Kepuasan':
        #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    def add_survei(name, nim, date, satisfaction, response_time, resolution, friendliness, handling, effectiveness, communication, appreciation, recommendation, feedback):
        data = [name, nim, date, satisfaction, response_time, resolution, friendliness, handling, effectiveness, communication, appreciation, recommendation, feedback]
        sheet1.insert_row(data, index=2)
    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets7.lottiefiles.com/private_files/lf30_VeGYYQ.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))
    st.title('Survei Kepuasan')
    st.write('Silahkan mengisi survei kepuasan berikut ini:')
    name = st.text_input('Nama:')
    nim = st.text_input('NIM:')
    date = st.date_input('Tanggal:', datetime.date.today())
    date_str = date.strftime('%Y-%m-%d') # ubah tipe data date menjadi string
    st.write('P1. Apakah Anda puas dengan layanan yang diberikan?')
    satisfaction = st.slider('', 1, 10, 5, key='slider1')
    st.write('P2. Apakah respon terhadap keluhan Anda cepat?')
    response_time = st.slider('', 1, 10, 5, key='slider2')
    st.write('P3. Apakah penyelesaian keluhan Anda memuaskan?')
    resolution = st.slider('', 1, 10, 5, key='slider3')
    st.write('P4. Apakah petugas yang menangani keluhan Anda ramah?')
    friendliness = st.slider('', 1, 10, 5, key='slider4')
    st.write('P5. Apakah keluhan Anda ditangani dengan baik?')
    handling = st.slider('', 1, 10, 5, key='slider5')
    st.write('P6. Apakah solusi yang diberikan efektif?')
    effectiveness = st.slider('', 1, 10, 5, key='slider6')
    st.write('P7. Apakah ada komunikasi yang baik antara petugas dan Anda?')
    communication = st.slider('', 1, 10, 5, key='slider7')
    st.write('P8. Apakah Anda merasa dihargai sebagai pelanggan?')
    appreciation = st.slider('', 1, 10, 5, key='slider8')
    st.write('P9. Apakah Anda akan merekomendasikan layanan ini ke orang lain?')
    recommendation = st.slider('', 1, 10, 5, key='slider9')
    st.write('P10. Apakah ada hal yang ingin Anda sampaikan terkait layanan ini?')
    feedback = st.text_input('', '')

    # Save survey data to Google Sheets
    # Add complaint to Google Sheets file
    if st.button('Kirim Hasil Survei'):
        if not name:
            st.warning('Harap isi Nama.')
        elif not nim:
            st.warning('Harap isi NIM.')
        elif not date:
            st.warning('Harap isi No WA.')
        elif not satisfaction:
            st.warning('Harap isi P1.')
        elif not response_time:
            st.warning('Harap isi P2.')
        elif not resolution:
            st.warning('Harap isi P3.')
        elif not friendliness:
            st.warning('Harap isi P4.')
        elif not handling:
            st.warning('Harap isi P5.')
        elif not effectiveness:
            st.warning('Harap isi P6.')
        elif not communication:
            st.warning('Harap isi P7.')
        elif not appreciation:
            st.warning('Harap isi P8.')
        elif not recommendation:
            st.warning('Harap isi P9.')
        elif not feedback:
            st.warning('Harap isi P10.')
        else:
            add_survei(name, nim, str(date), satisfaction, response_time, resolution, friendliness, handling, effectiveness, communication, appreciation, recommendation, feedback)
            st.success('Data survei telah disimpan')
  
   

if choice == 'Frequently Asked Questions':
    #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets3.lottiefiles.com/packages/lf20_D7l6QPTtOL.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    st.title('Frequently Asked Questions')
    st.write('Berikut adalah beberapa pertanyaan dan jawaban yang sering ditanyakan:')
    st.write('1. Bagaimana cara melihat status keluhan saya?')
    st.write('Anda dapat melihat status keluhan Anda di menu "Akses Keluhan" setelah melakukan autentifikasi.')
    st.write('2. Berapa lama waktu yang diperlukan untuk menanggapi keluhan?')
    st.write('Kami berusaha menanggapi setiap keluhan dalam waktu 24 jam.')
    st.write('3. Apa yang harus saya lakukan jika keluhan saya tidak direspon?')
    st.write('Silakan hubungi kami melalui email atau nomor telepon yang tertera di situs kami.')
    st.write('4. Apakah saya dapat memberikan feedback tentang pelayanan yang diberikan?')
    st.write('Tentu saja! Anda dapat memberikan feedback melalui menu "Survei Kepuasan" di situs kami.')
# if choice == 'Akses Keluhan':
#     #Mendefinisikan fungsi untuk menampilkan animasi Lottie
#     def load_lottie_url(url: str):
#         r = requests.get(url)
#         if r.status_code != 200:
#             return None
#         return r.json()

#     # Mendefinisikan URL animasi Lottie yang akan ditampilkan
#     url = "https://assets1.lottiefiles.com/packages/lf20_huqty7bz.json"
#     # Menampilkan animasi Lottie di tampilan utama Streamlit
#     st_lottie(load_lottie_url(url))

#     st.title('Autentifikasi')
#     st.write('Silakan masukkan email dan kata sandi Anda untuk mengakses keluhan:')
#     email = st.text_input('Email')
#     password = st.text_input('Kata Sandi', type='password')
#     if st.button('Login'):
#         if email == 'admin' and password == '12345':
#             st.success('Login berhasil')
#             st.write('Berikut adalah daftar keluhan yang belum ditanggapi:')
#             # Display the list of pending complaints from the database
#             query = 'SELECT * FROM complaints WHERE status = "diterima" ORDER BY timestamp DESC'
#             results = db.execute(query)
#             for row in results:
#                 st.write(row)
#         else:
#             st.error('Email atau kata sandi Anda salah. Silakan coba lagi.')

if choice == 'Akses Keluhan':
    #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets1.lottiefiles.com/packages/lf20_huqty7bz.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

    # Fungsi untuk mengakses Google Spreadsheet
    def access_spreadsheet():
        scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('united-option-379311-32c22a337d18.json', scope)
        client = gspread.authorize(creds)
        sheet= client.open('Keluhan Mahasiswa').sheet1 # ganti nama_spreadsheet dengan nama spreadsheet yang digunakan
        return sheet

    # Fungsi untuk mengubah status keluhan
    def update_complaint_status(sheet, row, status):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.update_cell(row, 4, status)
        sheet.update_cell(row, 5, now)

    # Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()



    st.title('Autentifikasi')
    st.write('Silakan masukkan email dan kata sandi Anda untuk mengakses keluhan:')
    email = st.text_input('Email')
    password = st.text_input('Kata Sandi', type='password')
    if st.button('Login'):
        if email == 'admin' and password == '12345':
            st.success('Login berhasil')
            sheet = access_spreadsheet()
            complaints = sheet.get_all_records()
            pending_complaints = [c for c in complaints if c['Status'] == 'diterima']
            if len(pending_complaints) == 0:
                st.write('Tidak ada keluhan yang belum ditanggapi.')
            else:
                st.write('Berikut adalah daftar keluhan yang belum ditanggapi:')
                for i, c in enumerate(pending_complaints):
                    st.write(f"{i+1}. {c['Keluhan']}")
                    if st.button(f"Tanggapi Keluhan {i+1}"):
                        status = st.selectbox('Status', ['Diterima/Sedang Diproses', 'Ditolak', 'Selesai'])
                        update_complaint_status(sheet, c['ID'], status)
                        st.success('Status keluhan telah diperbarui.')
        else:
            st.error('Email atau kata sandi Anda salah. Silakan coba lagi.')

if choice == 'Complaint Analytics':
    #Mendefinisikan fungsi untuk menampilkan animasi Lottie
    def load_lottie_url(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Mendefinisikan URL animasi Lottie yang akan ditampilkan
    url = "https://assets9.lottiefiles.com/packages/lf20_5tl1xxnz.json"
    # Menampilkan animasi Lottie di tampilan utama Streamlit
    st_lottie(load_lottie_url(url))

