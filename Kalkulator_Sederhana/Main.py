import tkinter as tk
import time

def isi_entry(digit):
    entry.insert("end", digit) #mengisi isi Entry
    
def hasil():
	try:
		has = entry.get() #mengambil isi Entry
		nilai = eval(has) #mengkalkulasi isi Entry dengan methode eval()	
		entry.delete(0, tk.END) #menghapus isi Entry
		entry.insert("end", nilai) #mengisi Entry dengan hasil kalkulasi
	except:
		entry.insert("end", "input error")
		time.sleep(1) #delay 1 detik
		entry.delete(0, tk.END)

def delete(): #fungsi untuk mendelete
	entry.delete(0, tk.END)

def center_window(window, width, height): #fungsi untuk menentukan window berada ditengah layar pada saat program dijalankan
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))

    window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

root = tk.Tk() #window
center_window(root, 500, 600) #pemanggilan fungsi untuk menentukan letak window

frame = tk.Frame(root, pady=30) #frame
frame.pack()


custom_font = ("Helvetica", 16) # custom font

entry = tk.Entry(frame, font=custom_font, width=30) #membuat isi Entry besar sesuai ukuran font
entry.pack()

frameButton = tk.Frame(root) # frame untuk button
frameButton.pack()

rows = 0 #baris
cols = 0 #kolom


for i in range(1, 10):
    #membuat button dari 1 - 9
    #fungsi lambda digunakan untuk memanggil fungsi saat di klik bukan saat button dibuat
	button = tk.Button(frameButton, text=str(i), width=5, height=3, command=lambda angka=i: isi_entry(str(angka)))
	if cols > 2: #untuk menentukan column jika sumbu x sudah terisi 3 button akan membuat y baru dan x kembali ke 0
		rows += 1
		cols = 0
		
	button.grid(row=rows, column=cols, padx=5, pady=5)
	cols +=1
 
buttonZero = tk.Button(frameButton, text="0", width=5, height=3, command=lambda: isi_entry("0"))
buttonZero.grid(row=3, column=1)
    
buttonKali = tk.Button(frameButton, text="x", width=5, height=3, command=lambda: isi_entry("*"))
buttonKali.grid(row=4, column=0)

buttonBagi = tk.Button(frameButton, text="÷", width=5, height=3, command=lambda: isi_entry("/"))
buttonBagi.grid(row=4, column=1)

buttonTambah = tk.Button(frameButton, text="+", width=5, height=3, command=lambda: isi_entry("+"))
buttonTambah.grid(row=4, column=2)

buttonKurang = tk.Button(frameButton, text="-", width=5, height=3, command=lambda: isi_entry("-"))
buttonKurang.grid(row=5, column=0)

buttonKoma = tk.Button(frameButton, text=".", width=5, height=3, command=lambda: isi_entry("."))
buttonKoma.grid(row=5, column=1)

buttonC = tk.Button(frameButton, text="C", width=5, height=3, command= lambda : delete())
buttonC.grid(row=5, column=2)

buttonSDengan = tk.Button(frameButton, text="=", width=5, height=3, command= lambda : hasil())
buttonSDengan.grid(row=6, column=1)


root.mainloop()