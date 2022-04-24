print('''
        ********** LIHAT HARGA TIKET BUS **********
          **********  E-NEW  SHANTIKA  **********
''')
print('''
Daftar Destinasi
1. jakarta-bandung
2. jakarta-surabaya
3. jakarta-bali
4. jakarta-semarang ''')

Destinasi = str(input("Masukkan Destinasi yang akan anda tuju : "))
if Destinasi == "jakarta-bandung":
    DataMobil = ["Daytrans                      ", "Baraya Travel                 ", "Jackal Holiday Premium Shuttle", "Priangan Intercity Travel     ", "XTrans                        "]
    DataHarga = ["85000 " , "99000 ", "125000" , "125000", "125000"]
    DataDestinasi = ["Setiap hari", "Setiap hari", "Setiap hari", "Setiap hari", "Setiap hari"]

    print('''
-----------------------------------------------------------------------
| Daftar Mobil                       Daftar Harga         Daftar Hari |
-----------------------------------------------------------------------''')
      
    for x in range(len(DataMobil)):
        isi = str(DataMobil[x])
        print("| " + isi, end = "      ")
        for y in range(25 - 15 - len(isi)):
            print(" ", end = "")
        
        isi1 = str(DataHarga[x])
        print("RP." + isi1, end = "")
        for y in range(12 - 5 - len(isi1)):
            print(" ", end = "          ")
        
        isi2 = str(DataDestinasi[x])
        print("" + isi2, end = "")
        for y in range(10 - 3 - len(isi2)):
            print(" ", end = " ")
        print(" |")
    print("-----------------------------------------------------------------------")
    
elif Destinasi == "jakarta-surabaya":
    DataMobil = ["PO Mawar          "]
    DataHarga = ["270000"]
    DataDestinasi = ["Setiap hari"]

    print('''
-----------------------------------------------------------
| Daftar Mobil            Daftar Harga        Daftar Hari |
-----------------------------------------------------------''')
      
    for x in range(len(DataMobil)):
        isi = str(DataMobil[x])
        print("| " + isi, end = "      ")
        for y in range(25 - 15 - len(isi)):
            print(" ", end = "")
        
        isi1 = str(DataHarga[x])
        print("RP." + isi1, end = "")
        for y in range(12 - 5 - len(isi1)):
            print(" ", end = "          ")
        
        isi2 = str(DataDestinasi[x])
        print("" + isi2, end = "")
        for y in range(10 - 3 - len(isi2)):
            print(" ", end = " ")
        print(" |")
    print("-----------------------------------------------------------")


elif Destinasi == "jakarta-bali":
    DataMobil = ["PO Tiara Mas                 ", "Kramat Djati Jakarta         ", "Pahala Kencana               ", "PT MITRA TITIAN NUSANTARA    "]
    DataHarga = ["450000" , "550000", "700000" , "900000"]
    DataDestinasi = ["Setiap hari", "Setiap hari", "Setiap hari", "Setiap hari"]

    print('''
----------------------------------------------------------------------
| Daftar Mobil                       Daftar Harga        Daftar Hari |
----------------------------------------------------------------------''')
      
    for x in range(len(DataMobil)):
        isi = str(DataMobil[x])
        print("| " + isi, end = "      ")
        for y in range(25 - 15 - len(isi)):
            print(" ", end = "")
        
        isi1 = str(DataHarga[x])
        print("RP." + isi1, end = "")
        for y in range(12 - 5 - len(isi1)):
            print(" ", end = "          ")
        
        isi2 = str(DataDestinasi[x])
        print("" + isi2, end = "")
        for y in range(10 - 3 - len(isi2)):
            print(" ", end = " ")
        print(" |")
    print("-----------------------------------------------------------------------")

elif Destinasi == "jakarta-semarang":
    DataMobil = ["PO Trans Zentrum                ", "Janur Renda Travel              ", "Gema Pratama Trans Tour n Travel", "Daytrans                        ", "Lestari Transport               "]
    DataHarga = ["180000" , "320000", "450000" , "450000", "630000"]
    DataDestinasi = ["Setiap hari", "Setiap hari", "Setiap hari", "Setiap hari", "Setiap hari"]

    print('''
-----------------------------------------------------------------------
| Daftar Mobil                          Daftar Harga        Daftar Hari |
-----------------------------------------------------------------------''')
      
    for x in range(len(DataMobil)):
        isi = str(DataMobil[x])
        print("| " + isi, end = "      ")
        for y in range(25 - 15 - len(isi)):
            print(" ", end = "")
        
        isi1 = str(DataHarga[x])
        print("RP." + isi1, end = "")
        for y in range(12 - 5 - len(isi1)):
            print(" ", end = "          ")
        
        isi2 = str(DataDestinasi[x])
        print("" + isi2, end = "")
        for y in range(10 - 3 - len(isi2)):
            print(" ", end = " ")
        print(" |")
    print("-----------------------------------------------------------------------")
    
else :
    print("Destinasi tidak Ada")
