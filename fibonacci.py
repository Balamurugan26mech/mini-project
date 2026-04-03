def nat(n):
    print("Natural number series: ")
    for i in range(1, n+1):
        print(i, end=" ")
    print()

def eve(n):
    print("Even numbers series: ")
    for i in range(2, n+1, 2):
        print(i, end=" ")
    print()

def odd(n):
    print("Odd number series: ")
    for i in range(1, n+1, 2):
        print(i, end=" ")
    print()

def fib(n):
    print("Fibonacci number: ")
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

print("1=Natural Number")
print("2=Even number")
print("3=Odd Number")
print("4=Fibonacci Number")

m = int(input("Enter number: "))
choice = int(input("Enter choice: "))

if choice == 1:
    nat(m)
elif choice == 2:
    eve(m)
elif choice == 3:
    odd(m)
elif choice == 4:
    fib(m)
else:
    print("Invalid Input")