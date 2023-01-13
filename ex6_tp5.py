T=input("t")
i=0
z=0
y=0
x=0
o=0
while x==0:
    if T[i]=="0":
        x=i
    else:
        i+=1
for i in range (0,x):
    if T[i]==("a" or "e" or "i" or "o" or "u" or "y"):
        z+=1
    else:
        y+=1
moy=(100*z)/y

for i in range (0,x-4):
    if T[i]=="w":
        if T[i+1] == "a":
            if T[i+2] == "g":
                if T[i+3] == "o":
                    if T[i+4] == "n":
                        o+=1

if o==1:
    print ("Il y a une fois le sous tableau wagon")
elif o>1:
    print(f"Il y a {o} fois le sous tableau wagon")
else:
    print("Il n'y a pas le sous tableau wagon")