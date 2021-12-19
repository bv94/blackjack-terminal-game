import random

regular_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
would_like_to_play_again = True


def ace_agent(deck):
    if(11 in deck):
        if(sum(deck) > 21):
            for i in range(len(deck)-1):
                if(deck[i] == 11):
                    deck[i] = 1


def deal_cards(deck):
    random.shuffle(deck)
    return deck.pop()


def deal_initial_cards(deck):
    cards = []
    for i in range(2):
        cards.append(deal_cards(deck))
    return cards


def is_bust(cards):
    if(sum(cards) > 21):
        return True
    return False


def get_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def dealer_agent():
    dealer_deck = regular_deck.copy()
    dealer_cards = deal_initial_cards(dealer_deck)
    while((sum(dealer_cards) < 17)):
        dealer_cards.append(deal_cards(dealer_deck))
        ace_agent(dealer_cards)
    return dealer_cards


def print_all_card(dealer_cards, user_cards):
    print(f"your cards were {user_cards} which adds up to {sum(user_cards)}\n dealers cards were {dealer_cards} which adds up to {sum(dealer_cards)}\n")


while(would_like_to_play_again):
    # dealer_deck = regular_deck.copy()
    user_deck = regular_deck.copy()
    hit_or_stand = ""

    print("welcome to blackjack")
    user_cards = deal_initial_cards(user_deck)
    # dealer_cards = deal_initial_cards(dealer_deck)
    dealer_cards = dealer_agent()
    # print([[user_cards, user_deck], [dealer_cards, dealer_deck]])
    hit_or_stand = input(
        f"your cards are {user_cards}\nwould you like to hit or stand?\n>")
    while((hit_or_stand == "h" or hit_or_stand == "hit")):
        user_cards.append(deal_cards(user_deck))
        hit_or_stand = input(
            f"your cards are {user_cards}\nwould you like to hit or stand?\n>")

    if(is_bust(user_cards)):
        print("you are bust\n\n")
    elif(is_bust(deal_cards)):
        print("dealer is bust\n\n")
    else:

        if(get_sum(user_cards) > get_sum(dealer_cards)):
            print(
                "you win\n\n\n")

        else:
            print(
                "you lose\n\n\n")
    print_all_card(dealer_cards, user_cards)
    if(input("would you like to play again?\n 'y' for yes 'n' for no>" == "n")):
        would_like_to_play_again == False

print("thanx for playing, hope you play again :>")
