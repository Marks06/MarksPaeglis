from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self,vards,epasts):
        self.vards = vards
        self.epasts = f"<{epasts}>"
    def info(self):
        return self.vards + " " + self.epasts
class Vestule(ABC):
    @abstractmethod
    def __init__(self, sutitajs,sanemejs,saturs) :
        self.sutitajs = sutitajs
        self.sanemejs = sanemejs
        self.saturs = saturs
class VestulesSuta(Vestule):
    
    def sutit_vestuli(self):
        pass
    def sanemt_vestuli(self):
        pass
class Pastnieks(VestulesSuta):
    def __init__(self, sutitajs, sanemejs, saturs):
        super().__init__(sutitajs, sanemejs, saturs)

    
    def sutit_vestuli(self):
        print(f"✉\nVēstule no: {self.sutitajs}")
        print(f'Vestule uz: {self.sanemejs}')
        print("Saturs: Sveiki, vai šodien esat darbā?")
        print("Vēstule nosūtīta ar pastnieka palīdzību.\n")
    def sanemt_vestuli(self):
        print(f"Vēstule saņemta no: {self.sutitajs}")
        print(f'Vestule adresēta uz: {self.sanemejs}')
        print("Saturs: Sveiki, vai šodien esat darbā?\n✉")

janis = Persona("Jānis Zibens", "zibens.sper@svg.lv")
zane = Persona("Zane Puķe", "pukes.zied@svg.lv")


vestule = Pastnieks(janis.info(), zane.info(), "Sveiki, vai šodien esat darbā?")

vestule.sutit_vestuli()
vestule.sanemt_vestuli()