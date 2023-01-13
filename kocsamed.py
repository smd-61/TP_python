a=str(input("Entrer votre nom sans caractère spéciaux"))
b=str(input("Entrer votre prénom sans caractère spéciaux"))
c=str(input("Entrer le 2ème nom sans caractère spéciaux"))
d=str(input("Entrer le 2ème prénom sans caractère spéciaux"))
x=0
if a>c:
    x=2
elif a<c:
    x=1
else:
    if b>d:
        x=2
    else:
        x=1

if x==1:
    print(b.capitalize(),a.upper())
    print(d.capitalize(), c.upper())
else:
    print(d.capitalize(), c.upper())
    print(b.capitalize(), a.upper())
