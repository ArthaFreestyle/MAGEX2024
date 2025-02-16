from tkinter import Tk, StringVar
from tkinter import ttk
from tkinter.messagebox import showinfo


window = Tk()
window.title("Welcome to Artha's app")
window.configure(bg='white')
window.geometry('350x200')

#Frame 
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

#Label
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10, fill='x', expand=True)

#Entry
NAMA_DEPAN = StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill='x', expand=True)

#Tombol
tombol_sapa = ttk.Button(input_frame, text="Sapa", command=lambda: showinfo("Info", f"Halo {NAMA_DEPAN.get()}"))
tombol_sapa.pack(padx=10, pady=10, fill='x', expand=True)
window.mainloop()

