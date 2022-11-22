#ex1
#a
print("Entrer un nombre ")
n=int(input())
s=0
for i in range (0, n+1):
    s=s+i

print("La somme des N premiers nombre est égale à", s)

#b
print("Entrer un nombre")
n=0
while n!=100:
    n=int(input())
print("ENFIN")

#c
a=0
b=0
c=0

for i in range (0, 10):
    n=0
    print("Entrer un nombre")
    n = int(input())
    while n<0 or n>20:
        print("Re rentrer un nombre")
        n=int(input())

    if n<10:
        a=a+1
    elif n<=10 and n<15:
        b=b+1
    else:
        c=c+1
print(f"Il y a donc, {a} valeurs inférieurs à 10, {b} entre 10 et 15 valeurs et {c} valeurs supérieurs à 15")

#d
print("Entrer un nombre ")
x=int(input())
s=0
y=0
r=1
while r<5:
    s=s+y
    if s<=x:
        y=y+1
    else:
        y=y-1
        break

print("Le plus grand nombre N est", y)



#ex2
#v1
from time import sleep
print("Entrer un nombre ")
x=int(input())
for i in range(x, -1, -1):
    print(i)
    sleep(1)

#v2
from time import sleep
print("Entrer un nombre")
x=int(input())
while x>-1:
    print(x)
    sleep(1)
    x=x-1
#ex3
import random
t=random.randint(0,100)
x=122
a=0
z=1
d=0
while z>0:
    print("Entrer un nombre")
    x= int(input())
        while x<0 or x>100:
            print("re entrer un nombre")
            x=int(input())

        if x<t:
            print("Le nombre est plus grand")
            a=a+1
            d=d+1
        elif x>t:
            print("Le nombre est plus petit")
            a=a+1
            d = d + 1
        else:
            a=a+1
            z=(-2)
            d=d+1

print("Vous avez trouvé le nombre", t,"en",d,"essais")

#ex4
print("Quelle boucle?\n-\"1\" pour la boucle while.\n-\"2\" pour la boucle for")
x=int(input())
a=1
c=1
if x==1:
    print("Entrer un nombre")
    z = int(input())
    if z!=0:
        for i in range (1, z+1):
            a=a*i
            print("Le factorielle de", z, " est égale à", a)
    else:
        print("Le factorielle de 0 est 1")

elif x==2:
    print("Entrer un nombre")
    z = int(input())
    if z != 0:
        while c<=z:
            a = a * c
            c=c+1
            print("Le factorielle de", z, " est égale à", a)
    else:
        print("Le factorielle de 0 est 1")
else:
    print("ERROR")