import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False
range = 100
while not quit:
    #random_number = random.randint(1, range)
    #testing for right on first try code
    random_number = 50
    count = 0
    number = -1
    while number != random_number:
        number = input("Please guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("Please guess a number!")
        elif number != random_number:
            number = int(number)
            count = count + 1
            print("Sorry, that number is incorrect")
            if number > random_number:
                print("Too high!")
            elif number < random_number:
                print("Too low!")
        else:
            print("You are correct!")
        if count == 10:
            print("\nYour guesses are too random. Try starting with 50.")
            print("\nIf your guess is too high choose a number halfway between 50 and 100")
            print("\nIf your guess is too low choose a number halfway between 1 and 50")
            print("\nIf you keep guessing halfway between the lower and higher values you can find the number a lot faster!")
    if count == 1:
        print("Amazing!!!")
    else:
        print("Good job!")
    print("You guessed it in {} tries!".format(count))
    play_again = input("\nWould you like to play again (yes or no)?")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True
print("\n\nThank you for playing! See you later!")