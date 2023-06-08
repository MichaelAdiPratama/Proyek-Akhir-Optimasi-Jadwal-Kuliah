
import random
import pandas as pd
from tkinter import *
from tkinter import messagebox



jadwal_kuliah = []


def tambah_jadwal():
    start_time = int(start_time_entry.get())
    end_time = int(end_time_entry.get())
    nama_dosen = nama_dosen_entry.get()
    mata_kuliah = mata_kuliah_entry.get()
    bobot_sks = int (bobot_sks_entry.get())
    ruangan = ruangan_entry.get()
    hari = hari_var.get()
    jadwal_kuliah.append([hari,mata_kuliah,nama_dosen,start_time, end_time, ruangan,bobot_sks])
    data_jadwal = pd.DataFrame(jadwal_kuliah,columns=["Hari", "Mata Kuliah","Nama Dosen", "Jam Mulai", "Jam Selesai", "Ruangan", "SKS"])
    jadwal_text.delete(1.0,END)
    jadwal_text.insert(END,data_jadwal.to_string(index=False))


def hapus_jadwal():
    if not jadwal_kuliah:
        messagebox.showinfo("Warning!","Tidak ada jadwal kuliah yang dapat dihapus!")
    else:
        jadwal_kuliah.pop()
        data_jadwal = pd.DataFrame(jadwal_kuliah,columns=["Hari", "Mata Kuliah","Nama Dosen", "Jam Mulai", "Jam Selesai", "Ruangan", "SKS"])
        jadwal_text.delete(1.0,END)
        jadwal_text.insert(END, data_jadwal.to_string(index=False))


def parent_selection(population):
    tournament_size = 3
    parent = []
    for _ in range(2):
        turnamen = random.sample(population, tournament_size)
        turnamen.sort(key=lambda x: evaluasi_fitness(x), reverse=True)
        parent.append(turnamen[0])
    return parent



def rekombinasi(parent):
    crossover_point = random.randint(1, len(jadwal_kuliah) - 1)
    child = []
    child.append(parent[0][:crossover_point] + parent[1][crossover_point:])
    child.append(parent[1][:crossover_point] + parent[0][crossover_point:])
    return child


def mutasi(child):
    for i in range(len(child)):
        if random.random() < 0.1:
            gen1 = random.randint(0, len(jadwal_kuliah) - 1)
            gen2 = random.randint(0, len(jadwal_kuliah) - 1)
            child[i][gen1], child[i][gen2] = child[i][gen2], child[i][gen1]
    return child


def genetic_algorithm(sum_generation, trace=False):
    population = inisialisasi_populasi(10)
    for generasi in range(sum_generation):
        new_population = []
        for _ in range(len(population) // 2):
            parent = parent_selection(population)
            child = rekombinasi(parent)
            child_mutate = mutasi(child)
            new_population.extend(child_mutate)
            if trace:
                print(f"\nGenerasi {generasi+1} - Crossover:  \n\nParent (0)\n\n {parent[0]} & \n\n Parent(1)\n\n {parent[1]} \n")
                print(f"\nGenerasi {generasi+1} - Mutasi:  Child mutate\n\n {child_mutate}\n")
        population = new_population

    population.sort(key=lambda x: evaluasi_fitness(x), reverse=True)
    return population[0]


def optimasi_jadwal():
    sum_generation = int(generations_entry.get())
    if len(jadwal_kuliah) < 2:
        messagebox.showinfo("Warning", "Minimal terdapat 2 jadwal kuliah untuk optimasi Jadwal!!!")

    else:
        jadwal_terbaik = genetic_algorithm(sum_generation, trace=True)
        tampilkan_jadwal_gui(jadwal_terbaik)


def evaluasi_fitness(kromosom):
    fitness_point = 0
    for i in range(len(kromosom)):
        for j in range(i + 1, len(kromosom)):
            if (kromosom[i][0] <= kromosom[j][0] < kromosom[i][1] or \
                kromosom[j][0] <= kromosom[i][0] < kromosom[j][1]) and \
                    kromosom[i][6] == kromosom[j][6]:
                fitness_point -= 1
    return fitness_point


def inisialisasi_populasi(jumlah_kromosom):
    population = []
    for _ in range(jumlah_kromosom):
        kromosom = random.sample(jadwal_kuliah, len(jadwal_kuliah))
        population.append(kromosom)
    return population


def tampilkan_jadwal(schedule):
    data_jadwal = pd.DataFrame(schedule, columns=["Hari", "Mata Kuliah","Nama Dosen", "Jam Mulai", "Jam Selesai", "Ruangan", "SKS"])
    return data_jadwal.to_string(index=False)


def tampilkan_jadwal_per_hari(schedule):
    schedule_every_day = {}
    for schedule_item in schedule:
        day = schedule_item[6]
        if day not in schedule_every_day:
            schedule_every_day[day] = []
        schedule_every_day[day].append(schedule_item)
    return schedule_every_day


def tampilkan_jadwal_gui(schedule):
    schedule_every_day = tampilkan_jadwal_per_hari(schedule)
    jadwal_text.delete(1.0, END)
    for day, schedule_items in schedule_every_day.items():
        data_jadwal = pd.DataFrame(schedule_items, columns=["Hari", "Mata Kuliah","Nama Dosen", "Jam Mulai", "Jam Selesai", "Ruangan", "SKS"])
        jadwal_text.insert(END, f"Hari: {day}\n")
        jadwal_text.insert(END, data_jadwal.to_string(index=False))
        jadwal_text.insert(END, "\n\n")



root = Tk()
root.title("Optimasi Jadwal Kuliah")
root.geometry("600x500")

input_frame = Frame(root)
input_frame.pack(pady=10)


root.configure(bg="#F0F0F0")
tambah_button_color = "#008080"
hapus_button_color = "#FF4500"
generate_button_color = "#006400"


label_bg_color = "#F0F0F0"
label_fg_color = "#000000"
text_bg_color = "#FFFFFF"
text_fg_color = "#000000"

start_time_label = Label(input_frame, text="Jam Mulai (HH:MM):")
start_time_label.grid(row=0, column=0)

start_time_entry = Entry(input_frame)
start_time_entry.grid(row=0, column=1)

end_time_label = Label(input_frame, text="Jam Selesai (HH:MM):")
end_time_label.grid(row=0, column=2)

end_time_entry = Entry(input_frame)
end_time_entry.grid(row=0, column=3)

nama_dosen_label = Label(input_frame, text="Nama Dosen:")
nama_dosen_label.grid(row=1, column=0)

nama_dosen_entry = Entry(input_frame)
nama_dosen_entry.grid(row=1, column=1)

mata_kuliah_label = Label(input_frame, text="Mata Kuliah:")
mata_kuliah_label.grid(row=1, column=2)

mata_kuliah_entry = Entry(input_frame)
mata_kuliah_entry.grid(row=1, column=3)

bobot_sks_label = Label(input_frame, text="Jumlah SKS:")
bobot_sks_label.grid(row=2, column=0)

bobot_sks_entry = Entry(input_frame)
bobot_sks_entry.grid(row=2, column=1)

ruangan_label = Label(input_frame, text="Ruangan:")
ruangan_label.grid(row=2, column=2)

ruangan_entry = Entry(input_frame)
ruangan_entry.grid(row=2, column=3)

hari_label = Label(input_frame, text="Hari:")
hari_label.grid(row=3, column=0)

hari_var = StringVar(root)
hari_var.set("Senin")  

hari_option_menu = OptionMenu(input_frame, hari_var, "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu")
hari_option_menu.grid(row=3, column=1)

button_frame = Frame(root)
button_frame.pack(pady=5)

tambah_button = Button(button_frame, text="Tambah Jadwal", command=tambah_jadwal,bg=tambah_button_color, fg=text_fg_color)
tambah_button.pack(side=LEFT)

hapus_button = Button(button_frame, text="Hapus Jadwal Terakhir", command=hapus_jadwal,bg=hapus_button_color, fg=text_fg_color)
hapus_button.pack(side=LEFT)

jadwal_frame = Frame(root)
jadwal_frame.pack(pady=10)

jadwal_text = Text(jadwal_frame, height=15, width=90)
jadwal_text.pack()

generations_label = Label(root, text="Jumlah Generasi:")
generations_label.pack()

generations_entry = Entry(root)
generations_entry.pack()

optimasi_button = Button(root, text="Optimasi Jadwal", command=optimasi_jadwal)
optimasi_button.pack()

root.mainloop()
