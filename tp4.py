#ex1
tab= []
z=float(input("Quelle table voulez-vous?"))
for i in range (0,10):
    a=z*i
    tab.append(round(a,1))
    print(z,"* ",i ,"=", tab[i])

#ex2
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
notes = []
ecart = []

for i in range (0,nombreEtudiants):
    notes.append(float(input(f"Note etudiant {i}:")))
    while notes[i]>20 or notes[i]<0 :
        notes[i] = float(input(f"Resaisir la note de l'etudiant {i}:"))

for i in range (0,nombreEtudiants):
    moyenne = moyenne+notes[i]

moyenne=moyenne/nombreEtudiants

for i in range (0,nombreEtudiants):
    ecart.append(notes[i]-moyenne)

print(f"Moyenne de classe :{moyenne}")
print(f"Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range (0,nombreEtudiants):
    print(f"{i} | {notes[i]} | {ecart[i]}")

#EXERCICE3
print("la taille maximale des vecteurs est 3")
nmax=3
pro=0
v1 = []
v2 = []
n=int(input("Entrer la taille effective des vecteurs"))
while n>nmax or n<1:
    n = int(input("Entrer de nouveau la taille effective des vecteurs"))

for i in range (0,n):
    v1.append(int(input(f"Entrer la valeur de la {i} composante de v1")))

for i in range (0,n):
    v2.append(int(input(f"Entrer la valeur de la {i} composante de v2")))

for i in range (0,n):
    pro=v1[i]*v2[i]+pro
    pro=float(pro)


print(f"Saisie du premier vecteur :\nv1[0] = {v1[0]}\nv1[1] = {v1[1]}\nv1[2] = {v1[2]}")
print(f"Saisie du second vecteur :\nv2[0] = {v2[0]}\nv2[1] = {v2[1]}\nv2[2] = {v2[2]}")
print("Le produit scalaire de v1 par v2 vaut", pro)

#ex4 Partie 1 :
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
L2 = []
mm=0
for i in range (0,10):
    L2.append(0)
a=0
l=(len(L1))
for i in range (0,l):
    a=L1[i]
    L2[a]= L2[a]+1
print(L1)
b=max(L2)
z=L2.index(b)
p=b
mm=z
del L2[z]
d=max(L2)
r=L2.index(d)+1
if b==d:
    p=d
    for i in range(l-1,-1,-1):
        if L1[i]==r:
            mm=z
            break
        elif L1[i]==z:
            mm=r
            break
        else:
            mm=0
print(f"Le nombre le plus frequent dans la liste est le :{mm} ({p}x)")


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
