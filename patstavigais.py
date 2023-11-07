'''izveidot 3 sarakstus. lietotājs pats norādīs, 
cik elementus likt sarakstā.
Pirmā un otrā saraksta vērtības ievada lietotājs.
Trešā saraksta vērtības iegūst apvienojot pirmos 2 sarakstus
Katra saraksta saturu glīti parādīt uz ekrāna.'''

saraksts1 = []
saraksts2 = []

print('Ievadi pirmā saraksta garumu: ')
garums = int(input()) #lietotājs patvs ievada saraksta garumu

for i in range(garums):
    lieta1 = input('Ievadiet saraksta elementu: ')
    saraksts1.append(lieta1)


print('Ievadi otrā saraksta garumu: ')
garums2 = int(input()) #lietotājs patvs ievada saraksta garumu

for i in range(garums2):
    lieta2 = input('Ievadiet saraksta elementu: ')
    saraksts2.append(lieta2)


print('***************************')
print('Pirmā saraksta elementi: ', saraksts1)
print('Otrā saraksta elementi: ', saraksts2)
jauns_saraksts = [saraksts1+saraksts2]
print('Trešais saraksts: ', jauns_saraksts)
print('***************************')