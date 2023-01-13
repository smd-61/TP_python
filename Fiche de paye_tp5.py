heure=int(input("Combien d\'heure a-t-il travaillé"))
prix=int(input("Quel est le salire/heure?"))
if heure>160:
    if heure >200:
        n50=heure-200
        n25=40
        n=160
    else:
        n25 = heure-160
        n = 160
        n50=0
else:
    n=heure
    n25 = 0
    n50 = 0

final=(n*prix)+n25*(prix*1.25)+n50*(prix*1.50)

print("Le salaire final du salarié est donc de", final, "euros")