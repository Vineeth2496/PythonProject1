n1=int(input("Enter number"))
flag=0
a=n1//2
print(a)
for i in range(a,2,-1):
  print(i)
  if n1%i==0:
    flag=1
    break

if flag==0:
  print(n1,"is prime no")
else:
  print(n1,"Not a prime")



















