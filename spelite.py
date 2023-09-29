import random
#akmens, skeres, papirs
gajieni = ['akmens','papirs','skeres'] #saraksts
while True:
    cilveka_gajiens = input('ievadi savu gājienu:')
    datora_gajiens = random.choice(gajieni)
    print('Cilvēks:', cilveka_gajiens, 'vs Dators:', datora_gajiens)
    if cilveka_gajiens == datora_gajiens:
        print('Neizšķirts!')
    elif cilveka_gajiens == 'akmens' and datora_gajiens == 'skeres': 
        print('Cilvēks uzvar!')
    elif cilveka_gajiens == 'skeres' and datora_gajiens == 'papirs':
        print('cilvēks uzvar!')
    elif cilveka_gajiens == 'papirs' and datora_gajiens == 'akmens':
        print('cilvēks uzvar!')
    else: 
        print('dators uzvar!')
