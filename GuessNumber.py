number = 15
print("You have the only 5 Guesses")
no = 1
while no < 6:
    guess = int(input("Guess the number between 1-100:"))
    if guess < number:
        print("Please enter Grater Number ")
    elif guess > number:
        print("Please enter Small Number ")

    else:
        print("Congratulations,You Win")
        break
    print(5-no, "No of Guesses Remaining")
    no = no+1
if no == 6:
    print("Please try again ")
else:
    print("Thank you for Participating")
