Z=1
x=0
for i in range (0,5):
    a=str(input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant :"))
    K=a.split()
    Z+=float(K[0])*int(K[1])
    if float(K[0])<8:
        x=1

if x==1 or  Z<10:
    print("L'élève n\'est pas admis")
else:
    print("L'élève est admis")