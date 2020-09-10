import random
from collections import Counter

# Boolean to track game win/lose condition
gameOver = False

# Replay function. This is called when the win or lose condition is met to prompt the user to either replay or exit
def replay():
    print("\nWould you like to play again? 1) Yes 2) No")
    validPlayAgain = False

    # Input bool loop that controls the play again or exit choice
    while (validPlayAgain == False):
        # Get user input
        playAgainChoice = input()
        # If said input is a digit, cast it as such
        if (playAgainChoice.isdigit()):
            playAgainChoice = int(playAgainChoice)
            # If the user entered 1, flip the game over bool flag which begins a new game
            if (playAgainChoice == 1):
                validPlayAgain = True
                # A bool to control the input loop
                gameOver = False           
            # If the user entered 2, print a goodbye message and exit the program
            elif (playAgainChoice == 2):
                validPlayAgain = True
                print("\nThank you for playing! Goodbye!")
                exit()
            # If the user entered anything else, provide an error message and reprompt
            else:
                print("Invalid choice. Please pick again.")
        # If the user did not enter a digit, capitalize their input
        else:
            playAgainChoice = playAgainChoice.upper()
            # If the user entered YES, flip the game over bool flag which begins a new game
            if (playAgainChoice == "YES"):
                validPlayAgain = True
                # A bool to control the input loop
                gameOver = False   
            # If the user entered NO, print the goodbye message and exit the program
            elif (playAgainChoice == "NO"):
                validPlayAgain = True
                print("Thank you for playing! Goodbye!")
                exit()
            # If the user entered anything else, provide an error message and reprompt
            else:
                print("Invalid choice. Please pick again.")

''' Main game logic function. Takes in a list of words for easy future expansion; simply pass in a word
    list from any of the other subject functions and this modular system will incorporate it seamlessly

    NOTE: In the future, I plan on looking into reading from text files to pull in arrays externally instead of
    manually hardcoding them '''
def game(wordList):
    # Setup of initial vars; 6 wrong guesses per word
    lives = 6
    # Word array that is populated with the passed in wordList
    words = []
    # Guessed letters array to store which letters the user has already (incorrectly) guessed
    guessedLetters = []
    # Bool flag to track if a letter has already been guessed
    alreadyGuessed = False
    # Populate the words array with the passed in wordList
    for word in wordList:
        words.append(word)

    # Amount of correct letters (used to track win condition)
    correctLetters = 0

    # Choose a random word from the word list
    chosenWord = words[random.randint(0, len(words)-1)]
    # Show the user how many letters are in the chosen word and print the appropriate amount of blanks
    print("\nYour word has: " + str(len(chosenWord)) + " letters in it.\n")
    blanks = "_ " * len(chosenWord)
    print(blanks)

    # Bool flag to track letter input
    validLetter = False
    # While the user has not yet entered a valid input
    while (validLetter == False):
        # If the user has any lives remaining
        if (lives > 0):
            # If the amount of correctly guessed letters is equal to the length of the secret word
            if (correctLetters == len(chosenWord)):
                # The user has won, print a congratulatory message and flip the game over bool flag to end the game
                print("\nYou won! Congratulations!")
                validLetter = True
                gameOver = True
                # Prompt for replay
                replay()
            # Otherwise, if the game is still going on
            else:
                # Prompt user for a letter
                letterInput = input("\nGuess a letter: ")
                  
                # If user input is NOT an alphabetical character, or the input is greater than a single char
                if (letterInput.isalpha() == False or len(letterInput) > 1):
                    # Prompt the user with an error message
                    print("Invalid input. Please only enter a single letter!")
                # The user input is valid (alphabetical)
                else:
                    # Capitalize input
                    letterInput = letterInput.upper()
                    # If there are no letters in the guessed letter in the array
                    if (len(guessedLetters) == 0):
                        # Save this guess 
                        guessedLetters.append(letterInput)
                    # Otherwise, if there is atleast 1 or more guessed letters
                    else:
                        # If the input is in the guessed letter array
                        if (letterInput in guessedLetters):
                            # Flip the bool flag to not reduce a life
                            alreadyGuessed = True
                            # Tell the user they've already guessed this letter
                            print("You've already guessed this letter. Please try again.\n")
                            print(blanks)
                        # Otherwise, if the input is not yet in the guessed letter array
                        else:
                            # Flip the bool flag to reduce a life
                            alreadyGuessed = False
                            # Add the guessed letter to the guessed letter array
                            guessedLetters.append(letterInput)

                    # Set number of correct letters in the word to 0
                    numCorrect = 0
                    # Set an index value to 0 (to keep track of the letters' positions in the word)
                    index = 0

                    # Counter that detects duplicate letters in a word
                    num = Counter(chosenWord)
                    result = []

                    # For each letter in the secret word
                    for i in chosenWord:
                        # If the inputted letter matches a letter in the word (guessed correctly)
                        if (letterInput == i):
                            # And if the player hasn't already guessed this letter
                            if (alreadyGuessed == False):
                                 # If there are multiple instances of that letter in the word
                                if (num[letterInput] > 1):
                                # Create an array and enumerate through the word, storing the indices of each duplicate
                                    indices = [index for index, element in enumerate(chosenWord) if element == i]
                                    for x in indices:
                                        if x not in result:
                                            result.append(x)
                                # If there is 1 or less instances of a letter
                                elif (num[letterInput] <= 1):
                                    # Increment the number of correct letters in the word by 1
                                    numCorrect += 1
                                    # Set the index value to the index of the input within the secret word
                                    index = chosenWord.index(letterInput)
                   
                    # For each element of the result array (letter positions)
                    for i in result:
                        # Increment the number of correct letters for each instance of that letter in the word
                        numCorrect += 1
                        # Set the index value to the index of the input within the secret word
                        index = chosenWord.index(letterInput)
                    
                    # If the user guessed a letter that is found once in the word
                    if (numCorrect == 1):
                        # Increment the correct letters (this is used to track win condition) 
                        correctLetters += 1   
                        # Tell them this
                        print("\nThere is " + str(numCorrect) + " " + letterInput + " in the word.")
                        ''' Update the blanks string, splicing in the guessed letter starting
                             at the beginning of the string up to index * 2 (because of whitespaces) and ending
                             at the char that's 1 index after that, until the end '''
                        blanks = blanks[:index * 2] + letterInput + blanks[(index * 2)+1:]
                        # Reprint the blanks with the updated letter(s)
                        print("\n" + blanks)
                    # If the user guessed a letter that is found more than once in the word
                    elif (numCorrect > 1):
                        # Increment the correct letters (this is used to track win condition) 
                        correctLetters += numCorrect
                        # Tell them this
                        print("\nThere are " + str(numCorrect) + " " + letterInput + "'s in the word.")
                        # For each element in the indices array created for duplicates
                        for j in result:
                            #Splice in the letters at each index a duplicate was found
                            blanks = blanks[:j * 2] + letterInput + blanks[(j * 2)+1:]
                        # Reprint the blanks string
                        print("\n" + blanks)
                        
                    # If the user guessed an incorrect letter
                    else:
                        # and if the user has not already guessed this letter
                        if (alreadyGuessed == False):
                            # Subtract a life
                            lives -= 1
                            # If the lives count is greater than 1 
                            if (lives > 1):
                                # Print a message using "lives" plural form
                                print("\nThere are no " + letterInput + "'s in the word. You have " + str(lives) + " lives remaining.\n")
                                print(blanks)
                            # If the lives count is exactly 1
                            elif  (lives == 1):
                                # Print a message using "life" singular form
                                print("\nThere are no " + letterInput + "'s in the word. You have " + str(lives) + " life remaining.\n")
                                print(blanks)
        # If the player has run out of lives
        else:
            # Flip bool flag to end the input loop
            validLetter = True
            # Flip bool flag to end the game
            gameOver = True
            # Print a game over message and show the user the word
            print("\nGAME OVER! The word was: " + chosenWord + ".\n")
            # Ask to replay 
            replay()
                        
        
def planets():
    # Planet word list
    planetWords = ['MERCURY', 'VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO']
    # Call the game function and pass in the above list
    game(planetWords)

def colors():
    # Color word list
    colorWords = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'PURPLE', 'ORANGE', 'BLACK', 'WHITE', 'PINK', 'BROWN', 'GREY', 'CHARTREUSE', 'TURQUOISE', 'MAGENTA', 'TEAL', 'MAROON', 'BEIGE']
    # Call the game function and pass in the above list
    game(colorWords)


def music():
    # Music genre word list
    musicWords = ['ROCK', 'METAL', 'POP', 'HIPHOP', 'TECHNO', 'RAP', 'BLUES', 'JAZZ', 'PUNK']
    # Call the game function and pass in the above list
    game(musicWords)
        
# Program Start

# If the game is not yet finished, run the intro
while (gameOver == False):
    print("\nWelcome to Hangman! Try to guess the word, but remember: you only have 6 lives! \nPick a subject: 1) Planets 2) Colors 3) Music")

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
            # Colors
            elif (choice == 2):
                validChoice = True
                colors()
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
            # If the choice was colors
            elif (choice == "COLORS"):
                # End the loop and run colors function
                validChoice = True
                colors()
            # If the choice was music 
            elif (choice == "MUSIC"):
                # End the loop and run music function
                validChoice = True
                music()
            # Otherwise, error message
            else:
                print("Invalid choice, please pick again.")
        
