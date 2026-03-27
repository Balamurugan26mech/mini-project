def natural_numbers(n):
    print("natural numbers series:")
    for i in range(1,n+1):
        print(1,end=" ")
    print()

def even(n):
    print("even numbers series:")
    for i in range(2,n+1,2):
        print(i,end=" ")
    print()

def odd(n):
    print("odd numbers :")
    for i in range(1,n+1,2):
        print(i,end=" ")
    print()

def fib(n):
    print("fibonnaci series :")
    a,b = 0,1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b


print("1.natural number")
print("2.even")
print("3.odd")
print("4.fiboncii")

a = int(input("enter a number :"))
b = int(input("give ur choice : "))

if b == 1:
    print(natural_numbers(a))

elif b == 2:
    print(even(a))

elif b == 3:
    print(odd(a))

elif b == 4:
    print(fib(a))

else:
    print("error in input ")