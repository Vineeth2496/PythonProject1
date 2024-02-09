'''
#Leap year
year=int(input("Enter year: "))

if year%4==0 and year%100!=0 or year%400==0:
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is NOT a leap year")
'''
'''
#Fabinocii
a=0
b=1
i=0
while i<=10:
    c=a+b
    a=b
    b=c
    print(b, ' ')
    i+=1
'''
'''
#Factorinal
n=int(input("Enter number: "))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print(f'factorial of number {n} is : {fact}')
'''
import string
str1=input('Enter String to check if it is palindrome')
str1=str1.casefold()
print(str1)



