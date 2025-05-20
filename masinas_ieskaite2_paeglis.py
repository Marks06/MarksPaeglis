class Masina:
    def __init__(self,marka,modelis,gads): #A uzdevums - bāzes klases izveide
        self.marka = marka
        self.modelis = modelis
        self.gads = gads

    def uzsakt(self): #B uzdevums - klases 3 metodes
        return (f'{self.marka} {self.modelis} sāk darboties.')
    def apstaties(self):
        return (f'{self.marka} {self.modelis} ir apstādināta.')
    def info_par_auto(self):
        return(f'Marka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads}')
    

auto1 = Masina("Porche","GTR-911",2024) #C uzdevums - objekts klasei masina

class Elektro_Auto(Masina): #D uzdevums - atributa akumulatora_ietilp pievienosana
    def __init__(self, marka, modelis, gads,akumulatora_ietilp,akumulatora_uzlades_limenis):
        super().__init__(marka, modelis, gads)
        self.akumulatora_ietilp = akumulatora_ietilp
        self.akumulatora_uzlade = akumulatora_uzlades_limenis #E uzd - akumulatora_uzlades līmenis 
        self.noklusetais_akumulatora_uzlades_limenis = 100 #E uzd- akumulatora noklusētā vērtiba 100%
    def uzsakt(self):
        if self.akumulatora_uzlade>=20: #F uzd- pārbauda akumulatora uzladi
            return super().uzsakt() + f"Akumulators: {self.akumulatora_uzlade}%" 
        else: 
            return super().uzsakt() + f"Akumulators: {self.noklusetais_akumulatora_uzlades_limenis}% \n{self.marka} {self.modelis} nevar sākt darboties, jo akumulators ir pārāk zems: {self.akumulatora_uzlade}%."
    def apstaties(self):
        return super().apstaties()
    def info_par_auto(self):
        return super().info_par_auto() + f'\nAkumulators: {self.akumulatora_ietilp} kWh' #G uzd - uzrāda akumulātora ietilpību

elektro_auto1 = Elektro_Auto("Tesla", "Cybertruk", 2024,125,70) #H uzd - objekts, kuram akumulatora uzlades līmenis >= 20
 
elektro_auto2 = Elektro_Auto("Tesla", "Model 3", 2021,65,15) #I uzd - Simulēta akumulatora līmeņa samazināšana
print(elektro_auto2.info_par_auto())
print(elektro_auto2.uzsakt())

class Degvielas_Auto(Masina):
    def __init__(self, marka, modelis, gads, bakas_tilpums): #J uzd - bērna klases izveide, pievienots atribūts bakas_tilpums
        super().__init__(marka, modelis, gads)
        self.bakas_tilpums = bakas_tilpums
        self.noklusetais_degvielas_limenis = 100 #K uzd - noklusetais degvielas līmenis - 100
    def uzsakt(self):
        if self.bakas_tilpums>=10: #L uzd- pārbauda akumulatora uzladi
            return super().uzsakt() + f"Degvielas līmenis: {self.bakas_tilpums}%" 
        else: 
            return super().uzsakt() + f"Degvielas līmenis: {self.noklusetais_degvielas_limenis}% \n{self.marka} {self.modelis} nevar sākt darboties, jo degvielas līmenis ir pārāk zems: {self.bakas_tilpums}%."
    def apstaties(self):
        return super().apstaties()
    def info_par_auto(self): 
        return super().info_par_auto() + f"\nBākas tilpums:{self.bakas_tilpums} Litri" #M uzd - Pievienots bākas tilpums

degvielas_auto1 = Degvielas_Auto("Audi", "A7", 2022, 85) #N uzd- objekts, kuram pietiekams degvielas daudzums

degvielas_auto2= Degvielas_Auto("Audi", "A5", 2020, 5) #O uzd - objekts, kuram degvielas daudzums ir 5
print(degvielas_auto2.info_par_auto())
print(degvielas_auto2.uzsakt())