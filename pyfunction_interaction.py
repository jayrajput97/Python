example = [1,2,3,4,5,6,7]

#importing shuffle function
from random import shuffle

#shuffling the list (shuffle function does not return a value)
shuffle(example)
#printing list
print(f'First shuffle call: {example}')


#creating a function to return a shuffled value
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(f'Second shuffle call using function return: {result}')

#making a simple guessing game to guess where the 'O' is.
my_list = [' ','O',' ']
r = shuffle_list(my_list)

#shuffled list for the guessing game.
print(f'Third shuffle call, printing with variable: {r}')

#seperate function to get player input to guess the position of 'O'.
def player_guess():
    guess = ''
    #keeping loop to make sure the input is either 1,2 or 3
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2")

    #returning guessed value
    return int(guess)

def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print('Correct')
    else:
        print('Wrong Guess')
        print(my_list)

#shuffling list once more for the guess
mixed_list = shuffle_list(my_list)

#calling function to run the game
guess = player_guess()
check_guess(mixed_list, guess)
