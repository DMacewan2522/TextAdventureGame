passWord = "Secret"

counter = 3

while counter > 0:
    userGuess = input("Attempt to guess my secret password: ")
    if userGuess == passWord:
        print("Well done, you guessed the password!")
        break
    elif userGuess != passWord and counter > 1:
        print("Try Again")
        counter -= 1
    else:
        print("You Lose")
        break
