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
