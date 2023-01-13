
x=0

a=str(input("Veuillez entrer la note du module 1 et le coefficient correspondant :"))
K=a.split()
b=str(input("Veuillez entrer la note du module 2 et le coefficient correspondant :"))
L=b.split()
c=str(input("Veuillez entrer la note du module 3 et le coefficient correspondant :"))
M=c.split()
d=str(input("Veuillez entrer la note du module 4 et le coefficient correspondant :"))
N=d.split()
e=str(input("Veuillez entrer la note du module 5 et le coefficient correspondant :"))
O=e.split()
Z=(float(K[0])*int(K[1])+float(L[0])*int(L[1])+float(M[0])*int(M[1])+float(N[0])*int(N[1])+float(O[0])*int(O[1]))/5
if ((int(K[0]) or int(L[0]) or int(M[0]) or int(N[0]) or int(O[0]))<8) or  Z<10:
    print("L'élève n\'est pas admis")
else:
    print("L'élève est admis")