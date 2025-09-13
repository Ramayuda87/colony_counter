import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, Button, Label
from tkinter import messagebox

# Fungsi untuk memproses gambar dan menghitung koloni
def count_colonies(image_path):
    # Membaca gambar
    image = cv2.imread(image_path)

    # Konversi gambar ke grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Mengurangi noise dengan Gaussian Blur
    blurred_image = cv2.GaussianBlur(gray_image, (11, 11), 0)

    # Thresholding untuk membuat gambar biner
    _, binary_image = cv2.threshold(blurred_image, 120, 255, cv2.THRESH_BINARY_INV)

    # Mendeteksi kontur (koloni bakteri)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Menghitung jumlah koloni
    colony_count = len(contours)

    # Gambar kontur di atas gambar asli
    output_image = image.copy()
    
    # Menambahkan anotasi jumlah koloni di samping setiap kontur
    for i, contour in enumerate(contours):
        # Menghitung posisi titik pusat kontur
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            # # Menambahkan anotasi teks dengan ukuran dan ketebalan yang dapat disesuaikan
            # cv2.putText(output_image, str(i+1), (cX + 5, cY - 5), 
            #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Gambar kontur di atas gambar output
        cv2.drawContours(output_image, [contour], -1, (0, 255, 0), 2)

    return colony_count, binary_image, output_image

# Fungsi untuk membuka dialog pemilihan gambar dan menghitung koloni
def open_file():
    # Membuka dialog untuk memilih file gambar
    file_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    if file_path:
        try:
            # Hitung koloni untuk gambar yang dipilih
            colony_count, binary_image, output_image = count_colonies(file_path)

            # Menampilkan hasil di console
            print(f"Jumlah koloni yang terdeteksi: {colony_count}")

            # Tampilkan gambar dengan hasil perhitungan
            plt.figure(figsize=(15, 7))

            # Judul untuk gambar hasil
            plt.title(f"Jumlah koloni yang terdeteksi: {colony_count}")
            plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            # Menampilkan pesan error jika ada masalah dengan pemrosesan gambar
            messagebox.showerror("Error", f"Gagal memproses gambar: {e}")
    else:
        messagebox.showwarning("Peringatan", "Tidak ada gambar yang dipilih!")

# Membuat jendela Tkinter
root = Tk()
root.title("Deteksi Koloni Bakteri")
root.geometry("400x200")

# Label instruksi
label = Label(root, text="Pilih gambar untuk menghitung koloni bakteri", padx=20, pady=20)
label.pack()

# Tombol untuk memilih gambar dan menghitung koloni
button = Button(root, text="Pilih Gambar", command=open_file, padx=10, pady=10)
button.pack()

# Menjalankan aplikasi Tkinter
root.mainloop()
