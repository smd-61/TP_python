# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#EX1
print("choisissez la valeur de x")
x=int(input())
print("choisissez la valeur de y")
y=int(input())
tmp=x
x=y
y=tmp
print("Les valeurs ont été permuter")

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

print(f"Il vous faudra donc {fromage}gramme de fromage, {eau}L d'eau, {ail} ail et enfin {pain} gramme de pain")


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