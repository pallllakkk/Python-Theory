num=int(input("Enter no."))
i=10
eve=0
odd=0
while(i>0):
        if(i%2==0):
                a=num%10
                b=num//10
                num=b
                eve=eve+a
        else:
                a=num%10
                b=num//10
                num=b
                odd=odd+a
        i-=1
if(eve==odd):
        print("Magic No.")
else:
        print("Not a Magic No.")
