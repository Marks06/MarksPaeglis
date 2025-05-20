class Darbinieks:
    def __init__(self,vards,uzvards,alga) :
        self.vards= vards
        self.uzvards = uzvards
        self.alga=alga

    def uzradit_info(self):
        return (f'Vārds: {self.vards} Uzvārds: {self.uzvards} Alga: {self.alga}')

class Programetajs(Darbinieks):
    def __init__(self, vards, uzvards, alga, programmesanas_valoda):
        super().__init__(vards, uzvards, alga)       
        self.programmesanas_valoda = programmesanas_valoda

    def uzradit_info(self):
        return super().uzradit_info()+ (f' Programmēšanas valoda: {self.programmesanas_valoda}')

class Pardevejs(Darbinieks):
    def __init__(self, vards, uzvards, alga, pardosanas_apjoms):
        super().__init__(vards, uzvards, alga)
        self.pardosanas_apjoms = pardosanas_apjoms

    def uzradit_info(self):
        return super().uzradit_info()+ (f' Pārdošanas apjoms: {self.pardosanas_apjoms}')

class Vaditajs(Darbinieks):
    def __init__(self, vards, uzvards, alga, vecums):
        super().__init__(vards, uzvards, alga)
        self.vecums = vecums
    def uzradit_info(self):
        return super().uzradit_info()+ (f' Vecums: {self.vecums}')
    
programetajs = Programetajs("Marks", "Lielbārdis",6203,"Python")
pardevejs = Pardevejs("Ludvigs", "Paeglis", 399, "Liels")
vaditajs = Vaditajs("Patriks", "Sidrevics", 234789, 5)

print(f"Programmetājs: {programetajs.uzradit_info()}\nPardevējs: {pardevejs.uzradit_info()}\nVadītājs: {vaditajs.uzradit_info()}")