# Aplikasi Colony Counter

Aplikasi Python sederhana menggunakan **OpenCV**, **Tkinter**, dan **Matplotlib** untuk mendeteksi serta menghitung jumlah koloni bakteri (gram negatif) pada gambar cawan Petri.

---

## Fitur
- Memuat gambar (format JPG, PNG, JPEG) melalui dialog file.
- Konversi gambar ke grayscale, reduksi noise dengan Gaussian Blur, dan thresholding.
- Deteksi koloni menggunakan metode kontur (contour detection).
- Menampilkan jumlah koloni yang terdeteksi.
- Tampilan GUI sederhana menggunakan Tkinter.

---

## Cara Menjalankan
1. **Clone repository ini:**
   ```bash
   git clone https://github.com/Ramayuda87/colony_counter.git
   cd colony_counter
   ```

2. Install Dependensi
   - pip install -r requirements.txt
  
3. Jalankan aplikasi
   python colony_counter.py

## Dependensi
- opencv-python
- numpy
- matplotlib
- tkinter

## Tampilan
- ![gambar utama](https://github.com/user-attachments/assets/c8434327-fc45-4c98-891d-3745ddb9427e)
- ![bakteri2](https://github.com/user-attachments/assets/1c556268-53fd-4665-b862-e70394d9c9ee)
- ![gambar hasil](https://github.com/user-attachments/assets/31b7ec3d-da1d-467c-b069-6828da0816e1)

## Lisensi
Proyek ini bersifat open-source dan dapat digunakan bebas untuk tujuan pembelajaran.
Tentunya masih banyak kekurangan dalam aplikasi ini dan butuh pengembangan lebih lanjut.
