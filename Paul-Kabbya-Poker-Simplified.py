import random
'''
This program will simulate a game of poker with a standard deck of 52 cards,
4 suits, 13 cards per suit in the arrangement of A (Ace or 1), 2, 3, 4, 5, 6, 
7, 8, 9, 10, J (Jack or 11), Q (Queen, or 12), and K (King or 13).
In this simulation, instead of Jack, Queen and King, we'll use 11, 12, and 13.

It will be a poker game between two players. One player will be the user and
the second will be a computerized opponent. Said opponent will play on its
own terms, meaning its moves will be made without taking into account the moves
of the user.

The rules will be the same as standard poker: 
    Each player gets dealt two cards.
    They either bet or fold.
        For the sake of simplicity, there will be no set bet amount and no
        all-in scenarios
    If both players bet, a river will be revealed, starting with 1 card, then
        a round of betting, then one more card, one more betting round, and a 
        final third card to close the game and determine the winner.
    If after the river is revealed, one player decides to not bet, the win will
        automatically go the opponent.
    If after the river is revealed, both players decide to not bet anymore, the
        rest of the river will be revealed and the winner will be decided.
    Again, for the sake of simplicity, if both players have the same type of
    hand, it will automatically defer to making the player with the highest 
    card the winner.

This game will keep going as long as the user wants to keep playing.
'''
SUITS = ('Clubs', 'Spades', 'Diamonds', 'Hearts')
VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
WIN_METHOD = {1: 'high card', 2: '1 pair', 3: '2 pair', 4: 'triple',
              5: 'straight', 6: 'flush', 7: 'full house', 8: '4 of a kind', 
              9: 'straight flush', 10: 'royal flush'}

def game_choice(game_number): 
    #This function takes in the user's will to play poker
    #It is a separate function because it also checks for first and subsequent
    #requests to play
    if game_number == 0:
        play = input("Would you like to play some poker? Please enter Y/N ")
    
    else:
        play = input("Would you like to play again? Please enter Y/N ")
        
    return play

def deal(player_hand, comp_hand):
    #Deals cards, returning one card at a time
    #Uses the random library to make a shuffled deck
    #It takes in the hands of the players and the river to deal an unused card
    while True:
        random_card = (SUITS[random.randrange(len(SUITS))], 
                       VALUES[random.randrange(len(VALUES))])
        
        if random_card not in player_hand and random_card not in comp_hand:
            return random_card

def repeat_counter(values):
    #This function uses the values of the cards within a hand and the river to 
    #return if there are any repeat values in the set, and if so, what kind of
    #repeats are present
    repeat_max = 0
    
    for i in range(len(values)):
        #Counts the largest occurrence of repetition
        repeat_counter = 0
        for j in range(i+1, len(values)):
            if values[i] == values[j]:
                repeat_counter += 1
        
        if repeat_counter > repeat_max:
            repeat_max = repeat_counter

    if repeat_max == 3:       
        return 4 #4 of a kind
    else:
        hand = values[:2]
        river = values[2:]
        
        if hand[0] == hand[1]:
            if hand[0] not in river:
                return 2 #1 pair and only in the hand
            else:
                return 3 #Triple in the hand and river
        else:
            if hand[0] in river and hand[1] in river:
                if river.count(hand[0]) == 2 or river.count(hand[1]) == 2:
                    return [3, 2] #Full house counting
                else:
                    return [2, 2] #2 pair
            elif hand[0] in river or hand[1] in river:
                return 2 #1 pair spread between river and hand
                
        return 1 #In case there are no repeats

def hand_type(hand):
    ##This function determines the hand type
    values = []
    suits = []
    #These following variables check for straights and flushes
    same_suits = True
    straight = True
    
    for i in hand:
        values.append(i[1]) #Used for every kind of hand other than flushes
        suits.append(i[0]) #Used for flushes
    
    if len(hand) == 2:
        #This is to chheck for a high card scenario wherein only the cards in
        #the hand are accounted for
        return max(values) 
    
    repeats = repeat_counter(values)
    #The following variable checks is going to be used for straights
    values.sort()
    
    for suit in range(len(suits) - 1):
        #Determining if there is a flush
        if suits[suit] != suits[suit + 1]:
            same_suits = False
            break
    
    for value in range(len(values) - 1):
        #checks for straights, accounting for repeats as well
        if values[value + 1] - values[value] > 1 or values[value + 1] - values[value] == 0:
            straight = False
            break
    
    #The function will return a number values so that they can be easily 
    #compared to determine who the winner is
    #The number is returned is based on the WIN_METHOD dictionary at the top
    if same_suits:
        if values == [1, 10, 11, 12, 13]:
            return 10 #Royal flush
        elif straight: 
            return 9 #Straight flush
        else:
            return 6 #flush
            
    if straight:
        return 5 #Straight
    
    if repeats == 4:
        return 8 #4 of a kind
    elif repeats == [3, 2]:
        return 7 #Full house
    elif repeats == 3:
        return 4 #Triple
    elif repeats == [2, 2]:
        return 3 #2 pair
    elif repeats == 2:
        return 2 #1 pair
    else:
        return 1 #High card
        
def hand_reveal(player_hand, comp_hand):
    #This function actually reveals the hands to show who won
    player_hand_type = hand_type(player_hand)
    comp_hand_type = hand_type(comp_hand)
    
    print("Your hand is")
    for i in range(2):
        print('\t', player_hand[i][1], 'of', player_hand[i][0])

    print("The opponent's hand is")
    for i in range(2):
        print('\t', comp_hand[i][1], 'of', comp_hand[i][0])
    
    print('The river is')
    for i in range(2, 5):
        print('\t', comp_hand[i][1], 'of', comp_hand[i][0])
    
    if len(player_hand) > 4: 
        #This will only come up in an end of round scenario where all of the 
        #river is revealed so that is accounted for
        if player_hand_type == comp_hand_type:
            if hand_type(player_hand[:2]) == hand_type(comp_hand[:2]):
                return ('Tie', player_hand_type)
            else:
                return (hand_type(player_hand[:2]) > hand_type(comp_hand[:2]), player_hand_type)
        
        return (player_hand_type > comp_hand_type, player_hand_type, comp_hand_type)

    return None

def comp_decision(comp_with_river):
    #This function figures out if the computer will bet
    #It is done by checking what kind of hand the computer can make combined
    #with the river
    comp_values = []
    high_card = 0
    comp_hand = hand_type(comp_with_river)
       
    for i in comp_with_river:
        comp_values.append(i[1])
    
    high_card = max(comp_values[:2])
    
    if comp_hand > 1 or high_card > 8: #These are safe bets
        return True
    
    return False
                     
def play_poker():
    #This function runs the actual game of poker
    player_hand = []
    comp_hand = []
    river = []
    player_bet = True
    comp_bet = True
    
    for i in range(2): #Getting the players' hands
        player_hand.append(deal(player_hand, comp_hand))
        comp_hand.append(deal(player_hand, comp_hand))
        
    print('Your Hand is\n', player_hand[0][1], 'of', player_hand[0][0], '\n', 
          player_hand[1][1], 'of', player_hand[1][0])
    
    #Checking bets
    bet = input("Will you bet? Please enter Y/N ")
    
    if bet == 'N':
        player_bet = False
        
    comp_bet = comp_decision(comp_hand)
    
    #If one of the two players don't bet off the bat, the round is skipped
    if not player_bet and not comp_bet:
        hand_reveal(player_hand, comp_hand)
        return [None]
    elif not player_bet:
        hand_reveal(player_hand, comp_hand)
        return [None, 'player']
    elif not comp_bet:
        hand_reveal(player_hand, comp_hand)
        return [None, 'comp']
    else:
        for i in range(2):
            river.append(deal(player_hand+river, comp_hand+river))
            
            print("The river is")
            for riv in river:
                print(riv[1], 'of', riv[0])
        
            bet = input("Will you bet? Please enter Y/N ")
            
            if bet == 'N':
                player_bet = False
                
            comp_bet = comp_decision(comp_hand + river)
            
            #If both players decide to not bet, it will automatically go to the
            #end of the round
            if not comp_bet and not player_bet:
                for j in range(3-(i+1)):
                    river.append(deal(player_hand+river, comp_hand+river))
                    print(river[i][1], 'of', river[i][0])
                return hand_reveal(player_hand+river, comp_hand+river)
                
            #If only one player decides to not keep betting, it will
            #automatically grant the win to the opponent
            elif not comp_bet:
                hand_reveal(player_hand, comp_hand)
                return [True, "Opponent did not bet."]
            
            elif not player_bet:
                hand_reveal(player_hand, comp_hand)
                return [False, "You did not bet."]
            
    river.append(deal(player_hand+river, comp_hand+river))
    print("The river is")
    for card in river:
        print(card[1], 'of', card[0])

    return hand_reveal(player_hand+river, comp_hand+river)

def show_stats():
    #This function uses to file wherein the game records are stored to reveal
    #the player's final number of games played and games won
    stats = open('cps109_a1_output.txt', 'r')
    everything = stats.readlines()
    line = everything[-2:]
    
    first_line = ''
    
    for i in line[0]:
        if i == '-':
            break
        
        first_line+=i
    
    line[0] = first_line
    
    for i in line:
        print(i)
    
    stats.close()
    
    return 0

def main():
    #The main function in this program deals with the initial stages and the
    #post game of each round
    stats = open('cps109_a1_output.txt', 'w')
    stats.write("Rounds VS Wins:\n")
    
    game_number = 0
    win_count = 0
    win_statement = "Lost"
    win = False
    
    play = game_choice(game_number) 
    #game_number slightly alters the question of wanting to play again
    
    while play == 'Y': #To allow infinite games as long as the player wants     
        game_number+=1
        
        #The win variable determines the outcome of each round
        #It is list, with the first index holding a boolean or None or 'Tie' to
        #show the result of the game from the user's perspective
        win = play_poker()
        if win[0] == None: #If anyone folded from the start
            if len(win) > 1:
                if win[1] == 'player':
                    print('Since you folded off the bat, the round is skipped')
                elif win[1] == 'comp':
                    print('Since your opponent folded off the bat, the round is skipped')
            else:
                print('Since both of you folded, this round is skipped.')
            win_statement = "No play"
        elif win[0] == 'Tie':
            print('Tie Round, both players had a', WIN_METHOD[win[1]],
                  #WIN_METHOD is called to reveal the hand types
                  'with the same high card')
            win_statement = "Tie"
        elif win[0]:
            print("You WIN!")
            if type(win[1]) == int:
                print('Your hand was a', WIN_METHOD[win[1]])
            else:
                print(win[1])
            if len(win) > 2:
                print("Your opponent's hand was a", WIN_METHOD[win[2]])
            win_count+=1
            win_statement = "Won"
        else:
            print("You lost.")
            if type(win[1]) == int:
                print('Your hand was a', WIN_METHOD[win[1]])
            else:
                print(win[1])
            if len(win) > 2:
                print("Your opponent's hand was a", WIN_METHOD[win[2]])
            win_statement = "Lost"
            
        #The game is recorded and the question of a next game is asked
        stats.write('Games Played: '+ str(game_number) + ' ---- ' + win_statement + '\n')
        stats.write('Games Won: ' + str(win_count) + '\n')
        play = game_choice(game_number)
    
    else:
        print("\nGoodbye (for now >:))\n")
        
    stats.close()
    
    show_stats()
    
    return 0

main()
