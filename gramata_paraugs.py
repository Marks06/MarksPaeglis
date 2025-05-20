from abc import ABC, abstractmethod

#visparīgā datu struktūra, kas nepieciešama visām grāmatām
class Gramata(ABC): #abstrakstā klase ar metodi gramatas_dati
    @abstractmethod
    def gramatas_dati(self):
        pass

#izveidot 2 apakšklases, kur katra metodi(gramatas_dati) realizē citādāk

class Rich_Dad_Poor_Dad(Gramata):
    def gramatas_dati(self):
        print(f"Rich Dad Poor Dad, 351 Lappuses")
class Ego_is_the_enemy(Gramata):
    def gramatas_dati(self):
        print(f"Ego is the enemy autors ir Ryan Holidays")

gramata1=Rich_Dad_Poor_Dad()
gramata1.gramatas_dati()

gramata2=Ego_is_the_enemy()
gramata2.gramatas_dati()