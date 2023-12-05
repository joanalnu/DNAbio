#random DNA sequence generator
from random import randint

lenght = int(input("Lenght: "))

DNA = "TAC"

for i in range (lenght):
    base = randint(1, 4)
    if base==1:
        DNA+='A'
    elif base==2:
        DNA+='C'
    elif base==3:
        DNA+='G'
    elif base==4:
        DNA+='T'

stopCodon = randint(1, 3)
if stopCodon==1:
    DNA+="ATT"
elif stopCodon==2:
    DNA+="ATC"
elif stopCodon==3:
    DNA+="ACT"

print(DNA)
