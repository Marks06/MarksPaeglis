from abc import ABC, abstractmethod #importē abstrakt klasi

class SkolasDarbinieks(ABC): #deklarē abstrakt klase
    def __init__(self,vards,uzvards) :
        self.vards= vards
        self.uzvards=uzvards

    def apraksts(self):
        return f'{self.vards} {self.uzvards}'

class Skolotajs_Matematikas(SkolasDarbinieks): #manto no abstrakt klases
    def apraksts(self):
        print(super().apraksts() + " ir matemātikas skolotājs") #
        return(super().apraksts() + " ir matemātikas skolotājs") #returns, lai varētu ievietot teksta failā
 
class Skolotajs_Sporta(SkolasDarbinieks):#manto no abstrakt klases
    def apraksts(self):
        print(super().apraksts() + " ir sporta skolotājs") 
        return (super().apraksts() + " ir sporta skolotājs") 

class Skolotajs_Vestures(SkolasDarbinieks): #manto no abstrakt klases
    def apraksts(self):
        print( super().apraksts() + " ir vēstures skolotājs") 
        return ( super().apraksts() + " ir vēstures skolotājs") 

class Lietvedis(SkolasDarbinieks): #manto no abstrakt klases
    def apraksts(self):
        print( super().apraksts() + " ir skolas lietvedis") 
        return ( super().apraksts() + " ir skolas lietvedis") 


darbinieki = [Skolotajs_Matematikas("Kaspars","Lācis"), 
Skolotajs_Sporta("Anda","Vīksna"), 
Skolotajs_Vestures("Inta","Romanovska"),
Lietvedis("Roberts","Rullis")]

with open("darbinieki.txt",'w',encoding='utf8') as fails:
    for i in darbinieki:
        fails.write(f"{i.apraksts()} \n")
    
