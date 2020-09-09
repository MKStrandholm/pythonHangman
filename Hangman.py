import random

def game(wordList):
    lives = 5
    words = []
    for word in wordList:
        words.append(word)
        
    chosenWord = words[random.randint(0, 4)]
    print("Your word has: " + str(len(chosenWord)) + " letters in it.")
    blanks = "_ " * len(chosenWord)
    print(blanks)
    print("\n")
    
    validLetter = False
    while (validLetter == False):
        if (lives >= 0):
            letterInput = input("Guess a letter: ")
            letterInput = letterInput.upper()
            numCorrect = 0
            index = 0
            for i in chosenWord:
                if (letterInput == i):
                    # Guessed correctly
                    numCorrect += 1
                    index = chosenWord.index(letterInput)
            if (numCorrect == 1):
                print("There is " + str(numCorrect) + " " + letterInput + " in the word")
                print(blanks)
                blanks = blanks[:index * 2] + letterInput + blanks[(index * 2)+1:]
                print(blanks)
            elif (numCorrect > 1):
                print("There are " + str(numCorrect) + " " + letterInput + "'s in the word")
                blanks = blanks.replace(blanks[(index * 2)], letterInput)
            else:
                print("There are no " + letterInput + "'s in the word. You have " + str(lives) + " lives remaining.")
                lives -= 1
        else:
            validLetter = True
            gameOver = True
            print("\nGAME OVER!")    
            print("Would you like to play again? 1) Yes 2) No")
            validPlayAgain = False

            while (validPlayAgain == False):
                playAgainChoice = input()
                if (playAgainChoice.isdigit()):
                    playAgainChoice = int(playAgainChoice)

                    if (playAgainChoice == 1):
                        validPlayAgain = True
                        gameOver = False
                    elif (playAgainChoice == 2):
                        validPlayAgain = True
                        print("Thank you for playing! Goodbye!")
                        exit()
                    else:
                        print("Invalid choice. Please pick again.")
                else:
                    playAgainChoice = playAgainChoice.upper()
                    if (playAgainChoice == "YES"):
                        validPlayAgain = True
                        gameOver = False
                    elif (playAgainChoice == "NO"):
                        validPlayAgain = True
                        print("Thank you for playing! Goodbye!")
                        exit()
                    else:
                        print("Invalid choice. Please pick again.")
                        
        
def planets():
    # Planet word list
    words = ['MERCURY', 'VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO']
    # Call the game function and pass in the above list
    game(words)
        
# Program Start
# Boolean to track game win/lose condition
gameOver = False

# If the game is not yet finished, run the intro
while (gameOver == False):
    print("Welcome to Hangman! Pick a subject: 1) Planets 2) Video Games 3) Music")
    # A bool to control the input loop
    validChoice = False

    ''' While the player has not yet entered a valid choice for subject,
    and the game isn't over yet '''
    while (validChoice == False):
        # Get an input from the player
        choice = input()
        # If the input is a number
        if (choice.isdigit()):
            # Cast the input as an int to register the appropriate choices
            choice = int(choice)
            # Planets
            if (choice == 1):
                validChoice = True
                planets()
            # Video Games
            elif (choice == 2):
                validChoice = True
                videoGames()
            # Music
            elif (choice == 3):
                validChoice = True
                music()
            # Anything else
            else:
                print("Invalid choice, please pick again.")
        # If the input is not a number
        else:
            # Capitalize the input
            choice = choice.upper()
            # If the choice was planets
            if (choice == "PLANETS"):
                # End the loop and run planets function
                validChoice = True
                planets()
            # If the choice was video games
            elif (choice == "VIDEO GAMES"):
                # End the loop and run video games function
                validChoice = True
                videoGames()
            # If the choice was music 
            elif (choice == "MUSIC"):
                # End the loop and run music function
                validChoice = True
                music()
            # Otherwise, error message
            else:
                print("Invalid choice, please pick again.")
        
