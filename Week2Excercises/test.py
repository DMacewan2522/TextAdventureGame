passWord = "Secret"

for i in range(0, 3):
    userGuess = input("Attempt to guess my secret password: ")
    if userGuess == passWord:
        print("Well done, you guessed the password!")
        break
    elif userGuess != passWord and i < 2:
        print("Try Again")
    else:
        print("You Lose")