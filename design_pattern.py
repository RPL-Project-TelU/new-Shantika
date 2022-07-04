#Jahfal Mudrik Ramadhan 1302204034
#factory method
#the shantika interface
from abc import ABCMeta, abstractmethod
#The bus_database Interface
class bus_database(metaclass=ABCMeta):
    @abstractmethod
    def bus_database():
        #An abstract interface method
        "new Shantika"
#Kelas konkret(nyata) cari_bus yang mengimplementasikan interface shantika
class tambah_bus():
    def __init__(self):
        self.nama = "Jahfal"
        self.kontak = "0812"
        self.alamat = "Bekasi"
        self.Operator = "Shantika"
        self.TipeBus = "Non AC"
        self.KotaAsal = "Bekasi"
        self.KotaTujuan = "Bandung"
        self.WaktuBerangkat = 7
        self.WaktuSampai = 10
        self.Tarif = 100000
        self.Bangku = 20
    
    def busdatabase(self):
        return {"Nama": self.nama, "Kontak": self.kontak, "Alamat": self.alamat, 
        "Operator": self.Operator, "Tipe Bus": self.TipeBus, "Kota Asal": self.KotaAsal, 
        "Kota Tujuan": self.KotaTujuan, "Waktu Berangkat": self.WaktuBerangkat, 
        "Waktu Sampai": self.WaktuSampai, "Harga": self.Tarif, "Bangku": self.Bangku}

#Kelas konkret(nyata) cari_bus yang mengimplementasikan interface shantika
class cari_bus():
    def __init__(self):
        self.Operator = "Shantika"
        self.TipeBus = "Non AC"
        self.KotaAsal = "Bekasi"
        self.KotaTujuan = "Bandung"
        self.WaktuBerangkat = 7
        self.WaktuSampai = 9
        self.Tarif = 100000
        self.Bangku = 20
    
    def busdatabase(self):
        return {"Operator": self.Operator, "Tipe Bus": self.TipeBus, "Kota Asal": self.KotaAsal, 
        "Kota Tujuan": self.KotaTujuan, "Waktu Berangkat": self.WaktuBerangkat, 
        "Waktu Sampai": self.WaktuSampai, "Harga": self.Tarif, "Bangku": self.Bangku}

#The Factory Class
class shantika():
    @staticmethod
    #A static method to get a database
    def getdatabase(database):
        try:
            if database == "tambah_bus":
                return tambah_bus()
            elif database == "cari_bus":
                return cari_bus()
            raise AssertionError("not found")
        except AssertionError as _e:
            print(_e)
            
class log_in:
    username = input("Username: ")
    password = input("Password: ")
    if username == "jahfal" and password == "123":
        print("LogIn Berhasil")
        if __name__ == "__main__":
            bus = shantika.getdatabase("tambah_bus")
            print(f"tambah_bus: {bus.busdatabase()}")
            print("")
            bus = shantika.getdatabase("cari_bus")
            print(f"cari_bus: {bus.busdatabase()}")
    else:
        print("Username dan Password Salah")