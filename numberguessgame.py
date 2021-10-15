import random
play = 'y'

def game(ll, ul):
    if option<4:
            chances = 7
    else:
            chances = 10
    number = random.randint(ll, ul)
    print("\nIm thinking of a number between {} and {}".format(ll, ul))
    print("\nYou have 7 chances to guess the right number.\n")
    numberChoice = int(input("Guess the number -> "))
    
    while numberChoice != number:
        chances -= 1
        if chances>0:
            if numberChoice > ul or numberChoice < ll:
                print("\nInvalid input!\nPlease input a number between {} and {}".format(ll,ul))
            elif numberChoice > number and numberChoice < ul:
                print("\nA little too high! Remaining chances {}".format(chances))
            elif numberChoice < number:
                print("\nA little too low!! Remaining chances {}".format(chances))
            numberChoice = int(input("Please try again -> "))
        else:
            print("\nYou lost! The number was {}\n".format(number))
            break 
    else:
        print('\nCorrect!! Great Guess!\n')
    

while play.lower() != 'n':
    option = int(input("Enter Difficulty Level between 1 to 5 -> "))
    if option == 1:
                game(0,10)  
    elif option == 2:
        game(0,30)

    elif option == 3:
        game(0,100)
    
    elif option == 4:
        game(0,300)
    elif option == 5:
        game(0,500)
    play = input("Want to play again? (y/n) -> ")
print('Thank you for playing my game!')