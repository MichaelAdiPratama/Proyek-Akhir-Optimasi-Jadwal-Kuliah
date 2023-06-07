# import library
import random
import pandas as pd
from tkinter import *
from tkinter import messagebox
import datetime as dt

# Inisiasi array Jadwal Kuliah
jadwal_kuliah = []

# fungsi add jadwal kuliah untuk menambahkan jadwal kuliah:
def tambah_jadwal():
    jam_mulai = int(jam_mulai_entry.get())
    jam_selesai = int(jam_selesai_entry.get())
    nama_dosen = nama_dosen_entry.get()
    mata_kuliah = mata_kuliah_entry.get()
    sks = int (sks_entry.get())
    ruangan = ruangan_entry.get()
    hari = hari_var.get()
    jadwal_kuliah.append([hari,mata_kuliah,nama_dosen,jam_mulai, jam_selesai, ruangan,sks])
    jadwal_df = pd.DataFrame(jadwal_kuliah,columns=["Jam Mulai", "Jam Selesai", "Nama Dosen", "Mata Kuliah", "SKS", "Ruangan", "Hari"])
    jadwal_text.delete(1.0,END)
    jadwal_text.insert(END,jadwal_df.to_string(index=False))

# fungsi hapus jadwal kuliah terakhir:
def hapus_jadwal():
    if jadwal_kuliah:
        jadwal_kuliah.pop()
        jadwal_df = pd.DataFrame(jadwal_kuliah,columns=["Hari", "Mata Kuliah","Nama Dosen", "Jam Mulai", "Jam Selesai", "Ruangan", "SKS"])
        jadwal_text.delete(1.0,END)
        jadwal_text.insert(END, jadwal_df.to_string(index=False))
    else:
        messagebox.showinfo("Peringatan","Tidak ada jadwal kuliah yang dapat dihapus!")








# Fungsi untuk menjalankan optimasi jadwal dengan metode Genetic Algorithm
def optimasi_jadwal():
    jumlah_generasi = int(generations_entry.get())
    if len(jadwal_kuliah) >= 2:
        jadwal_terbaik = genetic_algorithm(jumlah_generasi, trace=True)
        tampilkan_jadwal_gui(jadwal_terbaik)
    else:
        messagebox.showinfo("Peringatan", "Minimal harus ada 2 jadwal kuliah untuk melakukan optimasi.")