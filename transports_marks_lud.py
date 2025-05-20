class Transportlidzeklis:
    def __init__(self,transportlidzeklis,atrums):
        self.transportlidzeklis = transportlidzeklis
        self.atrums = atrums
    def parvietoties(self):
        return (f'{self.transportlidzeklis} brauc pa ')
    def uzradit_atrumu(self):
        return (f'Atrums ir {self.atrums} km/h')
class Auto(Transportlidzeklis):
    def __init__(self, transportlidzeklis, atrums):
        super().__init__(transportlidzeklis, atrums)

    def parvietoties(self):
        return super().parvietoties()+"ceļu"
    
class Velosipeds(Transportlidzeklis):
    def __init__(self, transportlidzeklis, atrums):
        super().__init__(transportlidzeklis, atrums)

    def parvietoties(self):
        return super().parvietoties()+"taku"

class Lidmasina(Transportlidzeklis):
    def __init__(self, transportlidzeklis, atrums):
        super().__init__(transportlidzeklis, atrums)

    def parvietoties(self):
        return super().parvietoties()+"gaisu"

transportlidzekli=[
    Auto("Auto",150),
    Velosipeds("Velosipēds",80),
    Lidmasina("Lidmašīna",460)
]

for i in transportlidzekli:
    print(i.parvietoties())
    print(i.uzradit_atrumu())
