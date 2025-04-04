# Import random operation
import random

# define main function
def main():
    max_number, guesses, secret = difficultySelect()
    if max_number: # Make sure guess is in range
        gameLoop(guesses, secret, max_number)

# define difficultySelect
def difficultySelect():
    print('1.) Easy   (Number Range: 1-25    ; Guesses: 5)')
    print('2.) Medium (Number Range: 1-100   ; Guesses: 8)')
    print('3.) Hard   (Number Range: 1-1000  ; Guesses: 12)')
    
    # Get the difficulty level from the user
    difficulty = int(input('Difficulty Level: '))
    
    # Set up game parameters based on difficulty
    if difficulty == 1:
        max_number = 25
        guesses = 5
    elif difficulty == 2:
        max_number = 100
        guesses = 8
    elif difficulty == 3:
        max_number = 1000
        guesses = 12
    else: 
        print('Invalid input, quitting game...')
        return None, None, None
    
    # Generate the secret number using randint()
    secret = random.randint(1, max_number)
    
    # Prompt user and return values
    print('\nI am thinking of a number between 1 and {}' .format(max_number))
    print('You have {} guesses.\n'.format(guesses))

    return max_number, guesses, secret

# defome gameLoop
def gameLoop(guesses, secret, max_number):
    for guess_num in range(guesses):
        # Get the player's guess
        guess = int(input('Take a guess (1-{}): '.format(max_number)))
        
        # Validate the guess within the correct range for the difficulty
        if guess < 1 or guess > max_number:
            guesses_left = guesses - guess_num -1
            print('Invalid input, guess must be within 1 and {}.' .format(max_number))
            print('You have {} guesses left.\n'.format(guesses_left))
            continue

        # Check if the guess is correct
        if guess == secret:
            print('Good job! You guessed my number!')
            return
        
        # Give a hint
        if guess < secret:
            print('The number is higher.')
        else:
            print('The number is lower.')
        
        # Tell them how many guesses are left
        guesses_left = guesses - (guess_num + 1)
        if guesses_left > 0:
            print('You have {} guesses left.\n'.format(guesses_left))
    
    # If they run out of guesses
    print('\nSorry, you ran out of guesses. The number was {}.' .format(secret))

# Begin program execution
main()
input('press any key to exit main')


