import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from streamlit_lottie import st_lottie
import requests 
import numpy as np
import plotly.express as px






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
    time_sent = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")
    data = [nama, nim, wa, tanggal, jenis_keluhan, deskripsi_keluhan, time_sent, "Keluhan Masuk",'', '', '']
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

    st.title("Dashboard Pengaduan KM PKU IPB")
    st.title('Input Keluhan Mahasiswa')

    # Get input from user
    nama = st.text_input('Nama')
    nim = st.text_input('NIM')
    wa = st.text_input('No WA')
    tanggal = st.date_input('Tanggal')
    jenis_keluhan = st.selectbox('Jenis Keluhan', ['Akademik dan Non-Akademik', 'Sarana dan Prasana','Pelayanan','Finansial'])
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
        sheet.update_cell(row, 10, str(round(durasi_penyelesaian_jam, 2))) # membulatkan hingga 2 desimal dan mengubah ke string

    def update_complaint_time(sheet, row, waktu_selesai):
    # Mengupdate waktu penyelesaian pada kolom "Waktu Penyelesaian"
        waktu_selesai_str = waktu_selesai.strftime('%Y-%m-%d %H:%M')
        sheet.update_cell(row,9, waktu_selesai_str)
    def update_complaint_status(sheet, row, status,email):
        # Mengupdate status pada kolom "Status"
        sheet.update_cell(row,8, status)
        # Mengupdate email pada kolom "Penerima Keluhan"
        sheet.update_cell(row, 11, email)
    def update_complaint_status_(sheet, row, status):
        # Mengupdate status pada kolom "Status"
        sheet.update_cell(row,8, status)
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
        st.write('Silakan masukkan email dan kata sandi Anda untuk mengakses keluhan:')
        email = st.text_input('Email')
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
                        st.write('## Keluhan #{}'.format(i+1))
                        st.write('### Nama: ', data['Nama'])
                        st.write('### NIM: ', data['NIM'])
                        st.write('### Nomor WhatsApp: ', data['No WA'])
                        st.write('### Kategori Keluhan: ', data['Kategori Keluhan'])
                        st.write('### Deskripsi Keluhan: ', data['Deskripsi Keluhan'])
                        st.write('### Waktu Pengiriman: ', data['Waktu Pengiriman'])
                        waktu_pengiriman = data['Waktu Pengiriman']
                        
                        # Tambahkan tombol "Proses", "Tolak", dan "Selesai"
                        st.write('### Eksekusi Keluhan')
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
                            st.write('Isi Keluhan:', data['Deskripsi Keluhan'])
                            st.write('Waktu Pengiriman:', data['Waktu Pengiriman'])
                            st.write('Status Keluhan:', data['Status'])
            
                    if data['Status'] == 'Diproses':
                        st.write('## Keluhan #{}'.format(i+1))
                        st.write('### Nama: ', data['Nama'])
                        st.write('### NIM: ', data['NIM'])
                        st.write('### Nomor WhatsApp: ', data['No WA'])
                        st.write('### Kategori Keluhan: ', data['Kategori Keluhan'])
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
                            st.write('Isi Keluhan:', data['Deskripsi Keluhan'])
                            st.write('Waktu Pengiriman:', data['Waktu Pengiriman'])
                            st.write('Status Keluhan:', data['Status'])
                            st.write('Durasi Penyelesaian:', durasi_penyelesaian)
                else:
                    st.warning('Silakan pilih kategori keluhan') 
    import streamlit as st

   

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
    def Complaint_Graph():
        # Load data
        #https://docs.google.com/spreadsheets/d/1kYAFrH0Ge5XxMmNkYKSSbysK2QXOe5cDPu9Y-u1GlXg/edit#gid=0
        sheet_id1 = '1kYAFrH0Ge5XxMmNkYKSSbysK2QXOe5cDPu9Y-u1GlXg'
        data= pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id1}/export?format=csv')
       

        # def keluhan_per_bulan(df):
        # # Membuat kolom baru berdasarkan bulan keluhan dibuat
        #     df['bulan'] = pd.to_datetime(df['Tanggal']).dt.strftime('%Y-%m')

        #     # Menghitung jumlah keluhan berdasarkan jenis keluhan dan bulan
        #     keluhan_jenis = df.groupby(['Kategori Keluhan', 'bulan']).size().reset_index(name='jumlah_keluhan')

        #     # Menghitung jumlah keluhan berdasarkan bulan
        #     keluhan_bulan = df.groupby('bulan').size().reset_index(name='jumlah_keluhan')

        #     return keluhan_jenis, keluhan_bulan



        #     # Membuat kolom baru berdasarkan bulan keluhan dibuat
        #     df['bulan'] = pd.to_datetime(df['Tanggal']).dt.strftime('%Y-%m')

        #     # Menghitung jumlah keluhan berdasarkan jenis keluhan dan bulan
        #     keluhan_jenis = df.groupby(['Kategori Keluhan', 'bulan']).size().reset_index(name='jumlah_keluhan')

        #     # Menghitung jumlah keluhan berdasarkan bulan
        #     keluhan_bulan = df.groupby('bulan').size().reset_index(name='jumlah_keluhan')

        #     return keluhan_jenis, keluhan_bulan
        # def keluhan_selesai(df):
        #     # Membuat kolom baru berdasarkan bulan keluhan diselesaikan
        #     df['bulan'] = pd.to_datetime(df['Tanggal']).dt.strftime('%Y-%m')

        #     # Menghitung jumlah keluhan yang diselesaikan dan diproses berdasarkan bulan
        #     keluhan_selesai = df.groupby('bulan')['keluhan_selesai'].agg(['sum', 'count']).reset_index()
        #     keluhan_selesai.columns = ['bulan', 'jumlah_selesai', 'jumlah_diproses']

        #     return keluhan_selesai
        
        # def total_keluhan(df):
        #     return df.shape[0]

        # # Tampilkan data keluhan
        # st.write('## Data Keluhan')
        # st.dataframe(df)

        # # Tampilkan grafik jumlah keluhan dan keluhan jenis berdasarkan bulan
        # keluhan_jenis, keluhan_bulan = keluhan_per_bulan(df)
        # st.write('## Grafik Jumlah Keluhan dan Jenis Keluhan per Bulan')
        # st.bar_chart(keluhan_bulan.set_index('bulan'))
        # st.bar_chart(keluhan_jenis.set_index(['bulan', 'Kategori Keluhan']))

        # # Tampilkan grafik jumlah keluhan yang diselesaikan dan diproses berdasarkan bulan
        # keluhan_selesai = keluhan_selesai(df)
        # st.write('## Grafik Jumlah Keluhan yang Diselesaikan dan Diproses per Bulan')
        # st.bar_chart(keluhan_selesai.set_index('bulan'))
        # # Tampilkan metrik total jumlah keluhan
        # total = total_keluhan(df)
        # st.write(f'## Total Keluhan: {total}')

        # Load satisfaction data
        #https://docs.google.com/spreadsheets/d/154rG3WMobkWhHP4f6GjBFZLyJbxa7pw3RN3j2tESemc/edit#gid=0
    #     sheet_id2 = '154rG3WMobkWhHP4f6GjBFZLyJbxa7pw3RN3j2tESemc'
    #     df1 = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv')
    #     # Replace non-numeric values with NaN
        data['Durasi Penyelesaian (jam)'] = pd.to_numeric(data['Durasi Penyelesaian (jam)'], errors='coerce')

        # Remove any rows containing NaN values
        data = data.dropna(subset=['Durasi Penyelesaian (jam)'])

        # Convert the column to float data type
        data['Durasi Penyelesaian (jam)'] = data['Durasi Penyelesaian (jam)'].astype(float)

        # Calculate average resolution time
        avg_resolution_time = int(data['Durasi Penyelesaian (jam)'].mean())
        # Create metric
        st.metric(label="Average resolution time", value=format(avg_resolution_time, '.2f'))
       # membaca data frame dari Google Sheet

    #     # create bar plot using plotly
    #     fig = px.bar(df1, x='Tanggal', y=['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation'], barmode='group')

    #     # display bar plot using Streamlit
    #     st.plotly_chart(fig)


        # membaca data frame dari Google Sheet
        sheet_id2 = '154rG3WMobkWhHP4f6GjBFZLyJbxa7pw3RN3j2tESemc'
        df1 = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv')

        # # Menambahkan kolom bulan pada data frame
        # df1['Bulan'] = pd.to_datetime(df1['Tanggal']).dt.strftime('%B')

        # # Mengelompokkan nilai berdasarkan bulan dan menghitung rata-rata dari setiap kolom
        # avg_metrics = df1.groupby('Bulan')[['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation']].mean().reset_index()

        # # Sort data frame berdasarkan bulan
        # avg_metrics = avg_metrics.sort_values('Bulan')

        # # Create bar plot using plotly dan menampilkan rata-rata nilai untuk bulan tertentu
        # fig = px.bar(avg_metrics, x='Bulan', y=['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation'], barmode='group')
        # st.plotly_chart(fig)   

        # # membaca data frame dari Google Sheet
        # sheet_id2 = '154rG3WMobkWhHP4f6GjBFZLyJbxa7pw3RN3j2tESemc'
        # df1 = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv')

        # # Menambahkan kolom bulan pada data frame
        # df1['Bulan'] = pd.to_datetime(df1['Tanggal']).dt.strftime('%B')

        # # Mengelompokkan nilai berdasarkan bulan dan menghitung rata-rata dari setiap kolom
        # avg_metrics = df1.groupby('Bulan')[['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation']].mean().reset_index()

        # # Sort data frame berdasarkan bulan
        # avg_metrics = avg_metrics.sort_values('Bulan')

        # # Create bar plot using plotly dan menampilkan rata-rata nilai untuk bulan tertentu
        # fig = px.bar(avg_metrics, x='Bulan', y=['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation'], barmode='group')
        # st.plotly_chart(fig)

        # # Tampilkan metric untuk setiap kolom
        # for metric in ['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation']:
        #     st.metric(label=metric, value=avg_metrics[metric].mean(), delta=avg_metrics[metric].diff().mean())


        # membaca data frame dari Google Sheet
        sheet_id2 = '154rG3WMobkWhHP4f6GjBFZLyJbxa7pw3RN3j2tESemc'
        df1 = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv')

        # Menambahkan kolom bulan pada data frame
        df1['Bulan'] = pd.to_datetime(df1['Tanggal']).dt.strftime('%B')

        # Mengelompokkan nilai berdasarkan bulan dan menghitung rata-rata dari setiap kolom
        avg_metrics = df1.groupby('Bulan')[['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation']].mean().reset_index()

        # Sort data frame berdasarkan bulan
        avg_metrics = avg_metrics.sort_values('Bulan')

        # Create bar plot using plotly dan menampilkan rata-rata nilai untuk bulan tertentu
        fig = px.bar(avg_metrics, x='Bulan', y=['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation'], barmode='group')
        st.plotly_chart(fig)

        # Create dropdown untuk sortir data berdasarkan bulan untuk setiap metric
        sort_options = ['Ascending', 'Descending']
        sort_by = st.selectbox('Sort by', avg_metrics.columns[1:], key='sort_by')

        if st.sidebar.checkbox('Show metrics'):
            for metric in avg_metrics.columns[1:]:
                sorted_avg_metrics = avg_metrics.sort_values(sort_by, ascending=sort_options[0] == 'Ascending')
                metric_value = sorted_avg_metrics[metric].mean()
                metric_delta = sorted_avg_metrics[metric].diff().mean()
                st.metric(label=metric, value=f"{metric_value:.2f}", delta=f"{metric_delta:.2f}")

        # membaca data frame dari Google Sheet
        # sheet_id2 = '154rG3WMobkWhHP4f6GjBFZLyJbxa7pw3RN3j2tESemc'
        # df1 = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv')

        # # Menambahkan kolom bulan pada data frame
        # df1['Bulan'] = pd.to_datetime(df1['Tanggal']).dt.strftime('%B')

        # # Mengelompokkan nilai berdasarkan bulan dan menghitung rata-rata dari setiap kolom
        # avg_metrics = df1.groupby('Bulan')[['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation']].mean().reset_index()

        # # Sort data frame berdasarkan bulan
        # avg_metrics = avg_metrics.sort_values('Bulan')

        # # Create dropdown untuk sortir data berdasarkan bulan untuk setiap metric
        # sort_options = ['Ascending', 'Descending']
        # sort_by = st.selectbox('Sort by', avg_metrics.columns[1:], key='sort_by')

        # if st.sidebar.checkbox('Show metrics'):
        #     for metric in avg_metrics.columns[1:]:
        #         sorted_avg_metrics = avg_metrics.sort_values(sort_by, ascending=sort_options[0] == 'Ascending')
        #         metric_value = sorted_avg_metrics[metric].mean()
        #         metric_delta = sorted_avg_metrics[metric].diff().mean()
        #         st.metric(label=metric, value=f"{metric_value:.2f}", delta=f"{metric_delta:.2f}")

        # # Create dropdown untuk memilih bulan
        # selected_month = st.sidebar.selectbox('Select month', options=avg_metrics['Bulan'], index=len(avg_metrics)-1)

        # # Membuat data frame dengan nilai hanya pada bulan yang dipilih
        # selected_month_data = avg_metrics[avg_metrics['Bulan'] == selected_month].reset_index(drop=True)

        # # Menampilkan rata-rata dan trend setiap metric untuk bulan yang dipilih
        # if selected_month_data.shape[1] > 1:
        #     for i in range(selected_month_data.shape[1]-1):
        #         metric = selected_month_data.columns[i+1]
        #         metric_value = selected_month_data[metric].iloc[0]
        #         metric_trend = selected_month_data[metric].iloc[0] - selected_month_data[metric].iloc[1]
        #         st.metric(label=metric, value=f"{metric_value:.2f}", delta=f"{metric_trend:.2f}")
        # else:
        #     st.write("No data available for the selected month.")

        # for i in range(selected_month_data.shape[1]-1):
        #     metric = selected_month_data.columns[i+1]
        #     metric_value = selected_month_data[metric].iloc[0]
        #     metric_trend = selected_month_data[metric].iloc[0] - selected_month_data[metric].iloc[1]
        #     st.metric(label=metric, value=f"{metric_value:.2f}", delta=f"{metric_trend:.2f}")

        # # membaca data frame dari Google Sheet
        # sheet_id = '154rG3WMobkWhHP4f6GjBFZLyJbxa7pw3RN3j2tESemc'
        # df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')

        # # Menambahkan kolom bulan pada data frame
        # df['Bulan'] = pd.to_datetime(df['Tanggal']).dt.strftime('%B')

        # # Mengelompokkan nilai berdasarkan bulan dan menghitung rata-rata dari setiap kolom
        # avg_metrics = df.groupby('Bulan')[['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation']].mean().reset_index()

        # # Sort data frame berdasarkan bulan
        # avg_metrics = avg_metrics.sort_values('Bulan')

        # # Create bar plot using plotly dan menampilkan rata-rata nilai untuk bulan tertentu
        # fig = px.bar(avg_metrics, x='Bulan', y=['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation'], barmode='group')
        # st.plotly_chart(fig)

        # # Tampilkan metric untuk setiap kolom
        # st.write('## Metrics')
        # metric_sort = st.selectbox('Select metric to sort by', ['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation'])
        # avg_metrics = avg_metrics.sort_values(metric_sort, ascending=False)

        # for metric in ['satisfaction', 'response_time', 'resolution', 'friendliness', 'handling', 'effectiveness', 'communication', 'appreciation', 'recommendation']:
        #     st.write('###', metric)
        #     st.write(f"Rata-rata nilai: {avg_metrics[metric].mean():.2f}")
        #     st.write(f"Tren: {avg_metrics[metric].diff().mean():+.2f}")
        #     st.write('---')




    auth = {
        'Hilmy': '22092003',
        'KingBudiSatriaHalim': 'password2',
        'FarhanRamadhanAbdullah': 'password3',
        'JasmitaYasmin': 'password4',
        'RifaMahiraDrinaputeri': 'password5'
    }


    # Fungsi untuk menampilkan halaman login
    def show_login_page():
        st.write('Silakan masukkan email dan kata sandi Anda untuk mengakses keluhan:')
        email = st.text_input('Email')
        password = st.text_input('Kata Sandi', type='password')

        if st.button('Login'):
            if email in auth and auth[email] == password:
                # Set a flag to indicate that the user has logged in
                session = st.session_state
                session.logged_in = True
                st.session_state.email = email # tambahkan email ke dalam session state
                st.success('Login berhasil')
                Complaint_Graph()


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

