class Viesis:
    def __init__(self,vards,parole):
        self.vards=vards
        self.parole=parole

    #izdrukā info par izveidotu lietotaju
    def druka_vardu(self):
        print("Lietotājs:",self.vards,"izveidots")
    
    def parbauda_paroli(self,parole):
        #pārbauda, vai parole sakrīt
        if self.parole == parole:
            print("Lietotāja:",self.vards,"parole ir pareiza.")
        else:
            print("Parole nav pareiza!")

#klase Darbinieks manto no Viesis
#metode druka_vardu izprintē info par administratoru

class Darbinieks(Viesis):
    def __init__(self, vards, parole):
        super().__init__(vards, parole)

    def druka_vardu(self):
        print("Administrators",self.vards,"izveidots")

#Testa dati
vards1="Valdis"
parole1="dators2"

vards2="Daina"
parole2="monitors2"

#izveidot objektu klasei Viesis un izsaukt metodes

objekts1 = Viesis(vards1,parole1)
objekts1.druka_vardu()
objekts1.parbauda_paroli(parole1)

objekts2 = Darbinieks(vards2,parole2)
objekts2.druka_vardu()
objekts2.parbauda_paroli(parole2)