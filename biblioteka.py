publikacija = (input('Vai grāmata ir publikācija? [Ja,Ne]:'))
pieprasits = (input('Vai grāmata ir pieprasīto izdevumu sarakstā? [Ja,Ne]:'))
gramatas = (input('Vai šī ir grāmata [ne žurnāls]? [Ja,Ne]:'))
zurnals = (input('Vai šīs ir žurnāls? [Ja,Ne]:'))
students = (input('Vai tu esi students? [Ja,Ne]:'))
nenodots = (input('Vai tev ir nenodots izdevums? [Ja,Ne]:'))

if publikacija == 'Ja' and pieprasits == 'Ja' and nenodots == 'Ne' and students == 'Ja' and students == 'Ne' and gramatas == 'Ja' or zurnals == 'Ja':
    print('Izsniedz uz 2 dienām')
elif gramatas == 'Ja' and pieprasits == 'Ne' and students == 'Ne' and nenodots == 'Ne':
    print('izsniedzam uz 28 dienām')
elif gramatas == 'Ja' and pieprasits == 'Ne' and students == 'Ja' and nenodots == 'Ne':
    print('izsniedzam uz 14 dienām')
elif zurnals == 'Ja' and pieprasits == 'Ne' and students == 'Ja' and students == 'Ne' and nenodots =='Ne':
    print('izsniedzam uz 7 dienām')
elif nenodots == 'Ja':
    print('Nedrīksti neko ņemt')
