import random
deck = [{"suit": "clubs", "value": 2, "worth" : 2},{"suit": "clubs", "value": 3, "worth" : 3},{"suit": "clubs", "value": 4, "worth" : 4},{"suit": "clubs", "value": 5, "worth" : 5},
    {"suit": "clubs", "value": 6, "worth" : 6},{"suit": "clubs", "value": 7, "worth" : 7},{"suit": "clubs", "value": 8, "worth" : 8},{"suit": "clubs", "value": 9, "worth" : 9},{"suit": "clubs", "value": 10, "worth" : 10},{"suit": "clubs", "value": "Jack", "worth" : 10},
    {"suit": "clubs", "value": "Queen", "worth" : 10},{"suit": "clubs", "value": "King", "worth" : 10},{"suit": "clubs", "value": "Ace", "worth" : 11},
    {"suit": "hearts", "value": 2, "worth" : 10},{"suit": "hearts", "value": 3, "worth" : 3},{"suit": "hearts", "value": 4, "worth" : 4},{"suit": "hearts", "value": 5, "worth" : 5},
    {"suit": "hearts", "value": 6, "worth" : 6},{"suit": "hearts", "value": 7, "worth" : 7},{"suit": "hearts", "value": 8, "worth" : 8},{"suit": "hearts", "value": 9, "worth" : 9},{"suit": "hearts", "value": 10, "worth" : 10},{"suit": "hearts", "value": "Jack", "worth" : 10},
    {"suit": "hearts", "value": "Queen", "worth" : 10},{"suit": "hearts", "value": "King", "worth" : 10},{"suit": "hearts", "value": "Ace", "worth" : 11},
    {"suit": "diamonds", "value": 2, "worth" : 2},{"suit": "diamonds", "value": 3, "worth" : 3},{"suit": "diamonds", "value": 4, "worth" : 4},{"suit": "diamonds", "value": 5, "worth" : 5},
    {"suit": "diamonds", "value": 6, "worth" : 6},{"suit": "diamonds", "value": 7, "worth" : 7},{"suit": "diamonds", "value": 8, "worth" : 8},{"suit": "diamonds", "value": 9, "worth" : 9},{"suit": "diamonds", "value": 10, "worth" : 10},{"suit": "diamonds", "value": "Jack", "worth" : 10},
    {"suit": "diamonds", "value": "Queen", "worth" : 10},{"suit": "diamonds", "value": "King", "worth" : 10},{"suit": "diamonds", "value": "Ace", "worth" : 11},
    {"suit": "spades", "value": 2, "worth" : 2},{"suit": "spades", "value": 3, "worth" : 3},{"suit": "spades", "value": 4, "worth" : 4},{"suit": "spades", "value": 5, "worth" : 5},
    {"suit": "spades", "value": 6, "worth" : 6},{"suit": "spades", "value": 7, "worth" : 7},{"suit": "spades", "value": 8, "worth" : 8},{"suit": "spades", "value": 9, "worth" : 9},{"suit": "spades", "value": 10, "worth" : 10},{"suit": "spades", "value": "Jack", "worth" : 10},
    {"suit": "spades", "value": "Queen", "worth" : 10},{"suit": "spades", "value": "King", "worth" : 10},{"suit": "spades", "value": "Ace", "worth" : 11}
    ]
# cash is the total money the player has
cash = 1000
def main(cash):
    # defining variables = Aced looks if you already counted an ace as 1
    # x is the player hand list y is dealer hand list
    aced = 0
    x = []
    y = []
    # putting 1 card in each hand
    card = deck[draw()]
    x.append(card)
    card = deck[draw()]
    y.append(card)
    # Taking a bet
    bet = betting(cash)
    # printing the dealer open face card
    print("Dealer First Card: " +str(card["value"]) + " of " + card["suit"])
    # result = total points / bust
    bet, x, style = play(x, aced, bet, cash)
    result = count(x, aced)
    dealer_result = count(dealer_play(y,aced), aced)
    # prints the final result comparing both hands
    outcome = compare(result, dealer_result)
    print(outcome)
    # checking the bets to hand out or take money from the total cash
    
    if outcome == "Player wins!" and style == "Double Down":
        print("You receive: " + str(bet) + "$")
        cash = cash + int(bet)
    elif outcome == "Player wins!":
        print("You receive: " + str(int(bet) * 1.5) + "$")
        cash = cash + int(int(bet) *1.5)
    if outcome == "The house wins!":
        print("You loose your bet: " + str(bet) + "$")
        cash = cash - int(bet) 
    if outcome == "Player wins!, Dealer Busted":
        print ("You receive: " + str(bet))
        cash = cash + int(bet)
    # printing current cash and asking if wants to keep going
    print("Your current cash: " + str(cash) +"$")
    play_again = input("Want to play again?: ").upper()
    if play_again == "YES":
        print("")
        print("")
        main(cash)
# random number generator for indexing the deck
def draw():
    n = random.randint(0,51)
    return n
# player play function
def play(x, aced, bet, cash):
    # adds anothercard to the deck
    card = deck[draw()]
    x.append(card)
    # prints the new card + the hand so far + the current score
    print("New card " +str(card["value"]) + " of " + card["suit"])
    print("Your Current Deck ", end='')
    for i in range(len(x)):
        print(str(x[i]["value"]) + " of " + x[i]["suit"] + " ", end='')
    print(" ")
    print("Current score "  + str(count(x, aced)))
    # Checks for bust, if busted, returns the deck and ends play
    style = "normal"
    if str(count(x, aced)) == "Bust":
        return bet, x
    # asking if player wants another card, if it does calls plays recursively
    else:
        answer = input("Want to draw again? (Type: YES, Double Down, ) ").upper()
        if answer == "YES":
            play( x, aced, bet, cash)
        if answer == "DOUBLE DOWN":
            bet, x, check = double_down(bet, x, aced, cash)
            style = "Double Down"
            if check == "Not enough cash":
                print("Not enough cash, you'll hit")
                play( x, aced, bet, cash)
            return bet, x, style
    #if answer is no returns the deck
    return bet, x, style

# Calculates the score 
def count(playerdeck, aced):
    # setting var points
    points = 0
    # assining points for each card in hand
    for i in range(len(playerdeck)):
        points = playerdeck[i]["worth"] + points
    # if busted
    if points > 21:
        #first checks if you have an ace that can be converted, if there is, it rests 10 points giving a second chance
        for i in range(len(playerdeck)):
            if playerdeck[i]["value"] == "Ace":
                aced += 1
        # In the rare case that player has up to 3 aces and is over 21
        if aced >= 1:
            if points > 21 and points < 31:
                points -= 10
                return points
            if points > 31 and points < 41 and aced >= 2:
                points -= 20
                return points
            if points > 41 and aced >= 3:
                points -= 30
                return points


        # if > 21 returns bust
        return "Bust"
    # if < 21 returns the score
    else:
        return points
# dealer playing function
def dealer_play(y, aced):
    # adds new card to deck
    card = deck[draw()]
    y.append(card)
    # if it busts or is > 17 returns the hand
    if count(y,aced) == "Bust" or count(y, aced) > 17:
        return y
    # if is < 17 recursively calls the same function
    elif count(y, aced) < 17:
        dealer_play(y, aced)
    # ends the function
    return y

# comparing  player and dealer hand
def compare(result, dealer_result):
    # no busts and player > dealer
    if result != "Bust" and dealer_result != "Bust" and result > dealer_result:
        print("Your result: " + str(result) +", Dealer result: " + str(dealer_result))
        return "Player wins!"
    # no busts dealer > player
    elif result != "Bust" and dealer_result != "Bust" and result < dealer_result:
        print("Your result: " + str(result) +", Dealer result: " + str(dealer_result))
        return "The house wins!"
    # no busts tie
    elif result != "Bust" and dealer_result != "Bust" and result == dealer_result:
        print("Your result: " + str(result) +", Dealer result: " + str(dealer_result))
        return "It's a tie!"
    # player bust
    elif result == "Bust":
        print("You busted")
        return "The house wins!"
    # player no bust dealer busts
    else:
        print("Your result: " + str(result) +", Dealer result: " + str(dealer_result))
        return "Player wins!, Dealer Busted"

def betting(cash):
    #Checks if you have enough money
    print("Current cash: " + str(cash) + "$")
    bet = input("What amount would you like to bet ($)?: ")
    if int(bet) > cash:
        print("You don't have enough money!")
        betting(cash)
    return bet

def double_down(bet, x, aced, cash):
    # If you have enough money to double down, doubles the bet and draws the final card
    card = deck[draw()]
    x.append(card)
    print("New, and final card " +str(card["value"]) + " of " + card["suit"])
    print("Your Current Deck ", end='')
    for i in range(len(x)):
        print(str(x[i]["value"]) + " of " + x[i]["suit"] + " ", end='')
    print(" ")
    print("Current score "  + str(count(x, aced)))
    if (int(bet)*2) <= cash:
        return (int(bet)*2), x, "Enough cash"
    return bet, x, "Not enough cash"


main(cash)