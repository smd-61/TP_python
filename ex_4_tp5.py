a=int(input("Entrer la somme d'argent"))
z=a
b=a//100
a=a%100
c=a//50
a=a%50
d=a//10
a=a%10
e=a//2
f=a%2
print(f"{z} euros, c’est donc {b}billets de 100, {c} de 50, {d} de 10, {e} pièces de 2 et {f} pièce 1.")