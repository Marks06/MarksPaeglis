
def parbaudit(vards):
    if not vards.isalpha():
        print("Vārdā drīkst būt tikai burti!")
        return False
    return True
def normalizet_vardu(vards):
    return vards.strip().capitalize()
def parbaudit_uzvardu(uzvards):
    if not uzvards.isalpha():
        print("Uzvārdā drīkst būt tikai burti!")
        return False
    return True
def normalizet_uzvardu(uzvards):
    return uzvards.strip().capitalize()
def parbaudit_vecumu(vecums):
    if not vecums.isdigit():
        print("Vecumam jābūt pozitīvam veselam skaitlim!")
        return False
    if int(vecums) <= 0:
        print("Vecumam jābūt pozitīvam veselam skaitlim!")
        return False
    return True
def parbaudit_atzimi(atzime):
    if not atzime.isdigit():
        print("Atzīmei jābūt pozitīvam skaitlim no 1-10!")
        return False
    if int(atzime) > 10 and int(atzime) < 0:
        print("Atzīmei jābūt pozitīvam skaitlim no 1-10!")
        return False
    return True

def pievienot_datus_failam(faila_nosaukums):
    turpinat = 'ja'
    try:  
        with open(faila_nosaukums,"a",encoding='utf8') as file: 
            while turpinat == "ja":
                print("Ievadiet jaunu ierakstu vai ievadiet 'STOP', lai pārtrauktu")
                while True:
                    vards = input("Ievadiet vārdu: ")
                    if vards == 'STOP':
                        break
                    elif parbaudit(vards):
                        vards=normalizet_vardu(vards)
                        break
                while True:
                    uzvards = input("Ievadiet uzvārdu: ")
                    if uzvards == 'STOP':
                        break
                    elif parbaudit(uzvards):
                        uzvards=normalizet_uzvardu(uzvards)
                        break
                while True:
                    vecums= input("Ievadiet vecumu: ")
                    if vecums == "STOP":
                        break
                    elif parbaudit_vecumu(vecums):
                        break
                while True:
                    atzime = input("Ievadiet gala atzīmi (1-10): ")
                    if atzime == "STOP":
                        break
                    elif parbaudit_atzimi(atzime):
                        break
                file.write(f'{vards},{uzvards},{vecums},{atzime}\n')
                turpinat = input("Vai vēlaties ievadīt vēl vienu ierakstu? (ja/ne):")
            
    except Exception as e:
        print(f"Kļūda, saglabājot datus failā: {e}")

def paradit_datus(faila_nosaukums):
    with open(faila_nosaukums,"r",encoding='utf8') as file: 
        dati=file.readlines()
        if not dati: #pārbauda vai failā ir dati
                print("Fails ir tukšs. Pievienojiet datus")

def izvelne():
    faila_nosaukums = "kontroldarbs.txt"
    turpinat = 'ja'
    while True:
        print("\nIzvēlēties opciju:")
        print('1 - Pievienot datus')
        print('2 - Parādīt datus')

        izvele = input("Izvēle: ")
        if izvele== '1':
            pievienot_datus_failam(faila_nosaukums)
        elif izvele=='2':
            paradit_datus(faila_nosaukums)
        else:
            print("Nepareiza izvēle. Lūdzu mēģiniet vēlreiz.")

izvelne()
