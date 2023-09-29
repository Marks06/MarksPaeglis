import math
zvaigznes = '\t ****' #lai nav visu laiku jaraksta tās **** es izveidoju mainīgo
print('Programmu izstrādāja: Marks, Daniels, Paeglis.')

print('Laukuma aprēķins ģeometriskām figurām' )
print(zvaigznes)
malaA = float(input("Ievadiet malas A garumu:")) #automātiski pārveidoju par float lai ir tas skaitlis .0 
print('Malas A garums:', malaA)
print(zvaigznes)
malaB = float(input("Ievadiet malas B garumu:"))
print('Malas B garums:', malaB)
print(zvaigznes)
augstums = float(input("Ievadiet augstumu:"))
print('Augstums:', augstums)
print('Laukums trijstūrim:',malaA*augstums/2)
print('Laukums trapecei:',(malaA+malaB)/2*augstums)
print('Laukums paralelogramam:',malaA*augstums)
print(zvaigznes)
print('Paldies!')
