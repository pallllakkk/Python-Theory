l=int(input("Enter l"))
r=int(input("Enter r"))
u=0
for i in range(l,r+1):
    for j in range(l,r+1):
        p=i^j
        if p>u:
            u=p
print(u)
