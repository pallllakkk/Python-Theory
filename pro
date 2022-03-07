cp=float(input("Enter the cost price"))
sp=float(input("Enter the selling price"))
if(sp>cp):
  pro=sp-cp
  print("Profit=",pro)
elif(cp>sp):
  loss=cp-sp
  print("Loss=",loss)
else:
  print("No profit no loss")
