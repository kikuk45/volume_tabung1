import streamlit as st
# import math # Tidak perlu math jika kita mendefinisikan PI_VALUE sendiri

def hitung_volume_tabung(jari_jari, tinggi, pi_value_to_use):
  """
  Menghitung volume tabung berdasarkan jari-jari, tinggi, dan nilai pi yang ditentukan.

  Args:
    jari_jari: Jari-jari alas tabung.
    tinggi: Tinggi tabung.
    pi_value_to_use: Nilai pi yang akan digunakan (misalnya 22/7 atau 3.14).

  Returns:
    Volume tabung.
  """
  volume = pi_value_to_use * (jari_jari ** 2) * tinggi
  return volume

st.title("Kalkulator Volume Tabung")
st.write("Aplikasi sederhana untuk menghitung volume tabung.")

# Input dari pengguna
st.header("Masukkan Dimensi Tabung")

jari_jari_input = st.number_input("Masukkan jari-jari tabung (cm):", min_value=0.0, value=7.0)
tinggi_input = st.number_input("Masukkan tinggi tabung (cm):", min_value=0.0, value=10.0)

# Tombol untuk menghitung
if st.button("Hitung Volume"):
  if jari_jari_input <= 0 or tinggi_input <= 0:
    st.error("Jari-jari dan tinggi harus lebih besar dari nol.")
  else:
    # Logika untuk memilih nilai Pi
    if jari_jari_input % 7 == 0: # Memeriksa apakah jari-jari adalah kelipatan 7
      PI_VALUE = 22 / 7
      pi_description = "($\pi = 22/7$)"
    else:
      PI_VALUE = 3.14
      pi_description = "($\pi = 3.14$)"

    volume_hasil = hitung_volume_tabung(jari_jari_input, tinggi_input, PI_VALUE)
    st.success(f"Volume tabung adalah: **{volume_hasil:.2f} cm³**")
    st.write(f"Perhitungan ini menggunakan nilai Pi {pi_description}.") # Keterangan Pi yang digunakan
    st.balloons() # Efek balon setelah perhitungan
