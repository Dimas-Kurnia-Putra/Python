import tkinter as tk
from tkinter import *
from tkinter import ttk

#data Utama
data = [
    ["Jhon", "Smith", 18, 22101134, "Depok"],
    ["Micahe", "Jhon", 16, 22101134, "Tanggerang"],
    ["Ucok", "baba", 18, 22101134, "Jakarta"],
    ["Ucup", "jordan", 18, 22101134, "Bogor"],
    ["Alice", "Johnson", 22, 22101134, "Bekasi"],
    ["Bob", "Anderson", 25, 22101134, "Palembang"],
    ["Eve", "Williams", 20, 22101134, "Bandung"]
]


#deklarasi variable karna digunakan di beberapa fungsi
frame_login = None
frame_utama = None
frame_add_data = None
frame_cari = None
Entry_search = None


#HALAMAN LOGIN
def login():
    global window, frame_login

    def cek_idpass():
        id = Entry_Username.get()
        password = Entry_Password.get()

        if id == "Admin" and password == "1234":
            Home()
            return
        else:
            label_Log_Failed = tk.Label(frame_login, text="GAGAl LOGIN", font=("Arial", 15))
            label_Log_Failed.grid(row=4, column=1, pady=10) 

    frame_login = tk.Frame(window)
    frame_login.pack()

    label_Login = tk.Label(frame_login, text="Login D1M4S.app", font=("Arial", 30, "bold"))
    label_Login.grid(row=0, column=1, pady=40, columnspan=2)

    label_Username = tk.Label(frame_login, text="Username", font=("Arial", 16))
    label_Username.grid(row=1, column=0, pady=10)

    Entry_Username = tk.Entry(frame_login, font=("Arial", 16))
    Entry_Username.grid(row=1, column=1, pady=10)

    label_Password = tk.Label(frame_login, text="Password", font=("Arial", 16))
    label_Password.grid(row=2, column=0, pady=10)

    Entry_Password = tk.Entry(frame_login, show="*", font=("Arial", 16))
    Entry_Password.grid(row=2, column=1, pady=10)

    Button_Enter = tk.Button(frame_login, text="Login", font=("Arial", 16), borderwidth=5, width=20, bg='#333333', fg='white', command= lambda:cek_idpass())
    Button_Enter.grid(row=3, column=1, pady=10)
    
#HALAMAN UTAMA
def Home():
    global window, data, frame_login, frame_utama, frame_add_data, Entry_search
    #menghancurkan frame frame

    if frame_login:
        frame_login.destroy()
    
    if frame_add_data:
        frame_add_data.destroy()

    #membuat frame
    frame_utama = tk.LabelFrame(window, text="KELAS LEVIOSA", font=("Arial", 16, "bold"))
    frame_utama.pack(padx=20, pady=20)

    Entry_search = tk.Entry(frame_utama, font=("Arial", 11), width=50)
    Entry_search.grid(row=0, column=0, padx=5, pady=10)
    
    Button_search = tk.Button(frame_utama, text="SEARCH", font=("Arial", 11), borderwidth=5, bg='#333333', fg='white', command=lambda:Search_Data())
    Button_search.grid(row=0, column=1, padx=5, pady=10)

    Button_addData = tk.Button(frame_utama, text="ADD DATA", font=("Arial", 11), borderwidth=5, bg='#333333', fg='white', command=lambda:Frame_Add_Data())
    Button_addData.grid(row=1, column=1, padx=5, pady=10)

    frame_tabel = tk.LabelFrame(frame_utama, text="DATA MAHASISWA", font=("Arial", 16, "bold"))
    frame_tabel.grid(row=2, column=0, columnspan=4, padx=10, pady=(10,60))

    #membuat tabel manual
    judul = ["First_Name", "Last_Name", "Age"]

    for col, isi in enumerate(judul):
        label_judul = tk.Label(frame_tabel, text=isi, font=("Arial", 11, "bold"), padx=10)
        label_judul.grid(row=0, column=col)  # menentukan letak judul table
        garis = tk.Label(frame_tabel, text="--------------------")
        garis.grid(row=1, column=col)

    #mencetak data data ke dalam tabel
    indeks_Data = 0 #menentukan indeks perbaris data utama
    for row, item in enumerate(data, start=2):
        butNumber = 0
        for col, value in enumerate(item[:3]):
            
            # membuat tk.Label
            label_data = tk.Label(frame_tabel, text=value, font=("Arial", 11, "bold"), padx=10, pady=5)
            # menentukan letak dari isi dari list dari data item
            label_data.grid(row=row, column=col, pady=5)

            butNumber +=1 #menentukan indeks item habis akan dibuat button

            if butNumber == 3:
                #command= lambda r=indeks_Data : Update_Data(r) 
                #mengambil parameter indeks dari data untuk dieksekusi didalam fungsi
                button_Edit = tk.Button(frame_tabel, text= "EDIT", width=10, padx=10, pady=5, borderwidth=5, bg='#333333', fg='white', command= lambda r=indeks_Data : Update_Data(r))
                button_Edit.grid(row=row, column=col+1, pady=5, padx=(0, 5))

                button_Detail = tk.Button(frame_tabel, text= "DETAIL", width=10, padx=10, pady=5, borderwidth=5, bg='#333333', fg='white', command=lambda r=indeks_Data : Detail_Data(r))
                button_Detail.grid(row=row, column=col+2, pady=5, padx=(0, 5))

                button_Delete = tk.Button(frame_tabel, text= "DELETE", width=10, padx=10, pady=5, borderwidth=5, bg='#333333', fg='white', command=lambda r=indeks_Data : Delete_Data(r))
                button_Delete.grid(row=row, column=col+3, pady=5, padx=(0, 5))
        
        indeks_Data+=1

#Window untuk menambahkan data
def Frame_Add_Data():
    global window, data, frame_utama, frame_add_data

    def Added_Data():
        firstName = Entry_firstName.get()
        lastName = Entry_lastName.get()
        age = Entry_age.get()
        nim = int(Entry_NIM.get())
        address = Entry_Address.get()

        dataTemp = [ #data sementara
            firstName,
            lastName,
            age,
            nim,
            address
        ]

        data.insert(0, dataTemp) # menambahkan data sesuai indeks

        Home()
        return

    #menghancurkan frame
    if frame_utama:
        frame_utama.destroy()

    #membuat frame
    frame_add_data = tk.LabelFrame(window, text="ADD DATA", font=("Arial", 16, "bold"), height=100)
    frame_add_data.pack(expand=True)

    label_firstName = tk.Label(frame_add_data, text="First Name", font=("Arial", 11))
    label_firstName.grid(row=0, column=0)

    label_lastName = tk.Label(frame_add_data, text="Last Name", font=("Arial", 11))
    label_lastName.grid(row=0, column=1)

    label_age = tk.Label(frame_add_data, text="Age", font=("Arial", 11))
    label_age.grid(row=0, column=2)

    label_NIM = tk.Label(frame_add_data, text="NIM", font=("Arial", 11))
    label_NIM.grid(row=2, column=0)

    label_Address = tk.Label(frame_add_data, text="Address", font=("Arial", 11))
    label_Address.grid(row=2, column=1)


    Entry_firstName = tk.Entry(frame_add_data, width=20, font=("Arial", 11))
    Entry_firstName.grid(row=1, column=0, padx=3, pady=5)

    Entry_lastName = tk.Entry(frame_add_data, width=20, font=("Arial", 11))
    Entry_lastName.grid(row=1, column=1, padx=3, pady=5)

    Entry_age = tk.Entry(frame_add_data, width=20, font=("Arial", 11))
    Entry_age.grid(row=1, column=2, padx=3, pady=5)

    Entry_NIM = tk.Entry(frame_add_data, width=20, font=("Arial", 11))
    Entry_NIM.grid(row=3, column=0, padx=3, pady=5)

    Entry_Address = tk.Entry(frame_add_data, width=20, font=("Arial", 11))
    Entry_Address.grid(row=3, column=1, padx=3, pady=5)

    Button_Finish_addData = tk.Button(frame_add_data, text="FINISH ADD DATA", borderwidth=5, bg='#333333', fg='white', font=("Arial", 11), command=lambda:Added_Data())
    Button_Finish_addData.grid(row=4, column=1)


#HALAMAN DETAIL
def Detail_Data(row):
    global window, frame_utama, data
    
    def Exit():
        if frame_detail:
            frame_detail.destroy()
            Home()

    frame_utama.destroy()

    #mengambil data berdasarkan indeks yang didapat dari parameter fungsi di button DETAIL
    detail_data = data[row]

    frame_detail = tk.LabelFrame(window)
    frame_detail.pack(pady=100)

    judul = ["First_Name", "Last_Name", "Age", "NIM", "Address"]

    for col, isi in enumerate(judul, start=0):
        label_judul = tk.Label(frame_detail, text=isi, font=("Arial", 11), padx=10)
        label_judul.grid(row=0, column=col)  # menentukan letak judul table
        garis = tk.Label(frame_detail, text="--------------------")
        garis.grid(row=1, column=col)

    #membuat button exit
    butNumber_detail = 0
    for col, value in enumerate(detail_data, start=0):
        # membuat tk.Label    
        label_data = tk.Label(frame_detail, text=value, font=("Arial", 11), padx=10, pady=5)
        # menentukan letak dari isi dari list (nama, nim, fakultas)
        label_data.grid(row=2, column=col, pady=5)

        butNumber_detail +=1
        if butNumber_detail == 4:
            Button_Exit = tk.Button(frame_detail, text="EXIT", borderwidth=5, bg='#333333', fg='white', width=20, command=lambda:Exit())
            Button_Exit.grid(row=1, column=col+2)


#HALAMAN EDIT
def Update_Data(row):
    global window, frame_utama, data

    #mengambil data satu baris list dari data utama didapat dari parameter fungsi
    sublist_edit = data[row]

    first_name, last_name, age, nim, address = sublist_edit

    default_firsname = first_name
    default_lastname = last_name
    default_age = age
    default_nim = nim
    default_address = address

    #memunculkan data lama yang ingin diubah ke form entry dengan tk.StringVar()
    string_var1 = tk.StringVar(window)
    string_var1.set(default_firsname)

    string_var2 = tk.StringVar(window)
    string_var2.set(default_lastname)

    string_var3 = tk.StringVar(window)
    string_var3.set(default_age)

    string_var4 = tk.StringVar(window)
    string_var4.set(default_nim)

    string_var5 = tk.StringVar(window)
    string_var5.set(default_address)


    #untuk mengupdate data yang sudah di input dengan data yang baru
    def cek_edit_data():
        firtName = Entry_firstName.get()
        lastName = Entry_lastName.get()
        age = Entry_age.get()
        nim = Entry_NIM.get()
        address = Entry_Address.get()

        #mengembalikan data sesuai dengan indeks di data utama, row didapat dari parameter button EDIT
        data[row] = [firtName, lastName, age, nim, address]

        if frame_edit:
            frame_edit.destroy()
            Home()
    
    #menghancurkan frame
    if frame_utama:
        frame_utama.destroy()

    #membuat frame untuk edit data
    frame_edit = tk.LabelFrame(window)
    frame_edit.pack(pady=100)

    label_firstName = tk.Label(frame_edit, text="First Name", font=("Arial", 11))
    label_firstName.grid(row=0, column=0)

    label_lastName = tk.Label(frame_edit, text="Last Name", font=("Arial", 11))
    label_lastName.grid(row=0, column=1)

    label_age = tk.Label(frame_edit, text="Age", font=("Arial", 11))
    label_age.grid(row=0, column=2)

    label_NIM = tk.Label(frame_edit, text="NIM", font=("Arial", 11))
    label_NIM.grid(row=2, column=0)

    label_Address = tk.Label(frame_edit, text="Address", font=("Arial", 11))
    label_Address.grid(row=2, column=1)

    Entry_firstName = tk.Entry(frame_edit, width=20, font=("Arial", 11), textvariable=string_var1)
    Entry_firstName.grid(row=1, column=0, padx=3, pady=5)

    Entry_lastName = tk.Entry(frame_edit, width=20, font=("Arial", 11), textvariable=string_var2)
    Entry_lastName.grid(row=1, column=1, padx=3, pady=5)

    Entry_age = tk.Entry(frame_edit, width=20, font=("Arial", 11), textvariable=string_var3)
    Entry_age.grid(row=1, column=2, padx=3, pady=5)

    Entry_NIM = tk.Entry(frame_edit, width=20, font=("Arial", 11), textvariable=string_var4)
    Entry_NIM.grid(row=3, column=0, padx=3, pady=5)

    Entry_Address = tk.Entry(frame_edit, width=20, font=("Arial", 11), textvariable=string_var5)
    Entry_Address.grid(row=3, column=1, padx=3, pady=5)

    Button_Finish_editData = tk.Button(frame_edit, text="FINISH EDIT DATA", borderwidth=5, bg='#333333', fg='white', font=("Arial", 11), command=lambda:cek_edit_data())
    Button_Finish_editData.grid(row=4, column=1)


#Mencari data
def Search_Data():
    global window, data, Entry_search, frame_cari, frame_utama, Home

    dicari = Entry_search.get() #harus ada sebelum frame utama di destroy
    dicari.lower()

    if frame_utama:
        frame_utama.destroy()

    frame_cari = tk.LabelFrame(window)
    frame_cari.pack(pady=100)

    def Exit():
        if frame_cari:
            frame_cari.destroy()
            Home()
    
    result = [] #list untuk menampung pencarian data apabila lebih dari satu data
    #melakukan pencarian data
    for cari_data in data:
        #bila ketemu
        #map() mengambil dua argumen: fungsi yang akan diterapkan pada setiap elemen, dan iterable (list, tuple, dsb.)
        #yang akan diolah oleh fungsi tersebut. 
        #map mengembalikan 2 indeks dari cari_data yaitu nama depan dan nama belakang
        if dicari.lower() in map(str.lower, cari_data[:2]):
            #mengambil data sesuai data yang dicari "cari_data" satu baris list 
            result.append(cari_data)

    #bila tidak ketemu / list result kosong               
    if not result:
        label_data_tidakditemukan = tk.Label(frame_cari, text="DATA TIDAK DITEMUKAN", font=("Arial", 20))
        label_data_tidakditemukan.grid(row=0, column=1, columnspan=3)
        
        Button_Exit = tk.Button(frame_cari, text="EXIT", borderwidth=5, bg='#333333', fg='white', width=20, command=lambda:Exit())
        Button_Exit.grid(row=1, column=1, columnspan=3)
    
    else:
        judul = ["First_Name", "Last_Name", "Age", "NIM", "Address"]

        for col, isi in enumerate(judul, start=0):
            label_judul = tk.Label(frame_cari, text=isi, font=("Arial", 11), padx=10)
            label_judul.grid(row=0, column=col)  # menentukan letak judul table
            garis = tk.Label(frame_cari, text="--------------------")
            garis.grid(row=1, column=col)

        
        for row, list_result in enumerate(result):
            butNumber_detail = 0 
            for col, value in enumerate(list_result, start=0):
                # membuat tk.Label    
                label_data = tk.Label(frame_cari, text=value, font=("Arial", 11), padx=10, pady=5)
                # menentukan letak baris dan column
                label_data.grid(row=row+2, column=col, pady=5)

                butNumber_detail +=1
                if butNumber_detail == 4: #jika data nama depan, belakang dan lain lain sudah dibuat maka dibuat button exit
                    Button_Exit = tk.Button(frame_cari, text="EXIT", borderwidth=5, bg='#333333', fg='white', width=20, command=lambda:Exit())
                    Button_Exit.grid(row=row+2, column=col+2)

#Mengapus data berdasarkan baris list atau indeks list data
def Delete_Data(row):
    global data, frame_utama

    del data[row] #menghapus berdasarkan indeks dari data utama, row didapat dari button DELETE

    if frame_utama:
        frame_utama.destroy()
        Home()


#MEMBUAT WINDOW DI TENGAH
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))

    window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

"""MAINLOOP"""
window = tk.Tk()
window.title("GUI-Data-Entry_CRUDS")
window.state('zoomed')
width = 926
height = 700
center_window(window, width, height)

# # Create A Main frame
# main_frame = tk.Frame(window)
# main_frame.pack(fill=BOTH, expand=1)

# # Create A canvas
# my_canvas = tk.Canvas(main_frame)
# my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# # Add a Scrollbar to the canvas
# my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
# my_scrollbar.pack(side=RIGHT, fill=Y)

# # Configure the Canvas
# my_canvas.configure(yscrollcommand=my_scrollbar.set)
# my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# #Create another frame inside the canvas
# second_frame = tk.Frame(my_canvas)

# # Add that new frame to a window in the canvas
# my_canvas.create_window((0,0), window=second_frame, anchor='nw')

#login()
Home()


window.mainloop()