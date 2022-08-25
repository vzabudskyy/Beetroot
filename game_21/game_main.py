import random


def get_deck():
    suits = ('♠️', '♣️', '♥️', '♦️')
    cards = ("6", "7", "8", "9", "10", "Valet", "Dama", "King", "Tuz")
    weight = (6, 7, 8, 9, 10, 2, 3, 4, 11)
    deck = []
    for suit in suits:
        for idx, nazva in enumerate(cards):
            card_weight = weight[idx]
            deck.append(
                (card_weight, suit, nazva)
            )
    return deck


def want_play():
    while True:
        user_answer = input("Do you want to play with me? If so, type 'Yes/Y'. If not, type 'No/N'\n")
        if user_answer.lower() == "yes" or user_answer.lower() == "y":
            return True
        elif user_answer.lower() == "no" or user_answer.lower() == "n":
            return False
        else:
            pass


def calculate_player_hand(cards):
    total_cards = 0
    for i in cards:
        total_cards += i[0]
    return total_cards


def display_user_cards(cards):
    for i in cards:
        print(f"Suit: {i[1]}\nCard: {i[2]}\n")
    print(f"Sum: {calculate_player_hand(cards)} \n\n")


deck = get_deck()
random.shuffle(deck)
player1 = [deck.pop(), deck.pop()]
computer = [deck.pop(), deck.pop()]
display_user_cards(player1)

while calculate_player_hand(player1) <= 21:
    if want_play():
        player1.append(deck.pop())
        display_user_cards(player1)
    else:
        break

if calculate_player_hand(player1) > 21:
    print("You lose")
else:
    while calculate_player_hand(computer) < random.randint(15, 19):
        computer.append(deck.pop())

    if calculate_player_hand(computer) > 21 or calculate_player_hand(computer) < calculate_player_hand(player1):
        print("You win!")
        print(f"Computer: {calculate_player_hand(computer)}")
    else:
        print("You lost!")
