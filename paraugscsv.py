import csv
#izveidot csv failus un ļaut rakstīt datus
'''
with open("students0.csv","a",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Name","House"]) #pievieno kolonnu nosaukumus
    #iegūst datus no lietotāja
    while True:
        name=input("Enter name and house(type 'ok' to finish):")
        if name.lower()=="ok":
            break
        student_house = input(f"Enter {name}'s house:")
        writer.writerow([name,student_house])
        print(f"{name} has been added.\n") '''
#nolasīt info no csv faila
students=[]
with open("students0.csv", encoding='utf8') as file:
    for line in file: #cikla mainīgais katrā iterācijā iegūst rindiņas saturu kā teksta virkni
        name, house=line.rstrip().split(",")#noņem liekos simbolus rindas beigās, ar split sadala tekstu ar , 
        students.append(f'{name} is in {house}.')
    for student in sorted(students):
        print(student)

