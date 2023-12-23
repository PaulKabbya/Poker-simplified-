# Poker-simplified-
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
