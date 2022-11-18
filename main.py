# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#EX1
import random

print("choisissez la valeur de x")
x=int(input())
print("choisissez la valeur de y")
y=int(input())
print(f"Avant permutation: \n -x : {x} \n -y : {y}")
tmp=x
x=y
y=tmp
print(f"Après permutation: \n -x : {x} \n -y : {y}")

#ex2
print("Quel est votre age?")
age=int(input())
an=2022-age

print(f"Votre année de ,naissance est {an}")


#ex3
a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

tmp1=b
tmp2=c
b=a
c=tmp1
a=tmp2

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)

#ex4

BASE=4
fromage=800.0
eau=2
ail=2
pain=400
print("Pour combien de personne préparer vous cette recette?")
nbConvives=int(input())
fromage=800.0*nbConvives/BASE
eau=2*nbConvives/BASE
ail=2*nbConvives/BASE
pain=400*nbConvives/BASE

print(f"-Il vous faudra donc {fromage}gramme de fromage\n- {eau}L d'eau\n- {ail} ail \n -{pain} gramme de pain\n")


#ex5
print("Donnez un nombre")
a=int(input())
c=a%2
if a>0:
    print("Le nombre est positif")
elif a==0:
    print("Le nombre est nul")
else:
    print("Le nombre est négatif")

if  c==0:
    print("et pair.")
else:
    print("et impair.")

#tp2exo6.py
import random
a=random.randint(0,100)
if a<50:
    print("PILE!")
else:
    print("FACE!")

#tp2exo7.py
import random
a=random.randint(0,2)
if a<2:
    print("PILE!")
else:
    print("FACE!")

#EX8
print("Entrer un nombre")
x=float(input())

if (x>=2 and x<3) or (x>0 and x<=1) or (x>=(-10) and x<(-2)):
    print("X appartient à I")
else:
    print("X n'appartient pas à I")