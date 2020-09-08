def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

num=int(input("Enter the factorial number for iterative method:"))
print("Factorian using iierative method:", factorial_iterative(num))

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n* factorial_recursive(n-1)

num=int(input("Enter the factorial number for recursive method:"))
print("Factorian using recursive method:", factorial_recursive(num))
