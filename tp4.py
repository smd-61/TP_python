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
L1 = [2, 7, 5, 7, 1, 6, 2, 1, 7, 6,6 ,6]
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

#Partie2
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
a=0
b=0
i=0
for i in range(0, len(L1)):

        if L1.count(L1[i]) >a :
            a=L1.count(L1[i])
            b=L1[i]
print(f"Le nombre le plus frequent dans la liste est le :{b} ({a}x)")

#exercice 5
q=0
a=0
b=0
c=0
z=0
y=0
u=0
r=0
R=[]
T=input("Donner la date")
if len(T)==8:
    for i in range (0,8):
        R.append(int(T[i]))
    a=R[0]*10+R[1]
    b=R[2]*10+R[3]
    c=R[4]*1000+R[5]*100+R[6]*10+R[7]

    if b>12 or b<=0:
        print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
    elif b==(1 or 3 or 5 or 7 or 8 or 10 or 12):
        z=1
        r = 1
    else :
        z=2
        r = 1
    if  (c%4==0 and c%100!=0) or c%400==0:
        y=4


    if b==2:
        if y==4:
            if a<=0 or a>29:
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
        else:
            if a<= 0 or a > 28:
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
            else:
                u=5
    else:
        if z==1:
            if a<=0 or a>31:\
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
        else:
            if a<=0 or a>30:
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
            else:
                u=5
    if u==5 and r==1:
        print("La date est correcte")
else:
    print("La date es incorrecte")

#exercice6
T=[5, 2, 4, 8, 1, 3]
a=0
print(T)
for i in range (0,len(T)):
    a, z = T[i], i
    for j in range (i+1,len(T)):
        if T[j]<a:
            a=T[j]
            z=j

    T[i],T[z]=T[z],T[i]
    print(T)

T=[5, 2, 4, 8, 1, 3]

print(sorted(T))
T.sort()
print(T)

#exercice7
a=input("Entrer votre login")
b=input("Entrer celui de votre voisin")
binome=(a,b)
print(f"L’étudiant {a} est en binome avec l’étudiant {b}")

#exercice8
dico = {}
dico['nom'] = 'toto'
dico['prénom'] = 'titi'
dico['promo'] = '2023'
dico['groupe'] = '202'

dic = {}
dic['nom'] = 'tata'
dic['prénom'] = 'tutu'
dic['promo'] = '2023'
dic['groupe'] = '102'

binome = {}
binome['élève1']= dico
binome['élève2']= dic


print(f"Votre nom est {dico['nom']}, votre prénom est {dico['prénom']}, vous faites partie de la promo {dico['promo']} et votre groupe est {dico['groupe']}")
print("Les clés du dictionnaire sont :")
for cle, valeur in dico.items():
    print("-",cle)

print("Les valeurs du dictionnaire sont :")
for cle, valeur in dico.items():
    print("-",valeur)

print("Les tuplets du dictionnaire sont :")
for valeur in dico.items():
    print("-",valeur)


print("Les étudiants formants le binôme sont :")


print(f"- L'étudiant {binome['élève1']['nom']} {binome['élève1']['prénom']} du groupe {binome['élève1']['groupe']}")
print(f"- L'étudiant {binome['élève2']['nom']} {binome['élève2']['prénom']} du groupe {binome['élève2']['groupe']}")
