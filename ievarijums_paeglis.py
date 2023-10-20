abols = int(input('Cik kg ābolu vēlies likt iegšā ievārijumā?'))
kanelis_majas = (input('Vai tev mājās ir kanēlis? (j,n)'))
cukurs_majas = (input('Vai tev mājās ir cukurs? (j,n)'))
if cukurs_majas == 'j':
     cukura_veids_majas = (input('Kāds tev mājās ir cukurs? (parastais , ievārijuma cukurs)'))
udens_majas = (input('Vai tev mājās ir ūdens? (j,n)'))
citrons_majas = (input('Vai tev mājās ir citrons? (j,n)'))
mandeles_majas = (input('Vai tev mājās ir mandeļu ekstraksts? (j,n)'))
c_cena = 1.35
k_cena = 0.39
u_cena = 0.55
ci_cena = 2.99
m_cena = 1.19
print('\tDotās cenas ir ņemtas no RIMI\n')

if cukurs_majas == 'n':
    print('Cukurs Rimi 1kg ir 1.35 Eur')
else :
    int(input('Cik kg cukura tev ir?'))
if kanelis_majas == 'n':
    print('Kanēlis Twins malts 15g ir 0.39eur')
else :
    int(input('Cik kg kanēlis tev ir?'))
if udens_majas == "n":
    print("Dzeramais ūdens Zaķumuiža negāzēts 0,5l maksā 0.45eur + depozīts 10 centi")
else :
    int(input('Cik l ūdens tev ir?'))
if citrons_majas == 'n':
    print('Citroni Mayer C/2-3 1. šķira 1kg ir 2.29eur')
else :
   int(input('Cik citroni tev ir?'))
if mandeles_majas == 'n':
    print('Mandeļu aromatizētājs Dr. Oetker 8ml ir 1.19eur')
else :
    int(input('Cik ml mandeļu ekstrakts tev ir?'))
if cukurs_majas == 'j' and kanelis_majas == 'j' and udens_majas == 'j' and citrons_majas == 'j' and mandeles_majas == 'j':
    int(input('Cik kg cukura tev ir?'))
elif cukurs_majas == 'n' and kanelis_majas == 'n' and udens_majas == 'n' and citrons_majas == 'n' and mandeles_majas == 'n':
    print('Kopā jāmaksā:', round(c_cena + k_cena + u_cena + ci_cena + m_cena, 2), 'eur')
print(' Recepte: \n \t 3kg āboli \n \t 1kg cukurs \n \t 500ml ūdens \n \t 1gab citrons \n \t 5ml mandeļu ekstrakts \n \t 10g kanēlis')
recepte = int(input('Vai vēlies visus ābolus iztērēt receptei? (j,n)'))
if recepte == 'j':
    print('Receptei nepieciešams šāds daudzums produktu:','aboli (kg)', abols ,' cukurs (kg):', abols/3, 'ūdens(ml):', abols/6,'citrons (gab.):', abols/3 , 'mandeļu ekstrakts (ml):',abols/600 , 'kanēlis (g)',abols/300)