#ex1
nom="koc"
prenom="samed"
math=float(20)
anglais=float(12.3)
info=float(17.4)
promotion=2022
moy=(math+anglais+info)/3
type(nom)
type(prenom)
type(math)
type(anglais)
type(info)
type(promotion)
type(moy)
print("L\'étudiant ", nom, prenom, "de la promotion", promotion, "a une moyenne  de", moy)
L'étudiant  koc samed de la promotion 2022 a une moyenne  de 16.566666666666666

#ex2
jour=18
heure=14
minute=5
durée=jour*24*60+heure*60=minute
SyntaxError: cannot assign to expression
durée= jour*24*60+heure*60=minute
SyntaxError: cannot assign to expression
duree= jour*24*60+heure*60+minute
print(duree)
26765

#ex3
print("Quelle jour est-il?")
jour=int(input())
print("Quelle heure est-il?")
heure=int(input())
print("Quelle minute est-il?")
minute=int(input())

duree= jour*24*60+heure*60+minute
print(duree, "minute sont passés depuis le début du mois")

#ex4
print("Quelle est le numéro du mois?")
mois=int(input())
print("Combien de minutes ce sont écoulées depuis le début du mois?")
dur=int(input())
jour=dur//1440
dur=dur%1440
heure=dur//60
minute=dur%60
print("On est le", jour,"/",mois, "et il est", heure, "heure", minute, "minute")

#ex5
import random
a=random.randint(0,100)
print(a)
