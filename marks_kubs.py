class Kubs:
    def __init__(self,krasa, malas_garums):
        self.malas_garums = malas_garums
        if self.malas_garums >= 2 and self.malas_garums <= 10: #pārbauda vai malas garums iekļaujas [2-10], ja nē, tad uzstāda vērtību 2
            self.malas_garums = malas_garums
        else:
            self.malas_garums = 2
        self.krasa = krasa

    def aprekinat_tilpumu(self):
        return round(self.malas_garums ** 3,1) #aprēķina tilpumu, un noapaļo līdz veselam skaitlim



class Bloks(Kubs):
    def __init__(self, krasa, malas_garums,forma,kubu_skaits):
        super().__init__(krasa, malas_garums) #manto no klases Kubs
        
        self.nosaukums = f"{krasa}{kubu_skaits}" #nosaukumu definēšana

        self.kubu_skaits = kubu_skaits
        if self.kubu_skaits >= 1 and self.kubu_skaits <= 4: #pārbauda vai kubs ir lielāks/vienās par 1 un mazāks/vienāds par 4, ja ir tad viss kārtībā
            self.kubu_skaits = kubu_skaits
        else:                                               #,bet ja nav, tad kubu skaits aiziet uz 1, un tiek paziņots ka Nepareiza kubu skaita vērtība
            print("Nepareiza kubu skaita vērtība!") 
            self.kubu_skaits = 1
            
        self.forma = forma
        iespejamas_vertibas = [11,12,13,14,22] #šīs ir tās derīgās formas vērtības
        if self.forma not in iespejamas_vertibas: #pārbauda vai self.forma (dotās formas vērtība) sakrīt šajās prasībās.
            self.forma = "nederīgs 0" #atgriež nederīgs 0  ,ja neatbilst
                
        else:
            self.forma ="derīgs 1" #atgriež derīgs 1 , ja atbilst

    def tilpums(self):
        return round(self.malas_garums**3* self.kubu_skaits,1) #aprēķina kopējo tilpumu visiem kubiem, noapaļojot to līdz veselam skaitlim

kubg=Kubs("Zaļa",10)
print("Dati par kubg objektu:")
print(f"Kubg krāsa un tilpums: {kubg.krasa} {kubg.aprekinat_tilpumu()}")
print(f"Kubg malas garums: {kubg.malas_garums}")
print("***")

kubr=Kubs("Sarkana",1)
print("Dati par kubr objektu:")
print(f"Kubr krāsa un tilpums: {kubr.krasa} {kubr.aprekinat_tilpumu()}")
print(f"Kubr malas garums: {kubr.malas_garums}")
print("***")

oranzs3 = Bloks("oranža",5,13,3)
print("Oranžs objekts:")
print(f"{oranzs3.nosaukums} {oranzs3.tilpums()} {oranzs3.forma}")
print("***")
print("Zils objekts:")
zils5 = Bloks("zila",7,23,5)

iespejamas_vertibas = [11,12,13,14,22]
if zils5.forma in iespejamas_vertibas:
    print(f"{zils5.nosaukums} {zils5.forma}") #pārbauda vai atbilst nosacijumiem
else:
    print("Forma neatbils nosacījumiem")
    print(f"{zils5.nosaukums} {zils5.forma}")
print("***")

zils5.forma = "derīgs 1"
print("Mainīta forma:")
print(f"{zils5.nosaukums} {zils5.forma}") 
print("***")