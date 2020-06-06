import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
            
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: "+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank=="Ace":
            self.aces+=1

    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

class Chips:
    
    def __init__(self):
        self.total = 1000
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        
        try:
            chips.bet = int(input("Please enter your bet: "))
        except:
            print("Whoops! Please enter an integer. ")
            continue
        else:
            if chips.bet>chips.total and chips.total>=1000:
                print("Sorry, your bet is greater than the amount of chips you have, {}.".format(chips.total))
                continue
            elif chips.bet<=0:
                print("Sorry, your bet must be more than 0.")
                continue
            else:
                print("A bet of {} will be placed! ".format(chips.bet))
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        h_or_s= input("\nEnter 'h' to hit or 's' to stand.\n")
        if h_or_s[0].lower()=='h':
            hit(deck,hand)
        elif h_or_s[0].lower()=='s':
            print("Player Stands. Dealer's turn")
            playing = False
            
        else:
            print("Oops, please enter h or s only!")
            continue
        break
        
def show_some(player,dealer):
    print("Dealer's Hand:")
    print("first card hidden")
    print(dealer.cards[1])
    print("\n")
    print("Player's Hand:")
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player's Hand:")
    for card in player.cards:
        print(card)

def player_busts(player, dealer, chips):
    print("\nPlayer Busts!")
    chips.lose_bet()
def player_wins(player, dealer, chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("\nDealer Busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("\nDealer Wins.")
    chips.lose_bet()

def push(player, dealer):
    print("\nPlayer and Dealer tie. PUSH!")



while True:
    # Print an opening statement
    print("Welcome to Blackjack! You start with 1000 chips. Remember the objective to stay under 21! An Ace can be 11 or 1. Good Luck!\n")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand, dealer_hand, player_chips)
            break


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value<=21:
        
        while dealer_hand.value<17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        
        if player_hand.value>dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        
        else:
            push(player_hand,dealer_hand)


    # Inform Player of their chips total 
    print("\nYour chip total is now {}".format(player_chips.total))
    # Ask to play again
    restart = input("Would you like to play again? 'y' or 'n'?")
    if restart[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break