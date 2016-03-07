import random

number = float(0)


while number < 9:
    numero = random.random() * 3
    userChoice = raw_input(" Would you like to hit or stick?- press 1 for hit and 2 for stick ")
    userChoice = int(userChoice)
    if userChoice == 1:
        print(" Your new number is " + str(number + numero))
        number = float(number + numero)
    
    
    
    if userChoice == 2:
        if number < 6:
            print(" Your final number is " + str(number) + ", not close")
        if number == 6:
            print(" Your final number is " + str(number) + ", not close")
        if number > 6:
            print(" Your final number is " + str(number) + " Pretty close! ")
        
        if number > 8.5:
            print(" Your final number is " + str(number) + "SOO SOOO CLOSE")
        exit()
        
        

        
    
    
if number < 9.2:
     print(" You win! Congragulations! ")

else:
    print(" Sorry! Bust! ")

