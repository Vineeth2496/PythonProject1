def reverse_digit(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    print(rev)
reverse_digit(7642)
