import csv
from datetime import datetime

class Rekins:
    def __init__(self,klients,veltijums,izmers,materials):
        self.klients = klients
        self.veltijums=veltijums
        self.izmers=izmers #platums,garums,augstums
        self.materials=materials
        self.laiks= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.darba_samaksa = 15
        self.PVN = 21
        #self.summa=0 #apreķinās vēlāk, izsaucot aprekins()
        self.summa=self.aprekins() #aprēķinās pēc objekta izveindošanas, pamatojoties uz citiem parametriem

    def aprekins(self):#self atsaucas uz pašreizējo objektu, tātad uz visies atribūtiem, kas tam piejami
        #"izpakot" izmērus
        platums, garums, augstums = self.izmers
        veltijuma_garums=len(self.veltijums)
        produkta_cena= (veltijuma_garums*1.20)+(platums/100*garums/100*augstums/100)/3*self.materials
        PVN_summa=(produkta_cena+self.darba_samaksa)*self.PVN/100
        rekina_summa =(produkta_cena+self.darba_samaksa)+PVN_summa 
        return round(rekina_summa,2)

    def izdruka(self):
        print(f"RĒĶINS\nIzdrukas laiks: {self.laiks}\n Rēķins: \n Klients: {self.klients}\n Veltījums: {self.veltijums}\n Izmēri(mm): platums{self.izmers[0]}, garums {self.izmers[1]}, augstums{self.izmers[2]}\n Materiālu cena:(eur/cm^3) {self.materials}\n Darba samaksa: {self.darba_samaksa}EUR\n PVN: {self.PVN}% \n Kopējā summa: {self.summa} EUR")

    def saglabat(self):
        datnes_nosaukums=f"rekins_{self.klients}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(datnes_nosaukums, 'w',newline='',encoding='utf8') as fails:
            writer=csv.writer(fails)
            writer.writerow(["Izveidošanas laiks","Klients","Veltījums","Izmērs","Cena (EUR/m^2)","PVN (%)","Summa (EUR)"])
            writer.writerow([self.laiks,self.klients,self.veltijums,
                            f"{self.izmers[0]}x{self.izmers[1]}x{self.izmers[2]}",
                            self.materials,self.darba_samaksa,self.summa])
            print(f"Rēķins saglabāts failā :{datnes_nosaukums}")

klients=input("Klients: ")
veltijums=input("Veltījums: ")
platums=int(input("Ievadiet platumu: "))
garums=int(input("Ievadiet garumu: "))
augstums=int(input("Ievadiet augstumu: "))
materials=float(input("Lūdzu ievadiet materiāla cenu (eur/cm^3): "))  

#jauna rēķina objekta izveidošana

rekins=Rekins(klients,veltijums,[platums,garums,augstums],materials)
#saglabāt un izdrukāt rēķinu
rekins.saglabat()
rekins.izdruka()
#rekins.aprekins() - ja pie laukiem liek, ka summa = 0