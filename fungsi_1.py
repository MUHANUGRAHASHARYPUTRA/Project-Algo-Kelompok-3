import calendar

nama_bulan = {
    "januari": 1,
    "februari": 2,
    "maret": 3,
    "april": 4,
    "mei": 5,
    "juni": 6,
    "juli": 7,
    "agustus": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "desember": 12
}

tahun = int(input("Masukkan tahun: "))
inputan_bulan = input("Masukkan nama bulan atau angka bulan (1-12) : ")

if inputan_bulan.isdigit():
    bulan = int(inputan_bulan)
   
    if 1 <= bulan <= 12:
        kal = calendar.month(tahun, bulan)
        print(kal)
    else:
        print("Bulan tidak valid. Silakan masukkan angka antara 1 dan 12.")
else:
    inputan_bulan = inputan_bulan.lower()
    if inputan_bulan in nama_bulan:
        bulan = nama_bulan[inputan_bulan]
        
        kal = calendar.month(tahun, bulan)
        print(kal)
    else:
        print("Nama bulan tidak valid. Silakan coba lagi.")