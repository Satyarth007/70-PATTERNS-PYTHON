#diamond pattern with fixed digit in every row
n=int(input("enter n:- "))
for i in range(n):
    print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))
for i in range(n-1):
    print(" "*(i+1)+(str(n-i-1)+" ")*(n-i-1))