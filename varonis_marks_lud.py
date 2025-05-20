class Varonis:
    def __init__(self, dzivubas, vards):
        self.dzivubas = dzivubas
        self.vards = vards
    def uzbrukt(self):
        return f"{self.vards} izmanto "
    def aizstaveties(self):
        return f"{self.vards} aizstavas ar "
class Karotajs(Varonis):
    def __init__(self, dzivubas, vards):
        super().__init__(dzivubas, vards)
    def uzbrukt(self):
        return super().uzbrukt() + "zobenu"
    def aizstaveties(self):
        return super().aizstaveties() + "vairogu"

class Burvis(Varonis):
    def __init__(self, dzivubas, vards):
        super().__init__(dzivubas, vards)
    def uzbrukt(self):
        return super().uzbrukt() + "savu lielo maģisko zizli"
    def aizstaveties(self):
        return super().aizstaveties() + "savu lielo maģisko zizli"

class Savejs(Varonis):
    def __init__(self, dzivubas, vards):
        super().__init__(dzivubas, vards)
    def uzbrukt(self):
        return super().uzbrukt() + "savu lielo snaiperi"
    def aizstaveties(self):
        return super().aizstaveties() + "neko"

karotajs = Karotajs(199, "Ludvigs")
burvis = Burvis(80, "Marks")
savejs = Savejs(50, "Robis")

print(karotajs.uzbrukt(), burvis.uzbrukt(), savejs.uzbrukt())
print(karotajs.aizstaveties(), burvis.aizstaveties(), savejs.aizstaveties())