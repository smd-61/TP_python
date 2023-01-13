a=[]
b=[]
a=input("Entrer la phrase")

for i in range(0,len(a)):
    if a[i].isalpha()==True:
        b.append(a[i].lower())

a=b[::-1]


if a==b:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
