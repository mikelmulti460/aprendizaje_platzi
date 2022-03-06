from uberBlack import UberBlack
from uberPool import UberPool
from account import Account

if __name__ == "__main__":
    car = UberBlack("AMR15647", Account("mikel Aranda","4hg39i1r"), "ToyotaYaris", "Plastilina")
    car.printCarData()

    car = UberPool("AMR185", Account("Danna","awfa489"), "HotWeels", "Papel Crepé")
    car.printCarData()