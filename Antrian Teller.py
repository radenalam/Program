import tkinter as tk

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


teller = tk.Button(main_window, text="Teller", command=cetak_antrian_teller)
teller.pack()
teller.place(x = 20, y = 50)

cs = tk.Button(main_window, text="Custumer Service")
cs.pack()
cs.place(x = 150, y = 50)

buku = tk.Button(main_window, text="Cetak Buku")
buku.pack()
buku.place(x = 300, y = 50)

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