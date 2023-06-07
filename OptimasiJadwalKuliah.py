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


def seleksi_orang_tua(populasi):
    ukuran_turnamen = 3
    orang_tua = []
    for _ in range(2):
        turnamen = random.sample(populasi, ukuran_turnamen)
        turnamen.sort(key=lambda x: evaluasi_fitness(x), reverse=True)
        orang_tua.append(turnamen[0])
    return orang_tua

def mutasi(anak):
    for i in range(len(anak)):
        if random.random() < 0.1:
            gen1 = random.randint(0, len(jadwal_kuliah) - 1)
            gen2 = random.randint(0, len(jadwal_kuliah) - 1)
            anak[i][gen1], anak[i][gen2] = anak[i][gen2], anak[i][gen1]
    return anak

# Algoritma genetika
def genetic_algorithm(jumlah_generasi, trace=False):
    populasi = inisialisasi_populasi(10)
    for generasi in range(jumlah_generasi):
        populasi_baru = []
        for _ in range(len(populasi) // 2):
            orang_tua = seleksi_orang_tua(populasi)
            anak = rekombinasi(orang_tua)
            anak_mutasi = mutasi(anak)
            populasi_baru.extend(anak_mutasi)
            if trace:
                print(f"Generasi {generasi+1} - Crossover: {orang_tua[0]} & {orang_tua[1]}")
                print(f"Generasi {generasi+1} - Mutasi: {anak_mutasi}")
        populasi = populasi_baru

    populasi.sort(key=lambda x: evaluasi_fitness(x), reverse=True)
    return populasi[0]


# Fungsi untuk menjalankan optimasi jadwal dengan metode Genetic Algorithm
def optimasi_jadwal():
    jumlah_generasi = int(generations_entry.get())
    if len(jadwal_kuliah) >= 2:
        jadwal_terbaik = genetic_algorithm(jumlah_generasi, trace=True)
        tampilkan_jadwal_gui(jadwal_terbaik)
    else:
        messagebox.showinfo("Peringatan", "Minimal harus ada 2 jadwal kuliah untuk melakukan optimasi.")



wkwkkwkw
