

def ierakstit_faila():

    with open ('fails.txt','w',encoding='utf8') as file:
        for i in range(1,11):
            pilseta=input(f"Ievadi {i}. pilsētu:")
            file.write(pilseta+"\n")
        print("Dati ir saglabāti!")

#ierakstit_faila()

def nolasit_ar_for():
    try:
        with open('fails.txt','r',encoding='utf8') as file:
            print("Faila saturs:")
            for i in file:
                print(i.strip())  #strip noņem liekās atstarpes!!
            print("--------------")
    except FileNotFoundError:
        print("Fails netika atrasts!")

def sakartot_datus():
    try:
        with open ('fails.txt','r',encoding='utf8') as file:
            saturs = file.readlines()
        kartots = sorted(saturs)
        print(kartots)
        print('Teksts sakārtots augošā secībā!')
    except FileNotFoundError:
        print("Fails netika atrasts!")

def pievienot_failam():
    vardi = []

    with open ('fails.txt','a',encoding='utf8') as file:
        for i in range(1,4):
            ievade = input("Ievadi vārdu kuru vēlies pievienot: ")
            vardi.append = ievade
        for i in vardi:
            file.write(i+'\n')
        print(f'{len(vardi)} jauni vārdi pievienoti')

'''def atrast_vardu():
    pilsetas_nosaukums = ievade
    with open ('fails.txt', 'r',encoding='utf8') as file:
        saturs = file.read()
    if pilsetas in saturs:
        print(f"Šī {pilsetas_nosaukums} pastāv sarakstā!")'''
            
