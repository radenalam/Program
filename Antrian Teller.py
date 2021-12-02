import tkinter as tk
from tkinter import*
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,Border,Side
from tkinter import font as tkfont

antrian_tl = []
antrian_cs = []
antrian_cb = []
nomor_teller = 1
nomor_cs = 1
nomor_cb = 1



def cetak_antrian_teller():
	nomor_teller_tl = 'T' + str(nomor_teller)
	antrian_tl.append(nomor_teller)
	nomor_teller +=1
	antriansekarang.set(nomor_teller_tl)
	label2.config(font=('Helvetica', 15, "bold"), fg="red")

def cetak_antrian_cs():
	nomor_teller_cs = 'CS' + str(nomor_cs)
	antrian_cs.append(nomor_cs)
	nomor_cs +=1
	print(" ")
	print("Nomor antrian Teller :" + nomor_teller_cs )
	print(" ")

def cetak_buku():
	nomor_teller_cb = 'CB' + str(nomor_cb)
	antrian_cb.append(nomor_cb)
	nomor_cb +=1
	print(" ")
	print("Nomor antrian Teller :" + nomor_teller_cb )
	print(" ")

main_window = tk.Tk()
main_window.title("BANK Yogyakarta")
main_window.geometry("600x300")

label = tk.Label(main_window, text="Selamat Datang di Bank")
label.pack()

frameNama = Frame(main_window, bg='white')
frameNama.place(rely=0.24,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
namainfo = Label(frameNama, bg='white', text='Nama')
namainfo.place(relwidth=0.5,relheight=1)
namaEntry = Entry(frameNama)
namaEntry.place(relx=0.5,relheight=1,relwidth=0.5)

frameJenisKelamin = Frame(main_window, bg='white')
frameJenisKelamin.place(rely=0.31,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
jeniskelamininfo = Label(frameJenisKelamin, bg='white', text='Jenis Kelamin')
jeniskelamininfo.place(relwidth=0.5,relheight=1)
jeniskelaminEntry = Entry(frameJenisKelamin)
jeniskelaminEntry.place(relx=0.5,relheight=1,relwidth=0.5)

framePekerjaan = Frame(main_window, bg='white')
framePekerjaan.place(rely=0.38,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
pekerjaaninfo = Label(framePekerjaan, bg='white', text='Pekerjaan')
pekerjaaninfo.place(relwidth=0.5,relheight=1)
pekerjaanEntry = Entry(framePekerjaan)
pekerjaanEntry.place(relx=0.5,relheight=1,relwidth=0.5)

frameNomorPonsel = Frame(main_window, bg='white')
frameNomorPonsel.place(rely=0.45,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
nomorponselinfo = Label(frameNomorPonsel, bg='white', text='Nomor Ponsel')
nomorponselinfo.place(relwidth=0.5,relheight=1)
nomorponselEntry = Entry(frameNomorPonsel)
nomorponselEntry.place(relx=0.5,relheight=1,relwidth=0.5)

frameAlamat = Frame(main_window, bg='white')
frameAlamat.place(rely=0.52,relx=0.5,relheight=0.06,relwidth=0.65,anchor='n')
alamatinfo = Label(frameAlamat, bg='white', text='Alamat')
alamatinfo.place(relwidth=0.5,relheight=1)
alamatEntry = Entry(frameAlamat)
alamatEntry.place(relx=0.5,relheight=1,relwidth=0.5)

teller = tk.Button(main_window, text="Teller", command=cetak_antrian_teller)
teller.pack()
teller.place(x = 100, y = 250)

cs = tk.Button(main_window, text="Custumer Service")
cs.pack()
cs.place(x = 300, y = 250)

buku = tk.Button(main_window, text="Cetak Buku")
buku.pack()
buku.place(x = 450, y = 250)

antriansekarang = tk.StringVar()
antriansekarang.set("0")
label2 = tk.Label(main_window, font=('Helvetica', 12, "bold"), textvariable=antriansekarang)
label2.pack()

main_window.mainloop()


""""
while True:
		print("SELAMAT DATANG DI BANK")
		print("1.Cetak antrian Teller")
		print("2.Cetak antrian CS")
		print("3.Cetak buku")
		a = int(input("Silahkan pilih menu : "))
		if a == 1:
			#membuat kode tiket tellet dengan diawali kode T
			nomor_teller_tl = 'T' + str(nomor_teller)
			antrian_tl.append(nomor_teller)
			nomor_teller +=1
			#cek nomor antrian
			print(" ")
			print("Nomor antrian Teller :" + nomor_teller_tl )
			print(" ")
			
		elif a == 2:
			nomor_teller_cs = 'CS' + str(nomor_cs)
			antrian_cs.append(nomor_cs)
			nomor_cs +=1
			#cek nomor antrian
			print(" ")
			print("Nomor antrian Teller :" + nomor_teller_cs )
			print(" ")
			
		elif a == 3:
			nomor_teller_cb = 'CB' + str(nomor_cb)
			antrian_cb.append(nomor_cb)
			nomor_cb +=1
			#cek nomor antrian
			print(" ")
			print("Nomor antrian Teller :" + nomor_teller_cb )
			print(" ")
			
		else:
			print("pilihan tidak tersedia")
			break
"""