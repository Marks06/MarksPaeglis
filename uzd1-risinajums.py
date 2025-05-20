#jānolasa csv faila saturs, aprēķināt vidējo vērtējumu
#jāpievieno jaunu lauku Vidējais, to visu saglabā jaunā csv failā

import csv
ievades_dati='skoleni.csv'
izvades_dati='skoleni_videjais.csv'

with open (ievades_dati,'r',encoding='utf8') as file:#mainigais file tagad atver atvērto failu
    #nolasīt csv failu un katru rindu pārvērš par vārdnīcu(kollona:atslēga, vērtība: konkrētā rinda)
    reader=csv.DictReader(file)
    skoleni=list(reader) #mainīgais skolēni ir python saraksts
    #katrs saraksta elements ir 1 ieraksts no csv faila

#rēķina vidējo un pievieno jaunu lauku
for skolens in skoleni:
    matematika=int(skolens['Matemātika'])
    anglu_val=int(skolens['Angļu valoda'])
    sports=int(skolens['Sports'])
    videjais=round((matematika+anglu_val+sports)/3,2)
    #katram skolēna ierakstam tiek pievienots jauns lauks Vidējais
    skolens['Videjais']=videjais

#saglabāt datus jaunā failā
with open (izvades_dati,'w',encoding='utf8',newline='') as file:
    fieldnames=skoleni[0].keys() #atgriež pirmās kollonas atslēgas nosaukumu
    #objekts,kas raksta datus uz csv faila
    writer=csv.DictWriter(file,fieldnames=fieldnames)#rakstīs pareizā secībā
    #ieraksta pirmo rindu
    writer.writeheader()#ieraksta pirmo rindu, kas ir kollonā
    writer.writerows(skoleni) #iziet cauri sarakstam un katru vārdnīcu ieraksta kā jaunu rindiņu

print(f"Jaunais fails ir saglabāts kā '{izvades_dati}'.")
