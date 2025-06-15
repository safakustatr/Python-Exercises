import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_the_ace(card_list):
    if sum(card_list) > 21:
        if 11 in card_list:
            card_list[card_list.index(11)] = 1
            return card_list
        else:
            return card_list
    else:
        return card_list

def draw(card_list):
    while sum(card_list) <= 16:
        card_list.append(random.choice(cards))
        card_list = check_the_ace(card_list)
    return card_list

def compare(card_list1, card_list2):
    if sum(card_list1) > sum(card_list2) or sum(card_list2) > 21:
        return 1
    elif sum(card_list1) < sum(card_list2) <= 21:
        return 2
    else:
        return 3

def blackjack(computer_cards, player_cards):
    while True:
        player_cards.append(random.choice(cards))
        player_cards = check_the_ace(player_cards)
        print(f"Your cards: {player_cards}, score: {sum(player_cards)}")
        print(f"Dealer's first card: {computer_cards[0]}")
        if sum(player_cards) > 21:
            print("You went over 21. You lose.")
            return
        if sum(player_cards) == 21 and len(player_cards) == 2:
            print("Win with Blackjack!")
            return
        choice = input("Type 'y to hit, type 'n' to stand: ")
        if choice == 'n':
            break
    computer_cards = draw(computer_cards)
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Dealer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    result = compare(player_cards, computer_cards)
    if result == 1:
        print("You win!")
    elif result == 2:
        print("You lose!")
    else:
        print("Draw!")

while True:
    choice = input("Do you want to play a game of Blackjack? (y/n): ")
    if choice == 'y':
        print("\n" * 20)
        print(art.logo)
        computer_cards = []
        player_cards = []
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        blackjack(computer_cards, player_cards)
    if choice == 'n':
        break