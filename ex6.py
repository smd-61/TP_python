T=[5, 2, 4, 8, 1, 3]
a=0
print(T)
for i in range (0,len(T)):
    a, z = T[i], i
    for j in range (i+1,len(T)):
        if T[j]<a:
            a=T[j]
            z=j

    T[i],T[z]=T[z],T[i]
    print(T)

T=[5, 2, 4, 8, 1, 3]

print(sorted(T))
T.sort()
print(T)