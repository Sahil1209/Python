n=18
number_of_guesses=1
while(number_of_guesses<=5):
    guess_number=int(input("Enter your guessed number:\n"))
    if guess_number>18:
        print("The number you entered is greater than the required one\n")
    elif guess_number<18:
        print("The number you entered is lesser than the required one\n")
    else:
        print("You won\n")
        print(number_of_guesses,"Number of guesses be took to finish")
        break

    print(5-number_of_guesses,"No. of guesses left")
    number_of_guesses=number_of_guesses+1
if(number_of_guesses>5):
    print("Game over")
