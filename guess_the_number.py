import random

def guess_the_number(rand_number, guess):

    if guess < rand_number:
        print('Too low')
    elif guess > rand_number:
        print('Too high')
    else:
        return


x = random.randint(1, 100)
tries = 0
while True:
    try:
        #print(x)
        y = int(input('Guess a number between 1 and 100: '))
        tries += 1
        guess_the_number(x, y)
        if x == y:
            if tries == 1:
                print('You got it on your first try!')
            else:
                print('You guessed it in ' + str(tries) + ' tries!')
            again = input('Do you want to play again? (y/n): ')
            if again.lower() == 'n':
                break
            else:
                x = random.randint(1, 100)
                tries = 0
    except ValueError:
        print('Please enter a valid number!')
