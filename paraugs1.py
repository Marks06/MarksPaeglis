'''#saglabāt datus saraktā
names = []
for i in range(3):
    names.append(input("What's your name?"))
#atgriež sakārtotus
for name in sorted(names):
    print(f"Hello,{name}")'''
'''
#info no konsoles ieraksta failā
name=(input("What's your name?"))
file=open("names.txt","a",encoding='utf8')#w izveido failu un ieraksta datus
#a režīmā arī izveido failu,bet informāciju pievieno klāt
file.write(f'{name}\n')
file.close()#ja izmanto file=open, tad aizver ciet failu '''

'''#lieto context manager-fails nav jāaizver
name=(input("What's your name?"))
with open("names.txt","a",encoding='utf8') as file:
    file.write(f'{name}\n')'''

'''#nolasīt informāciju no faila
with open("names.txt",encoding='utf8') as file:
    for line in file:
        print("Hello,",line.rstrip())'''

#atgriezt sakārtotus datus no faila
names = []
with open("names.txt",encoding='utf8') as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"Hello,{name}")
