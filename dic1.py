d={}
n= int(input("Enter n"))
d[1],d[2]=0,1
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
print(d)
© 2022 GitHub, Inc.
