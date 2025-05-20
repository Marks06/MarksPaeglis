#bāzes klases Persona ar laukiem vārds,vecums un metodi, kas šos datus izdrukā
class Persona():
    def __init__(self,vards,vecums):
        self.vards=vards
        self.vecums=vecums
    def izdruka(self):
        print("Vārds: ",self.vards, "Vecums: ",self.vecums)

#atvasinātā klase students, kas manto abus divus laukus un pievieno specifisko lauku "kurss"
class Students(Persona):
    def __init__(self, vards, vecums,kurss):
        super().__init__(vards, vecums)
        self.kurss=kurss
        #metodes pārrakstīšana
    def izdruka(self):
        super().izdruka()
        print('Kurss: ',self.kurss)

#izveidot katrai klasei vienu objektu

persona1=Persona("Centis",35)
persona1.izdruka()

students1=Students("Santīms",20,2)
students1.izdruka()

super(Students,students1).izdruka()