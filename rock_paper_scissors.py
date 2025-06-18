import random

def rock_paper_scissors():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    #print(computer_choice) To check only
    player_choice = input("Please enter your choice: (Rock: 'R', Paper: 'P', Scissors: 'S')")
    if player_choice.lower() == 'r':
        if computer_choice == 'rock':
            print('Draw!')
        elif computer_choice == 'paper':
            print('I chose paper, you lose!')
        elif computer_choice == 'scissors':
            print('I chose scissors, you win!')
    elif player_choice.lower() == 'p':
        if computer_choice == 'rock':
            print('I chose rock, you win!')
        elif computer_choice == 'paper':
            print('Draw!')
        elif computer_choice == 'scissors':
            print('I chose scissors, you lose!')
    elif player_choice.lower() == 's':
        if computer_choice == 'rock':
            print('I chose rock, you lose!')
        elif computer_choice == 'paper':
            print('I chose paper, you win!')
        elif computer_choice == 'scissors':
            print('Draw!')
    else:
        print(ValueError('Please enter a valid choice.'))

print('Rock Paper Scissors')
print('Rules: ')
print('1. Rock beats Scissors')
print('2. Paper beats Rock')
print('3. Scissors beats Paper')
print('Make your choice')

while True:
    rock_paper_scissors()
    again = input('Would you like to play again? (y/n): ')
    if again.lower() == 'n':
        break
