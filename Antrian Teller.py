import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

antrian_tl = []
antrian_cs = []
antrian_cb = []
nomor_teller = 1
nomor_cs = 1
nomor_cb = 1

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
