class Dzivnieks:
    def __init__(self,vards,vecums):
        self.vards = vards
        self.vecums = vecums
    
    def izdod_skanu(self):
        return (f'{self.vards} izdod ')
    
class Suns(Dzivnieks):
    def __init__(self, vards, vecums):
        super().__init__(vards, vecums)
    def izdod_skanu(self):
        return super().izdod_skanu()+"vau vau"

class Kakis(Dzivnieks):
    def __init__(self, vards, vecums):
        super().__init__(vards, vecums)
    def izdod_skanu(self):
        return super().izdod_skanu()+ "ņau ņau"

class Putns(Dzivnieks):
    def __init__(self, vards, vecums):
        super().__init__(vards, vecums)
    def izdod_skanu(self):
        return super().izdod_skanu()+ "čiv čiv"

dzivnieks1=Suns("Suns",146)
print(dzivnieks1.izdod_skanu())