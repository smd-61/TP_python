import os.path
import datetime
x=1
a=input("Entrer le nom du premier fichier (ex: f1.txt)")
b=input("Entrer le nom du deuxième fichier(ex: f2.txt)")
if os.path.isfile(a) == True:
    c=os.path.getsize(a)
    print("La taille du 1er fichier est de",c,"octets")
else:
    print("Ce fichier n'existe, pas dans le répertoire courant.")
    x=0

if os.path.isfile(b) == True:
    d = os.path.getsize(b)
    print("La taille du 2ème fichier est de",d,"octets")
else:
    print("Ce fichier n'existe, pas dans le répertoire courant.")
    x=0

if x==1:
    if (os.path.getmtime(a))>(os.path.getmtime(b)):
        print(f"Le fichier qui a été modifier en dernier est le fichier {a}, le {datetime.datetime.fromtimestamp(os.path.getmtime(a))}")
    elif (os.path.getmtime(a))<(os.path.getmtime(b)):
        print(f"Le fichier qui a été modifier en dernier est le fichier {b}, le {datetime.datetime.fromtimestamp(os.path.getmtime(b))}")
    else:
        print(f"Les fichiers ont été modifier en même temps le: {datetime.datetime.fromtimestamp(os.path.getmtime(a))}")
