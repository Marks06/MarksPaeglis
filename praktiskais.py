#ierakstīt teksta failā(no programmas) vārdu, uzvārdu, vecumu.
'''dot iespēju izvēlēties: 
 1- pievienot datus 
 2- Nolasīt datus
 3- parādīt sakārtotus datus pēc vecuma
 4- iziet
 Apstrādāt kļūdas
 def pievienot_datus_failam, def sakartot_pec_vecuma, def paradit_sak_datus
'''

def parbaudit_vardu(vards): #pārbauda vai dati sastāv tikai no burtiem
    if not vards.isalpha():
        print("Vārdā drīkst būt tikai burti!")
        return False
    return True


def parbaudit_vecumu(vecums): #pārbauda vai derīgi dati
    if not vecums.isdigit():
        print("Vecumam jābūt skaitlim!")
        return False
    if int(vecums) <= 0:
        print("Vecumam jābūt lielākam par 0!")
        return False
    return True

def normalizet_vardu(vards):
    return vards.strip().capitalize()

def dublikats(vards,uzvards,vecums,faila_nosaukums):
    try:
        with open(faila_nosaukums,"r",encoding='utf8') as file:
            dati=file.readlines()
        ieraksts=f"{vards},{uzvards},{vecums}\n"
        return ieraksts in dati
    except FileNotFoundError:
        return False #fails nav izveidots, tātad dublikātu nav


def pievienot_datus_failam(faila_nosaukums):
    try:
        with open(faila_nosaukums,"a",encoding='utf8') as file:
            while True:
                vards = input("Ievadiet vārdu:")
                if parbaudit_vardu(vards):
                    vards=normalizet_vardu(vards)
                    break

            while True:       
                uzvards = input('Ievadiet uzvārdu:')
                if parbaudit_vardu(uzvards):
                    uzvards =normalizet_vardu(uzvards)
                    break
            while True:
                vecums = input('Ievadiet vecumu:')
                if parbaudit_vecumu(vecums):
                    break

            if dublikats(vards,uzvards,vecums,faila_nosaukums):
                print("Šis ieraksts jau pastāv!")
                return
        #dati tiek saglabāti teksta failā
        
            file.write(f'{vards},{uzvards},{vecums}\n')
        print("Dati ir pievienoti veiksmīgi!")
        
        file.close

    except Exception as e:
        print(f"Kļūda, saglabājot datus failā: {e}")





def paradit_datus(faila_nosaukums):
        try:
            with open(faila_nosaukums,"r",encoding='utf8') as file:
                dati=file.readlines()
            if not dati: #pārbauda vai failā ir dati
                print("Fails ir tukšs. Pievienojiet datus")
            else:
                print("\nDati no faila:")
                for ieraksts in dati:
                    print(ieraksts.strip())
        except FileNotFoundError:
            print(f"Fails {faila_nosaukums} nepastāv!")

def iegut_vecumu_no_datiem(ieraksts):
    try:
        vecums=int(ieraksts.strip().split(",")[-1])
        return vecums
    #ja formāts nav pareizs, atgriež 0
    except(IndexError,ValueError):
        return 0

def sakartot_un_paradit(faila_nosaukums):
    try:
        with open(faila_nosaukums,"r",encoding='utf8') as file:
            dati=file.readlines()
        if not dati: #pārbauda vai failā ir dati
                print("Fails ir tukšs. Pievienojiet datus")
        else:
            #kārtošana
            sakartoti_dati = sorted(dati,key=iegut_vecumu_no_datiem)
            print("\nPēc vecuma sakārtoti dati:")
            for ieraksts in  sakartoti_dati:
                print(ieraksts)
    except FileNotFoundError:
        print(f"Fails {faila_nosaukums} nepastāv!")            



#programmas galvenā daļa            
def izvelne():
    faila_nosaukums = "dati.txt"
    while True:
        print("\nIzvēlēties opciju:")
        print("1 - Pievienot datus")
        print('2 - Parādīt datus')
        print('3 - Parādīt sakārtotus datus pēc vecuma')
        print('4 - Iziet')

        izvele = input("Izvēle: ")
        if izvele== '1':
            pievienot_datus_failam(faila_nosaukums)
        elif izvele=='2':
            paradit_datus(faila_nosaukums)
        elif izvele=='3':
            sakartot_un_paradit(faila_nosaukums)
        elif izvele == '4':
            print('Programma beidzas')
            break
        else:
            print("Nepareiza izvēle. Lūdzu mēģiniet vēlreiz.")

izvelne()