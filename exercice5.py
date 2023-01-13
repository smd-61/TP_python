q=0
a=0
b=0
c=0
z=0
y=0
u=0
r=0
R=[]
T=input("Donner la date")
if len(T)==8:
    for i in range (0,8):
        R.append(int(T[i]))
    a=R[0]*10+R[1]
    b=R[2]*10+R[3]
    c=R[4]*1000+R[5]*100+R[6]*10+R[7]

    if b>12 or b<=0:
        print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
    elif b==(1 or 3 or 5 or 7 or 8 or 10 or 12):
        z=1
        r = 1
    else :
        z=2
        r = 1
    if  (c%4==0 and c%100!=0) or c%400==0:
        y=4


    if b==2:
        if y==4:
            if a<=0 or a>29:
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
        else:
            if a<= 0 or a > 28:
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
            else:
                u=5
    else:
        if z==1:
            if a<=0 or a>31:\
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
        else:
            if a<=0 or a>30:
                print(f"La date {T[0]}{T[1]}/{T[2]}{T[3]}/{T[4]}{T[5]}{T[6]}{T[7]} est incorrecte")
            else:
                u=5
    if u==5 and r==1:
        print("La date est correcte")
else:
    print("La date es incorrecte")
