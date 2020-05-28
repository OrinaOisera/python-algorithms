import random

low = 0
high = 99
correct = False

ans = int((high + low )/2)

print("Please think of a number between 0 and 100!")

while not correct:
    ans = int((high + low )/2)
    print('Is your secret number ' + str(ans))
    fb = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")

    if fb == "h":
        high = ans
    elif fb == "l":
        low = ans
    elif fb == "c":
        correct = True
        print('Game over. Your secret number was: ' + str(ans))


    else:
        print("Sorry, I did not understand your input.")


