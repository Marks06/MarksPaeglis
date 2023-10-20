'''atbilde = 'j'
while atbilde == 'j':
    print('Nekusties!')
    atbilde = input('Vai briesmonis ir draudzīgs?(j/n)')
print('Bēdz prom!')'''

#pārbaudīt vai lietotājs prot reizināt ar 7
#programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautājumi
reiz = int(input('Reizinātājs:'))
for i in range(1,13): #cikla manīgais no 1-12
    print('Cik ir ',i,'reizināts ar',reiz,'?')
    minejums = input()
    if minejums == 'stop':
        break  #izbēgšana no cikla
    if minejums == 'izlaist':
        print('Tiek izlaists')
        continue #izlaiž 1 jautājumu un turpina tālāk
    atb = i*reiz
    if int(minejums) == atb:
        print('Pareizi!')
    else:
        print('Nē, tas ir',atb)
        #ja ir nepareizi, tad atgriežas pie jautājuma
        #rezinātaju ievada lietotājs