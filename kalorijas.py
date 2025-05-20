kal_kopejais = []
def iegut_datus():
    global kal_kopejais
    while True:
        try:
            nosaukums = str(input('Ievadiet ēdiena nosaukumu: '))
            kal_sk = float(input('Ievadiet kaloriju daudzumu uz 100g: '))
            svars_edienam = float(input("Cik gramus ēdiena Jūs apēdāt?: "))
            kal = kal_sk/100*svars_edienam
            kal_kopejais.append(kal)
            print(f'Kopējās kalorijas: ',kal_kopejais)
            aprekinat_cal_uznemsanu = input("Vai vēlies aprēķināt kaloriju uzņemšanu?(Jā/Nē): ")
            if aprekinat_cal_uznemsanu == 'Nē':
                break
            elif aprekinat_cal_uznemsanu == 'Jā':
                kaloriju_aprekins()

        except InterruptedError:
            print("Lūdzu ievadi pareizus datus.")
        except ValueError:
            print("Lūdzu ievadi pareizus datus.")

def kaloriju_aprekins():
    global kal_kopejais
    svars_cilvekam=float(input("Ievadiet savu svaru(kg): "))
    vecums=int(input("Ievadiet savu vecumu(vesels skaitlis): "))
    garums=int(input('Ievadiet savu garumu(vesels skaitlis/cm): '))
    dzimums=str(input('Ievadiet savu dzimumu(sieviete/vīrietis): '))
    aktivitates_limenis = input('Kāds ir jūsu aktivitātes līmenis? (zems,vidējs,augsts): ')
    print(f'Kopējo kaloriju uzņemšana:',kal_kopejais)
    if dzimums == 'sieviete':
        kalorijas = 655.1 + (9.563*svars_cilvekam) + (1.850*garums) - (4.676*vecums)
        if aktivitates_limenis == 'zems':
            kalorijas_diena = kalorijas*1.375
            if kal_kopejais < kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir zem kaloriju uzņemšanas normas robežām.')
            elif kal_kopejais >= kalorijas_diena and kal_kopejais <=kalorijas_diena:
                print("Jūsu kaloriju uzņemšana ir atbilstoši kaloriju uzņemšanas normas robežām.")
            elif kal_kopejais > kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir pāri kaloriju uzņemšanas normas robežām.')
        elif aktivitates_limenis == 'vidējs':
            kalorijas_diena = kalorijas*1.55
            if kal_kopejais < kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir zem kaloriju uzņemšanas normas robežām.')
            elif kal_kopejais >= kalorijas_diena and kal_kopejais <=kalorijas_diena:
                print("Jūsu kaloriju uzņemšana ir atbilstoši kaloriju uzņemšanas normas robežām.")
            elif kal_kopejais > kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir pāri kaloriju uzņemšanas normas robežām.')
        elif aktivitates_limenis == 'augsts':
            kalorijas_diena = kalorijas*1.725
            if kal_kopejais < kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir zem kaloriju uzņemšanas normas robežām.')
            elif kal_kopejais >= kalorijas_diena and kal_kopejais <=kalorijas_diena:
                print("Jūsu kaloriju uzņemšana ir atbilstoši kaloriju uzņemšanas normas robežām.")
            elif kal_kopejais > kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir pāri kaloriju uzņemšanas normas robežām.')
                
    elif dzimums == 'virietis':
        kalorijas = 6.47 + (13.75*svars_cilvekam) + (5.003*garums) - (6.755*vecums)
        if aktivitates_limenis == 'zems':
            kalorijas_diena = kalorijas*1.375
            if kal_kopejais < kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir zem kaloriju uzņemšanas normas robežām.')
            elif kal_kopejais >= kalorijas_diena and kal_kopejais <=kalorijas_diena:
                print("Jūsu kaloriju uzņemšana ir atbilstoši kaloriju uzņemšanas normas robežām.")
            elif kal_kopejais > kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir pāri kaloriju uzņemšanas normas robežām.')
        elif aktivitates_limenis == 'vidējs':
            kalorijas_diena = kalorijas*1.55
            if kal_kopejais < kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir zem kaloriju uzņemšanas normas robežām.')
            elif kal_kopejais >= kalorijas_diena and kal_kopejais <=kalorijas_diena:
                print("Jūsu kaloriju uzņemšana ir atbilstoši kaloriju uzņemšanas normas robežām.")
            elif kal_kopejais > kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir pāri kaloriju uzņemšanas normas robežām.')
        elif aktivitates_limenis == 'augsts':
            kalorijas_diena = kalorijas*1.725
            if kal_kopejais < kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir zem kaloriju uzņemšanas normas robežām.')
            elif kal_kopejais >= kalorijas_diena and kal_kopejais <=kalorijas_diena:
                print("Jūsu kaloriju uzņemšana ir atbilstoši kaloriju uzņemšanas normas robežām.")
            elif kal_kopejais > kalorijas_diena:
                print('Jūsu kaloriju uzņemšana ir pāri kaloriju uzņemšanas normas robežām.')
        
