for num in range(1,10):
    print(str(num)*num)
print('******')
gadi = int(input('Kāds ir suņa vecums?'))

if gadi < 0 :
    exit()
elif gadi <= 2:
    print(gadi*10.5)
elif gadi > 2:
    print(2*10.5 + gadi*4)

print('**********')

for i in range (1,21):
    print('<<',i,'.autobusa pietura>>')

print('**********')

rinda = 7
for i in range(0,rinda):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")

for i in range(rinda, 0, -1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")

