class Forma:
    def aprekinat_laukumu(self):
        return 0
    def perimetrs(self):
        return 0

class Aplis(Forma):
    def __init__(self, radiuss) -> None:
        self.radiuss = radiuss
        super().__init__()
    def aprekinat_laukumu(self):
        return super().aprekinat_laukumu()+(3.14 * self.radiuss * self.radiuss)
    def perimetrs(self):
        return super().perimetrs() + (2 * 3.14 * self.radiuss)
    
class Kvadrats(Forma):
    def __init__(self, mala) -> None:
        super().__init__()
        self.mala = mala

    def aprekinat_laukumu(self):
        return super().aprekinat_laukumu() + (self.mala * self.mala)
    
    def perimetrs(self):
        return super().perimetrs() + (4 * self.mala)

class Taisnsturis(Forma):
    def __init__(self, mala1, mala2) -> None:
        super().__init__()
        self.mala1 = mala1
        self.mala2 = mala2

    def aprekinat_laukumu(self):
        return super().aprekinat_laukumu() + (self.mala1 * self.mala2)

    def perimetrs(self):
        return super().perimetrs() + ((self.mala1 * 2) + (self.mala2 * 2))

aplis = Aplis(5)
kvadrats = Kvadrats(6)
taisnsturis = Taisnsturis(3, 5)

print("Laukums")
print(f"Aplis: {aplis.aprekinat_laukumu()}\nKvadrats: {kvadrats.aprekinat_laukumu()}\nTaisnsturis: {taisnsturis.aprekinat_laukumu()}")
print("Perimetrs")
print(f"Aplis: {aplis.perimetrs()}\nKvadrats: {kvadrats.perimetrs()}\nTaisnsturis: {taisnsturis.perimetrs()}")
