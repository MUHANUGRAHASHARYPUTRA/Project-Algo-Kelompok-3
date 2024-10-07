from datetime import date

def hari_libur_nasional(tahun, bulan):
    hari_libur = {
        date(tahun, 1, 1): "Tahun Baru 2024",
        date(tahun, 2, 8): "Isra Mi’raj Nabi Muhammad SAW",
        date(tahun, 3, 11): "Cuti Bersama Tahun Baru Imlek",
        date(tahun, 4, 10): "Tahun Baru Imlek 2575 Kongzili",
        date(tahun, 5, 1): "Hari Suci Nyepi Tahun Baru Saka 1946",
        date(tahun, 5, 9): "Cuti Bersama Hari Suci Nyepi Tahun Baru Saka 1946",
        date(tahun, 5, 23): "Wafat Isa Almasih",
        date(tahun, 6, 1): "Cuti Bersama Idul Fitri 1445 Hijriah",
        date(tahun, 8, 17): "Hari Kemerdekaan RI",
        date(tahun, 9, 16): "Hari Raya Idul Fitri 1445 Hijriah",
        date(tahun, 12, 25): "Hari Raya Natal",
        date(tahun, 12, 26): "Cuti Bersama Hari Raya Natal"
    }

    return {tanggal: keterangan for tanggal, keterangan in hari_libur.items() if tanggal.month == bulan}

tahun = 2024  
for bulan in range(1, 13):
    libur_bulan_ini = hari_libur_nasional(tahun, bulan)
    print(f"Hari libur di bulan {bulan} {tahun}:")
    
    if libur_bulan_ini:
        for tanggal, keterangan in libur_bulan_ini.items():
            print(f"{tanggal}: {keterangan}")
    else:
        print("Tidak ada hari libur nasional di bulan ini.")
    
    print()
