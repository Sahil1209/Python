print("Enter the no of Num1:")
Num1=int(input())
print("Enter the no of Num2:")
Num2=int(input())

print("Enter the operation:")
opt=input()

if opt=='+':
    print("Sum of Num1 and Num2 =",Num1+Num2)
elif opt=='-':
    print("Submission of Num1 and Num2 =",Num1-Num2)
elif opt=='*':
    print("Multiplication of Num1 and Num2 =",Num1*Num2)
elif opt=='/':
    print("Division of Num1 and Num2 =",Num1/Num2)
else:
    print("Invalid operator")
