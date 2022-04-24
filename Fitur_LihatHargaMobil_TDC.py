def lihathargabus():
    print('''
        ********** LIHAT HARGA TIKET BUS **********
          **********  E-NEW  SHANTIKA  **********
''')
    print('''
    Daftar Destinasi
    1. jakarta-bandung
    2. jakarta-surabaya
    3. jakarta-bali
    4. jakarta-semarang''')

    Destinasi = int(input("Masukkan Destinasi yang akan anda tuju (Sesuai angka) : "))
    if Destinasi == 1:
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
        kembali = str(input("Kembali Ke Menu utama? (yes/no) : "))
        if kembali == "yes":
            lihathargabus()
        else:
            print("***********TERIMAKASIH***********")
    elif Destinasi == 2:
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
        kembali = str(input("Kembali Ke Menu utama? (yes/no) : "))
        if kembali == "yes":
            lihathargabus()
        else:
            print("***********TERIMAKASIH***********")

    elif Destinasi == 3:
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
        kembali = str(input("Kembali Ke Menu utama? (yes/no) : "))
        if kembali == "yes":
            lihathargabus()
        else:
            print("***********TERIMAKASIH***********")
    elif Destinasi == 4:
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
        kembali = str(input("Kembali Ke Menu utama? (yes/no) : "))
        if kembali == "yes":
            lihathargabus()
        else:
            print("***********TERIMAKASIH***********")
    else :
        print("Destinasi tidak Ada")
    return
lihathargabus()
