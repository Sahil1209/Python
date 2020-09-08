while(True):
    A=int(input("Enter a number:"))
    if A>100:
        print("You have entered a number which is greater than 100")
        break
    else:
        print("Please try again the number you entered is less than 100")
        continue
