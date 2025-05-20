import csv

def izveidot_failu():
    with open ('dati_pilsetas.csv','w',newline='',encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(["Pilseta","Iedzīvotāju skaits"])
        for i in range(5):
            while True:
                pilseta=input(f"Ievadi {i+1} pilētas nosaukumu:")
                if pilseta:
                    try:
                        iedzivotaji=int(input(f"Ievadi {pilseta} iedzīvotāju skaitu:"))
                        writer.writerow([pilseta,iedzivotaji])
                        break
                    except ValueError:
                        print("Lūdzu ievadiet skaitli.")
                else:
                    print("Pilsētas nosaukums nedrīkst būt tukšs")
#izveidot_failu()

def lasit_csv():
    try: #try , lai varētu novērst erroru
        with open ('dati_pilsetas.csv','r',encoding='utf8') as file: #r režīms , jo vajag tikai nolasīt
            reader=csv.reader(file)
            next(reader)
            for rinda in reader:
                print(*rinda) #Šis * simbols padara skaistāku, noņem kvadrāt iekavas
                print("--------------")
    except FileNotFoundError:
        print("Fails netika atrasts!")

#lasit_csv()

def kopskaits():
    try: #try , lai varētu novērst erroru
        with open ('dati_pilsetas.csv','r',encoding='utf8') as file: #r režīms , jo vajag tikai nolasīt
            reader=csv.reader(file)
            next(reader)
            kopejais_skaits=sum(int(rinda[1]) for rinda in reader)
            print(f'Kopējais iedzīvotāju skaits: {kopejais_skaits}')

    except FileNotFoundError:
        print("Fails netika atrasts!")

kopskaits()
