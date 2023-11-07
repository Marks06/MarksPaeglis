saraksts = [2,6,8,3,1,9,7,4,6]
saraksts.append('Cepums') #pievieno beigās
print(saraksts)

saraksts.pop()  #izmet no beigām
print(saraksts)

saraksts.insert(3, 'Hello!') #ievieto pirms 3 no kreisās puses
print(saraksts)

saraksts.remove('Hello!') #izdzēš norādīto vērtību
print(saraksts)

tests = [1,2,3,4,5,6,7,8]
del tests[2] #izdzēš 1 elementu
print(tests)

del tests[3:6]
print(tests) #izdzēš intervālu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2] #no intervāla 2 līdz 7 izdzēš katru otro elementu
print(cipari)