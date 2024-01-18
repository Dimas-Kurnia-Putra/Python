import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

window = tk.Tk()
window.title("Google Translate 1.0")
window.geometry("1080x400")
window.resizable(False, False)
window.configure(background="white")

def label_change(): #fungsi untuk mengubah label sesuai combobox bahasa
    c = combo1.get() #mendapatkan nilai di combobox
    c1 = combo2.get()
    
    label1.configure(text=c) # mengkonfigurasi teks di label sesuai text dari combobox
    label2.configure(text=c1)

    window.after(100, label_change)

def translate_now(): # fungsi translatenya
    text_ = text1.get(1.0,END) #mendapatkan nilai dari text1 yaitu kalimat yang akan di terjemahkan
    t1 = Translator() # mendeklarasikan translator

    #menerjemahkan teks dari bahasa sumber (src) ke bahasa tujuan (dest)
    #t1 adalah objek Translator dari modul googletrans.
    #translate() adalah metode dari objek Translator yang digunakan untuk menerjemahkan teks.
    #text_ adalah teks yang akan diterjemahkan. text_ sepertinya merupakan variabel yang berisi teks yang ingin Anda terjemahkan.
    #src=combo1.get() mengambil nilai dari combo1 (ComboBox pertama) yang dipilih pengguna sebagai bahasa sumber.
    #dest=combo2.get() mengambil nilai dari combo2 (ComboBox kedua) yang dipilih pengguna sebagai bahasa tujuan.
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())

    #Setelah baris pertama dieksekusi, translate_text berisi hasil dari terjemahan teks dari bahasa sumber ke bahasa tujuan.
    translate_text = trans_text.text

    text2.delete(1.0, END) #mengapus text yang ada pada objek text2
    text2.insert(END, translate_text) # mengisi text2 hasil dari kalimat yang sudah diterjemahkan

def swab_translate(): #menukar bahasa yang akan ditranslate
    comb1 = combo1.get()
    comb2 = combo2.get()

    combo1.set(comb2) # .set() memilih nilai yang dipilih pada combobox
    combo2.set(comb1)

#arrow
arrow = tk.Button(window, text="<<==>>", font=("Roboto 14", 18, "bold"), width=9, command=lambda:swab_translate())
arrow.place(x=467, y=130)

nama = tk.Label(window, text="D1M4S.app", font=("Roboto", 22, "bold"), width=9)
nama.place(x=454, y=0)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

#first combobox
combo1 = ttk.Combobox(window, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("indonesian")

label1 = tk.Label(window, text="indonesian", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

#second combobox
combo2 = ttk.Combobox(window, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("select language")

label2 = tk.Label(window, text="english", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=625, y=50)

#first frame
frame1 = tk.Frame(window, bg="black", bd=5)
frame1.place(x=10, y=118, width=440, height=250)

text1 = tk.Text(frame1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=410, height=240)

#membuat scrollbar 1
scrollbar1 = ttk.Scrollbar(frame1)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#second frame
frame2 = tk.Frame(window, bg="black", bd=5)
frame2.place(x=620, y=118, width=440, height=250)

text2 = tk.Text(frame2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=410, height=240)

#membuat scrollbar 2
scrollbar2 = ttk.Scrollbar(frame2)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button
translate = tk.Button(window, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, width=10,
                      height=2, bg="black", fg="white", command=lambda:translate_now())
translate.place(x=476, y=250)

label_change()

window.mainloop()
