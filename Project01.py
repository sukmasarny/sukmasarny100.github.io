import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import graphviz as graphviz
from PIL import Image
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

with open('search.html') as f:
    st.markdown(f'<search>{f.read()}</search>', unsafe_allow_html=True)
    """"""
    """"""
    """"""
    """"""

# Object notation
st.sidebar.markdown("<h1 style='text-align: center; color: black;'>Welcome to Our Project</h1>", unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("")


option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('🏠 Home','🔍 Analisis','📝 Modeling')
)


if option == '🏠 Home' or option == '':
    st.markdown("<h2 style='text-align: center; color: green;'>ANDROID MALWARE</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("")
    st.sidebar.markdown("<h3 style='text-align: center; color:  black;'>Informasi Tambahan</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
            <p style=='color: black; '>Kontribusi :</p>
            <o1 style=='color: black;'>
                <li> Nama: Wa Ode Sukmasarny(Coding)</li>
                <li> Nama: Hesti Yuana(Coding)</li>
                <li> Nama: Sandra Armayanti(Konten)</li>
                <li> Nama: Nina Novita Sapitri(Konten)</li>
            </o1>
            """, unsafe_allow_html=True)
        
            
    """"""
    """"""
    """"""
    """"""

    st.markdown("<div style='text-align: justify;'>Saat ini perkembangan teknologi semakin cepat berkembang, Sehingga dapat mempermudah manusia untuk mencari informasi yang ada diseluruh dunia dengan menggunakan teknologi yang tersambung internet. Dan untuk saat ini smartphone merupakan teknologi yang perkembanganya cukup cepat dalam segi jumlah pengguna. Android sendiri merupakan sistem operasi yang sangat digemari oleh pengguna teknologi saat ini. Dengan banyaknya pengguna sistem operasi Android tersebut semakin banyak pula kejahatan yang berada dalam lingkup teknologi smartphone.", unsafe_allow_html=True)
    """"""
    """"""
    st.subheader('Malicious Software')
    st.markdown("<div style='text-align: justify;'>Malicious software adalah perangkat lunak yang dirancang untuk menyerang,merusak,menonaktifkan, atau mengganggu komputer, sistem komputer, atau Jaringan. Malware mengacu pada program yang disisipkan ke dalam sebuah sistem, biasanya secara terselubung dengan maksud untuk melihat kerahasiaan korban baik berbentuk data, aplikasi, ataupun sistem oprasi.",unsafe_allow_html=True)
    """"""
    """"""
    st.subheader('Android Malware')
    st.markdown("<div style='text-align: justify;'>Android Malware adalah perangkat lunak berbahaya yang dibuat untuk menyerang sistem operasi android pada smartphone. Malware bergantung pada eksploitasi sistem operasi, tertentu dan software pada ponsel",unsafe_allow_html=True)
    st.write()
    st.write()
    """"""
    """"""
    

    """"""
    """"""
    st.subheader("Jenis-Jenis Malware")
    st.markdown("<div style='text-align: justify;'>A. Adware merupakan sebuah perangkat lunak yang menampilkan unduhan iklan tanpa izin dan menampilkan spanduk pada antarmuka pengguna program saat pengguna terhubung ke internet. Adware dimasukkan secara diam-diam oleh pembuat program dengan kemampuan untuk mengunduh dan menampilkan materi iklan secara otomatis tanpa di ketahui penggunanya. Adware ini umumnya berbentuk seperti iklan Pop-Up yang ada di suatu situs.", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>B. Spyware merupakan malware yang muncul sebagai aplikasi jinak, tetapi sebenarnya malware tersebut memonitori informasi rahasia pengguna seperti pesan, kontak, lokasi, dll. Spywares pribadi dapat menginstal muatan berbahaya tanpa sepengetahuan korban. Malware tersebut mengirimkan informasi korban seperti pesan teks, kontak ,dll kepada penyerang yang menginstal software tersebut pada perangkat korban", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>C. Virus merupakan Virus merupakan salah satu jenis Malware yang mempunyai kemampuan untuk memanipulasi data, menginfeksi, mengubah dan merusak sebuah program komputer perusahaan. Adapun kemampuan lain dari virus ini, yaitu dapat menggandakan diri dengan cara menyelipkan program dari kopian dari asal dirinya menjadi bagian dari program lain di komputer", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>D. Worms merupakan malware yang menyerang melalui jaringan. Misalnya, worm bluetooth menyebarkan malware melalui jaringan bluetooth dengan mengirimkan salinan malware keperangkat yang terhubung", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>E. Trojan merupakan malware yang terlihat bersifat benign. Bahkan, trojan benar benar mencuri informasi rahasia pengguna tanpa sepengetahuan pengguna. Perangkat semacam ini dapat dengan mudah mendapatkan akses ke riwayat penelusuran, pesan , kontak dll. Perangkat mencuri informasi ini tanpa persetujuan pengguna", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>F. Ransomwares merupakan malware yang mencegah pengguna mengakses data mereka diperangkatnya dengan mengunci perangkat tersebut. Hingga jumlah tebusan yang diajukan penyerang dibayarkan", unsafe_allow_html=True)
    """"""  
    """""" 
    """""" 
    st.subheader('Cara Terinfeksi dan Mencegah Malware pada Perangkat Android\n\n')
    """"""
    st.write('**A. Email Spam**\n')
    st.markdown("<div style='text-align: justify;'>Pembuat *malware* sering mencoba menipu untuk mengunduh file yang berbahaya. Salah satu bentuk penipuan berupa email dengan file terlampir yang memberi tahu bahwa email tersebut adalah tanda terima untuk pengiriman, pengembalian pajak, atau faktur untuk tiket. Sehingga membuat pengguna harus membuka lampiran tersebut untuk mendapatkan barang yang dikirimkan atau untuk mendapatkan uang.", unsafe_allow_html=True)
    """"""
    st.markdown("""
            <p style=='color: black; '>Solusi mengurangi kemungkinan perangkat terinfeksi dari email spam adalah sebagai berikut :</p>
            <o1 style=='color: black;'>
                <li> Jika tidak yakin siapa yang mengirimi email atau ada yang tidak beres diharapkan jangan dibuka</li>
                <li> Jangan pernah mengklik tautan tak terduga dalam email</li>
                <li> Jangan membuka lampiran pada email yang tidak Anda harapkan.</li>
            </o1>
            """, unsafe_allow_html=True)

    """"""
    """"""
    """"""
    st.write('**B. Perangkat Drive yang Terinfeksi**\n')
    st.markdown("<div style='text-align: justify;'>Malware dapat diinstal secara otomatis ketika menghubungkan storage device yang terinfeksi. Malware dapat menyebar dengan menginfeksi removable drive seperti USB flash drive atau hard drive eksternal.", unsafe_allow_html=True)
    st.markdown("""
            <p style=='color: black; '>Hal yang dapat dilakukan untuk menghindari jenis infeksi dari storage device sebagai berikut :</p>
            <o1 style=='color: black;'>
                <li> Berhati-hatilah terhadap perangkat USB yang tidak dimiliki.</li>
                <li> Jangan pernah mengklik tautan tak terduga dalam email</li>
                <li> Jika memasang perangkat drive yang tidak dikenal segera jalankan pemindaian keamanan.</li>
            </o1>
            """, unsafe_allow_html=True)

    """"""
    """"""
    st.write('**C. Perangkat Lunak yang Terinfeksi**\n')
    st.markdown("<div style='text-align: justify;'>Malware dapat diinstal bersamaan dengan program lain yang telah diunduh. Sehingga lebih dikenal sebagai perangkat lunak dari situs web pihak ketiga atau file yang dibagikan melalui jaringan peer-to-peer. Beberapa program juga akan menginstal perangkat lunak lain yang mungkin tidak diinginkan. Salah satu contohnya yaitu program yang menampilkan iklan tambahan saat menggunkan website tersebut.", unsafe_allow_html=True)
    """"""
    st.markdown("""
            <p style=='color: black; '>Langkah dalam menghindari pemasangan malware atau perangkat lunak yang mungkin tidak diinginkan dengan cara sebagai berikut:</p>
            <o1 style=='color: black;'>
                <li> Selalu unduh perangkat lunak dari situs web vendor resmi</li>
                <li> Pastikan membaca dengan tepat ketika akan menginstal, jangan hanya mengklik OK</li>
            </o1>
            """, unsafe_allow_html=True)

    """"""
    """"""
    st.write('**D. Halaman Website yang Diretas**\n')
    st.write('*Malware* dapat menggunakan kerentanan perangkat lunak yang diketahui untuk menginfeksi perangkat android. Kerentanan seperti lubang di perangkat android yang dapat memberikan akses malware. Salah satunya dengan cara situs web tersebut yang mungkin berbahaya atau dapat berupa situs web sah yang telah disusupi atau diretas.')
    st.write('Hal yang dapat dilakukan untuk menghindari jenis infeksi dari website yang telah diretas adalah sebagai berikut :')
    st.write('1. Sangat penting untuk selalu memperbarui semua perangkat lunak pada android yang dimiliki terutama browser web serta menghapus perangkat lunak yang tidak digunakan, termasuk ekstensi browser yang tidak digunakan.')
    st.write('2. Mengurangi kemungkinan terkena malware dengan cara dengan menggunakan browser modern, seperti google chrome atau firefox dan terus memperbaruinya.\n\n')


elif option == '🔍 Analisis':
    st.subheader('Statistik Analisis') #Menampilkan judul halaman dataframe
    st.markdown("<div style='text-align: justify;'>Statistik Analisis merupakan Teknik static analysis dilakukan tanpa menjalankan aplikasi dalam emulator atau perangkat android. Analisi statis adalah teknik untuk mengamati perilaku malware dengan menganalisa segmen code. Namun ada beberapa kelamahan static analysis yaitu ada beberapa code yang sulit dipecahkan dengan teknik ini. Keuntungan dari analisis ini adalah biayanya yang terhitung murah dan tidak memakan waktu banyak.", unsafe_allow_html=True)
    """"""
    """"""
   