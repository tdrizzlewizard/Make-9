import random

options = [1,2,3]

number = float(0)


while number < 9:
    numero = random.choice(options)
    userChoice = raw_input(" Would you like to hit or stick?- press 1 for hit and 2 for stick ")
    userChoice = int(userChoice)
    if userChoice == 1:
        print(" Your new number is " + str(number + numero))
        number = int(number + numero)
    
    
    
    if userChoice == 2:
        if number < 6:
            print(" Your final number is " + str(number) + ", not close")
        if number == 6:
            print(" Your final number is " + str(number) + ", not close")
        if number > 6:
            print(" Your final number is " + str(number) + " So close! ")
        exit
        



if number == 9:
    print(" You win! Congragulations! ")
    

elif number > 9:
    print(" Sorry! Bust! ")

