publikacija = (input('Vai šī ir publikācija? [Ja,Ne]:'))
pieprasits = (input('Vai grāmata ir pieprasīto izdevumu sarakstā? [Ja,Ne]:'))
gramatas = (input('Vai šī ir grāmata [ne žurnāls]? [Ja,Ne]:'))
zurnals = (input('Vai šīs ir žurnāls? [Ja,Ne]:'))
students = (input('Vai tu esi students? [Ja,Ne]:'))
nenodots = (input('Vai tev ir nenodots izdevums? [Ja,Ne]:'))

if publikacija == 'Ja' and pieprasits == 'Ja' and nenodots == 'Ne' and students == 'Ja' and students == 'Ne' and gramatas == 'Ja' or zurnals == 'Ja': #ja atbilst visiem kritērijiem , tad printē ka izsniedz uz 2 dienām
    print('Izsniedz uz 2 dienām')
elif gramatas == 'Ja' and pieprasits == 'Ne' and students == 'Ne' and nenodots == 'Ne': #ja atbilst visiem kritērijiem , tad printē ka izsniedz uz 28 dienām
    print('izsniedzam uz 28 dienām')
elif gramatas == 'Ja' and pieprasits == 'Ne' and students == 'Ja' and nenodots == 'Ne': #ja atbilst visiem kritērijiem , tad printē ka izsniedz uz 14 dienām
    print('izsniedzam uz 14 dienām')
elif zurnals == 'Ja' and pieprasits == 'Ne' and students == 'Ja' and students == 'Ne' and nenodots =='Ne':  #ja atbilst visiem kritērijiem , tad printē ka izsniedz uz 7 dienām
    print('izsniedzam uz 7 dienām')
elif nenodots == 'Ja':    #ja atbilst visiem kritērijiem , tad printē ka neizsniedz vispār
    print('Nedrīksti neko ņemt')
