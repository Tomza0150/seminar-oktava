#!/usr/bin/env python3

class Arena:
    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self.bojovnik_1 = bojovnik_1
        self.bojovnik_2 = bojovnik_2
        self.kostka = kostka
    
    def _vykresli(self):
        print("----------------Arena---------------- \n")
        print("Bojovnici: \n")
        self._vypis_bojovnika(self.bojovnik_1)
        self._vypis_bojovnika(self.bojovnik_2)

    def _vycisti(self):
            import sys as _sys
            import subprocess as _subprocess
            import time as _time
            _time.sleep(0.5)
            if _sys.platform.startswith("win"):
                _subprocess.call(["cmd.exe", "/C", "cls"])
            else:
                _subprocess.call(["clear"])


    def _vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f"Zivot: {bojovnik.graficky_zivot()}")
        if isinstance(bojovnik, Mag):
            print(f"Mana: {bojovnik.graficka_mana()}")

    def _vypis_zpravu(self, zprava):
        print()
        print(zprava)
        import time as _time
        _time.sleep(0.75)
    
    def zapas(self):
        print("Vítejte v Areně!")
        print(f"Dnes se utkají {self.bojovnik_1} a {self.bojovnik_2}!")
        print("Zápas může začít...", end="")

        import random as _random
        if _random.randint(0,1):
            self.bojovnik_1, self.bojovnik_2 = self.bojovnik_2, self.bojovnik_1

        while self.bojovnik_1.nazivu and self.bojovnik_2.nazivu:




            self.bojovnik_1.utoc(self.bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self.bojovnik_2.get_zprava())
            if self.bojovnik_2.nazivu:
                self.bojovnik_2.utoc(self.bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self.bojovnik_1.get_zprava())

if __name__ == "__main__":
    from kostka import Kostka
    from Bojovník import Bojovnik
    from Bojovník import Mag
    k = Kostka(10)
    b1 = Bojovnik("Honza", 100, 20, 10, k)
    b2 = Mag("Jenik", 60, 18, 15, k, 40, 40)

    a = Arena(b1, b2, k)
    a.zapas()
