import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from streamlit_lottie import st_lottie
import requests 
import numpy as np
import plotly.express as px





st.set_page_config(page_title='Keluhan Mahasiswa', page_icon=':mortar_board:', layout='wide')
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
def add_complaint(nama, nim, wa, tanggal, jenis_keluhan,judul, deskripsi_keluhan):
    time_sent = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")
    data = [nama, nim, wa, tanggal, jenis_keluhan, judul, deskripsi_keluhan, time_sent, "Keluhan Masuk",'', '', '']
    sheet.insert_row(data, index=2)



# Define function for updating the status of a complaint
def update_status(row, status):
    col = 9 if status == 'diterima' else 10
    sheet.update_cell(row, col, pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))


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

    st.title("Misal: Chat Gantari")
    st.title('Input Keluhan Mahasiswa')

    # Get input from user
    nama = st.text_input('Nama')
    nim = st.text_input('NIM')
    wa = st.text_input('No WA')
    tanggal = st.date_input('Tanggal')
    jenis_keluhan = st.selectbox('Jenis Keluhan', ['Akademik dan Non-Akademik', 'Sarana dan Prasana','Pelayanan','Finansial'])
    judul = st.text_input('Judul Keluhan')
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
        elif not judul:
            st.warning('Harap isi Judul Keluhan.')
        elif not deskripsi_keluhan:
            st.warning('Harap isi Deskripsi Keluhan.')
        else:
            add_complaint(nama, nim, wa, str(tanggal), jenis_keluhan, judul, deskripsi_keluhan)
            # 'update_complaint_status(sheet, sheet.row_count, "Keluhan Masuk")'
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

if choice == 'Akses Keluhan':
    # Mendefinisikan fungsi untuk menampilkan animasi Lottie
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

# Define a function to get the latest complaint data from the Google Sheet
    # Fungsi untuk mengupdate durasi penyelesaian keluhan di Google Spreadsheet
    def update_complaint_duration(sheet, row, durasi_penyelesaian):
        durasi_penyelesaian_jam = durasi_penyelesaian.seconds / 3600 # konversi durasi ke satuan jam
        sheet.update_cell(row, 11, str(round(durasi_penyelesaian_jam, 2))) # membulatkan hingga 2 desimal dan mengubah ke string

    def update_complaint_time(sheet, row, waktu_selesai):
    # Mengupdate waktu penyelesaian pada kolom "Waktu Penyelesaian"
        waktu_selesai_str = waktu_selesai.strftime('%Y-%m-%d %H:%M')
        sheet.update_cell(row,10, waktu_selesai_str)
    def update_complaint_status(sheet, row, status,email):
        # Mengupdate status pada kolom "Status"
        sheet.update_cell(row,9, status)
        # Mengupdate email pada kolom "Penerima Keluhan"
        sheet.update_cell(row, 12, email)
    def update_complaint_status_(sheet, row, status):
        # Mengupdate status pada kolom "Status"
        sheet.update_cell(row,9, status)
    # Fungsi untuk mendapatkan data keluhan terbaru
    def get_latest_complaint_data(sheet):
        data = sheet.get_all_records()[-1]
        return data
    
    # Define the SessionState class
    class SessionState:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def get(self, key, default=None):
            return self.__dict__.get(key, default)

        def __repr__(self):
            return str(self.__dict__)

    auth = {
        'Hilmy': '22092003',
        'KingBudiSatriaHalim': 'password2',
        'FarhanRamadhanAbdullah': 'password3',
        'JasmitaYasmin': 'password4',
        'RifaMahiraDrinaputeri': 'password5'
    }


    # Fungsi untuk menampilkan halaman login
    def show_login_page():
        st.title('Autentifikasi untuk Advocare')
        st.write('Silakan masukkan Username dan kata sandi Anda untuk mengakses keluhan:')
        email = st.text_input('Username')
        password = st.text_input('Kata Sandi', type='password')

        if st.button('Login'):
            if email in auth and auth[email] == password:
                # Set a flag to indicate that the user has logged in
                session = st.session_state
                session.logged_in = True
                st.session_state.email = email # tambahkan email ke dalam session state
                st.success('Login berhasil')
                show_complaint_page(sheet)
            else:
                st.error('Email atau kata sandi Anda salah. Silakan coba lagi.')
    
    def show_complaint_page(sheet):
                # Tampilkan daftar keluhan yang telah diterima
                st.header('Keluhan yang Telah Diterima')
                keluhan = sheet.get_all_records()
                df = pd.DataFrame(keluhan)
                # Menampilkan filter berdasarkan status, bulan, dan kategori keluhan
                # status_list = df['Status'].unique().tolist()
                status_list = ['Keluhan Masuk', 'Diproses', 'Selesai']
                selected_status = st.selectbox('Pilih Status Keluhan', status_list, key='box1')

                bulan_list = pd.DatetimeIndex(df['Waktu Pengiriman']).month_name().unique().tolist()
                selected_bulan = st.selectbox('Pilih Bulan', bulan_list, key='box2')

                # kategori_list = df['Kategori Keluhan'].unique().tolist()
                kategori_list = ['Akademik dan Non-Akademik', 'Sarana dan Prasana','Pelayanan','Finansial']
                selected_kategori = st.selectbox('Pilih Kategori Keluhan', kategori_list, key='box3')

                filtered_df = df[(df['Status'] == selected_status) & (pd.DatetimeIndex(df['Waktu Pengiriman']).month_name() == selected_bulan) & (df['Kategori Keluhan'] == selected_kategori)]

                st.write('### Jumlah Keluhan: ', len(filtered_df))

                for i, data in filtered_df.iterrows():
                    if data['Status'] == 'Keluhan Masuk':
                        st.markdown('-------------')
                        st.write('## Keluhan #{}'.format(i+1))
                        st.write('### Nama: ', data['Nama'])
                        st.write('### NIM: ', data['NIM'])
                        st.write('### Nomor WhatsApp: ', data['No WA'])
                        st.write('### Kategori Keluhan: ', data['Kategori Keluhan'])
                        st.write('### Judul Keluhan: ', data['Judul Keluhan'])
                        st.write('### Deskripsi Keluhan: ', data['Deskripsi Keluhan'])
                        st.write('### Waktu Pengiriman: ', data['Waktu Pengiriman'])
                        waktu_pengiriman = data['Waktu Pengiriman']
                      
                        
                        # Tambahkan tombol "Proses", "Tolak", dan "Selesai"
                        st.write('### Eksekusi Keluhan')
                        st.markdown('-------------')
                        if st.button('Proses'+ str(i)):
                            # Update status keluhan menjadi "Diproses" di Google Spreadsheet
                            row = data.name + 2
                            session = st.session_state
                            email = session.email
                            update_complaint_status(sheet, row, 'Diproses', email)      

                        if st.button('Tolak'+ str(i)):
                            # Hapus data keluhan dari Google Spreadsheet
                            row = data.name + 2
                            sheet.delete_row(row)
                            st.success('Keluhan telah ditolak.')
                        # Tampilkan data keluhan terbaru
                            data = get_latest_complaint_data(sheet)
                            st.write('### Data Keluhan Terbaru')
                            st.write('Nama Pelapor:', data['Nama'])
                            st.write('Kategori Keluhan:', data['Kategori Keluhan'])
                            st.write('### Judul Keluhan: ', data['Judul Keluhan'])
                            st.write('Isi Keluhan:', data['Deskripsi Keluhan'])
                            st.write('Waktu Pengiriman:', data['Waktu Pengiriman'])
                            st.write('Status Keluhan:', data['Status'])
                        
            
                    if data['Status'] == 'Diproses':
                        st.write('## Keluhan #{}'.format(i+1))
                        st.write('### Nama: ', data['Nama'])
                        st.write('### NIM: ', data['NIM'])
                        st.write('### Nomor WhatsApp: ', data['No WA'])
                        st.write('### Kategori Keluhan: ', data['Kategori Keluhan'])
                        st.write('### Judul Keluhan: ', data['Judul Keluhan'])
                        st.write('### Deskripsi Keluhan: ', data['Deskripsi Keluhan'])
                        st.write('### Waktu Pengiriman: ', data['Waktu Pengiriman'])
                        st.write('### Dieksekusi Oleh: ', data['Penerima Keluhan'])
                        waktu_pengiriman = data['Waktu Pengiriman']
                        
                        # Tambahkan tombol "Proses", "Tolak", dan "Selesai" 
                        if st.button('Selesai'+ str(i)):
                             # Update status keluhan menjadi "Selesai" dan hitung durasi penyelesaian di Google Spreadsheet
                            row = data.name + 2
                            waktu_selesai = datetime.datetime.now()
                            waktu_pengiriman_str = data['Waktu Pengiriman']
                            waktu_pengiriman = datetime.datetime.strptime(waktu_pengiriman_str, '%Y-%m-%d %H:%M')
                            durasi_penyelesaian = waktu_selesai - waktu_pengiriman
                            update_complaint_status_(sheet, row, "Selesai")
                            update_complaint_duration(sheet, row, durasi_penyelesaian)
                            update_complaint_time(sheet, row, waktu_selesai)
                            st.success('Keluhan telah diselesaikan')

                        # Tampilkan data keluhan terbaru
                            data = get_latest_complaint_data(sheet)
                            st.write('### Data Keluhan Terbaru')
                            st.write('Nama Pelapor:', data['Nama'])
                            st.write('Kategori Keluhan:', data['Kategori Keluhan'])
                            st.write('### Judul Keluhan: ', data['Judul Keluhan'])
                            st.write('Isi Keluhan:', data['Deskripsi Keluhan'])
                            st.write('Waktu Pengiriman:', data['Waktu Pengiriman'])
                            st.write('Status Keluhan:', data['Status'])
                            st.write('Durasi Penyelesaian:', durasi_penyelesaian)
              
   
   

    # Fungsi utama
    def main():
        # Check if the user is already logged in
        session = st.session_state
        if 'logged_in' not in session:
            session.logged_in = False
        if session.logged_in:
            st.write('Anda telah berhasil login')
            show_complaint_page(sheet)
        else:
            show_login_page()

        # Add a logout button
        if session.logged_in:
            if st.button('Logout'):
                # Reset the flag to indicate that the user has logged out
                session.logged_in = False
                st.write('Anda telah berhasil logout')

    if __name__ == '__main__':
        # Run the app
        main()


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
    
    def Complaint_Graph_For_Viewers():
        # Load data
       
        keluhan = sheet.get_all_records()
        data1 = pd.DataFrame(keluhan)
      

        # Hitung jumlah keluhan dengan status Diproses
        keluhan_diproses = len(data1[data1['Status'] == 'Diproses'])
        # Hitung jumlah keluhan dengan status Selesai
        keluhan_selesai = len(data1[data1['Status'] == 'Selesai'])
        # Hitung jumlah keluhan dengan status Keluhan Masuk
        keluhan_masuk = len(data1[data1['Status'] == 'Keluhan Masuk'])
        # Hitung total jumlah keluhan
        total_keluhan = keluhan_diproses + keluhan_masuk + keluhan_selesai 

        # Hitung jumlah keluhan finansial
        Finansial = len(data1[data1['Kategori Keluhan'] == 'Finansial'])
        # Hitung jumlah keluhan akademik
        Akademik = len(data1[data1['Kategori Keluhan'] == 'Akademik dan Non-Akademik'])
        # Hitung jumlah keluhan sarana
        Sarana = len(data1[data1['Kategori Keluhan'] == 'Sarana dan Prasana'])
        # Hitung jumlah keluhan pelayanan
        Pelayanan = len(data1[data1['Kategori Keluhan'] == 'Pelayanan'])
        st.title('Dashboard Program Pengaduan Keluhan KM PKU IPB')
        st.markdown('-------------')
        st.subheader('Metrik Total Keluhan')
        # st.markdown('''
        #     Grafik time series interaktif untuk menampilkan nilai performa Kabinet Gantari Arti.
        #     ''')

         # Tampilkan metrik dalam kolom
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Keluhan", total_keluhan)
        with col2:
            st.metric("Keluhan Diproses", keluhan_diproses)
        with col3:
            st.metric("Keluhan Selesai", keluhan_selesai)
        with col4:
            st.metric("Keluhan Masuk", keluhan_masuk)

        st.write("")  # Tambahkan spasi kosong

        # Tampilkan metrik dalam kolom
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Finansial", Finansial)
        with col2:
            st.metric("Akademik dan Non-Akademik", Akademik)
        with col3:
            st.metric("Sarana dan Prasana", Sarana)
        with col4:
            st.metric("Pelayanan", Pelayanan)

        data = pd.DataFrame(data1)
        # Ubah tipe data kolom tanggal menjadi datetime
        data["Tanggal"] = pd.to_datetime(data["Tanggal"])

        # Urutkan data berdasarkan tanggal
        data = data.sort_values("Tanggal")
        # Hitung jumlah keluhan tiap bulan
        keluhan_per_bulan = (
            data.groupby(pd.Grouper(key="Tanggal", freq="M"))
            .size()
            .reset_index(name="Jumlah Keluhan")
        )

        # # Tambahkan data bulan September dan seterusnya (Di Akhir)===========-=-=-=-=-=-=-=-=-=
        # for i in range(5, 13):
        #     if keluhan_per_bulan["Tanggal"].dt.month.isin([i]).any():
        #         continue
        #     keluhan_per_bulan = keluhan_per_bulan.append(
        #         {"Tanggal": pd.to_datetime(f"2023-{i}-01"), "Jumlah Keluhan": 0},
        #         ignore_index=True,
        #     )

        # Tampilkan grafik menggunakan Plotly Express
       
         # Tampilkan line chart
        st.subheader('Jumlah Keluhan Tiap Bulan')
        fig = px.line(keluhan_per_bulan, x="Tanggal", y="Jumlah Keluhan")
        st.title('Line Chart (Time Series) Frekuensi Keluhan Mahasiswa Tiap Bulan')
        st.markdown('''
            Grafik interaktif untuk menampilkan banyaknya Keluhan Mahasiswa di tiap bulannya
            ''')
                # Disable zooming
        fig.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )
        st.plotly_chart(fig)





        df = pd.DataFrame(data1)
        # Convert tanggal column to datetime type
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])

        # Extract year and month from tanggal column
        df['Year'] = df['Tanggal'].dt.year
        df['Month'] = df['Tanggal'].dt.month_name()

        # Group data by Year, Month, and Kategori keluhan
        df_grouped = df.groupby(['Year', 'Month', 'Kategori Keluhan']).size().reset_index(name='Jumlah')
        # Create list of months in order from March to October
        month_order = ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']

        # Sort the Month column based on month_order
        df_grouped['Month'] = pd.Categorical(df_grouped['Month'], categories=month_order, ordered=True)
        df_grouped = df_grouped.sort_values('Month')

        # Create stacked chart time series using plotly express
        fig = px.area(df_grouped, x='Month', y='Jumlah', color='Kategori Keluhan', line_group='Kategori Keluhan',
                    hover_name='Kategori Keluhan', title='Jumlah Keluhan Berdasarkan Kategori Keluhan Tiap Bulan')

        
        # Disable zooming
        fig.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

         # Tampilkan stacked chart
        st.subheader('Jumlah Keluhan Tiap Bulan Berdasarkan Kategori')
   
        st.title('Stacked Chart (Time Series) Frekuensi Kategori Keluhan Mahasiswa Tiap Bulan')
        st.markdown('''
            Grafik interaktif untuk menampilkan banyaknya Keluhan Mahasiswa berdasarkan Kategori Keluhan di tiap bulannya .
            ''')
        st.plotly_chart(fig)
      



















       
        st.markdown('-------------')
        # Konversi kolom Tanggal menjadi format tanggal
        data1 = pd.DataFrame(data1)
        # Drop kolom yang tidak diperlukan
        data1 = data1.drop(columns=['Waktu Penyelesaian', 'Durasi Penyelesaian (jam)','Penerima Keluhan', 'Bulan'])

        # Ubah tipe data kolom Tanggal menjadi datetime
        data1['Tanggal'] = pd.to_datetime(data1['Tanggal'], errors='coerce')

        # Menambahkan tanggal yang hilang dengan nilai 0
        date_range = pd.date_range(start=data1['Tanggal'].min(), end=data1['Tanggal'].max(), freq='D')
        date_range = pd.DataFrame(date_range, columns=['Tanggal'])
        data1 = pd.merge(data1, date_range, how='right', on='Tanggal')
        data1['Jumlah Keluhan'] = data1.groupby('Tanggal')['Status'].transform('count')

        # Buat pilihan sortir berdasarkan bulan
        sort_by_month = st.selectbox('Sortir berdasarkan bulan:', options=data1['Tanggal'].dt.month_name().unique())

        # Filter data berdasarkan bulan yang dipilih
        filtered_data = data1[data1['Tanggal'].dt.month_name() == sort_by_month]

        # Hitung jumlah keluhan per hari dan buat grafik menggunakan Plotly Express
        daily_counts = filtered_data.groupby('Tanggal')['Status'].count().reset_index(name='Jumlah Keluhan')
        fig = px.line(daily_counts, x='Tanggal', y='Jumlah Keluhan', title='Jumlah Keluhan per Hari')

       
        fig2 = px.histogram(filtered_data, x='Kategori Keluhan', title='Kategori Keluhan')

        # Tampilkan grafik status keluhan menggunakan Plotly Express
       
        fig3 = px.pie(filtered_data, values=filtered_data.index, names='Status', title='Status Keluhan')

        # Tampilkan grafik menggunakan Streamlit
        st.title('Line Chart (Time Series) Frekuensi Keluhan Mahasiswa Tiap Hari')
        st.markdown('''
            Grafik interaktif untuk menampilkan banyaknya Keluhan Mahasiswa di tiap harinya
            ''')
         # Disable zooming
        fig.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )


        st.plotly_chart(fig)
        st.title('Histogram Frekuensi Kategori Keluhan Mahasiswa')
        st.markdown('''
            Grafik interaktif untuk menampilkan banyaknya Keluhan Mahasiswa berdasarkan Kategori Keluhan di tiap bulannya.
            ''')
         # Disable zooming
        fig2.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

        st.plotly_chart(fig2)
        st.title('Pie Chart Frekuensi Status Keluhan Mahasiswa')
        st.markdown('''
             Grafik interaktif untuk menampilkan banyaknya Keluhan Mahasiswa berdasarkan status Keluhan di tiap bulannya
            ''')
         # Disable zooming
        fig3.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

        st.plotly_chart(fig3)
    

        # Preprocess data
        data1['Tanggal'] = pd.to_datetime(data1['Tanggal'], format='%Y-%m-%d')
        data1['Bulan'] = data1['Tanggal'].dt.strftime('%Y-%m')


    def Complaint_Graph():
        keluhan = sheet.get_all_records()
        data1 = pd.DataFrame(keluhan)
        data1['Durasi Penyelesaian (jam)'] = pd.to_numeric(data1['Durasi Penyelesaian (jam)'], errors='coerce')

        # Remove any rows containing NaN values
        data2 = data1.dropna(subset=['Durasi Penyelesaian (jam)'])

        # Calculate average resolution time
        avg_resolution_time =(data2['Durasi Penyelesaian (jam)'].mean())


        st.write("")  # Tambahkan spasi kosong

        col1, col2 = st.columns(2)
        with col1:
            st.write("")  # Tambahkan spasi kosong
        with col2:
            st.metric("Average resolution time (Hours)", f"{avg_resolution_time:.2f}")


            



    auth = {
        'Hilmy': '22092003',
        'KingBudiSatriaHalim': 'password2',
        'FarhanRamadhanAbdullah': 'password3',
        'JasmitaYasmin': 'password4',
        'RifaMahiraDrinaputeri': 'password5'
    }


    # Fungsi untuk menampilkan halaman login
    def show_login_page():
        Complaint_Graph_For_Viewers()
        st.title('Autentifikasi untuk Advocare')
        st.write('Silakan masukkan username dan kata sandi Anda untuk melihat Evaluasi Program Keluhan Mahasiswa secara Statistik:')
        email = st.text_input('Username')
        password = st.text_input('Kata Sandi', type='password')

        if st.button('Login'):
            if email in auth and auth[email] == password:
                # Set a flag to indicate that the user has logged in
                session = st.session_state
                session.logged_in = True
                st.session_state.email = email # tambahkan email ke dalam session state
                st.success('Login berhasil')
                


            else:
                st.error('Email atau kata sandi Anda salah. Silakan coba lagi.')
        # Fungsi utama

    def main():
        # Check if the user is already logged in
        session = st.session_state
        if 'logged_in' not in session:
            session.logged_in = False
        if session.logged_in:
            st.write('Anda telah berhasil login')
            Complaint_Graph()
            
        else:
            show_login_page()

        # Add a logout button
        if session.logged_in:
            if st.button('Logout'):
                # Reset the flag to indicate that the user has logged out
                session.logged_in = False
                st.write('Anda telah berhasil logout')

    if __name__ == '__main__':
        # Run the app
        main()
