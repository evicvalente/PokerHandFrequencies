"""
@author: Emma Valente

This program will help someone figure out how likely
a flush, one pair, two pair, and high card hand
is in a simplified version of the game of Poker.
"""

import deck as decks
import hand as hands
from flush import isFlush
from pairs import pairsCounting

def play_rounds():
    '''
    Main function that determines how likely a hand occurs.

    Creates deck and initializes counters and containers.
    Iterates 100,000 times, and for each iteration the deck is shuffled and a new hand is dealt.
    Checks if the hand is a flush, one pair, two pair, or high card, and increases its respective counter by 1.
    Appends result to respective containers once iterations reach 100,000.
    Creates list with bins for number of hands, then creates and fills lists for shares of different hands.
    Prints the results table.


    :return:
    '''
    deck = decks.createDeck()

    iterations_n = 0
    pairs_counters = []
    two_pairs_counters = []
    flushes_counters = []
    high_cards_counters = []
    pairs_counter = 0
    two_pairs_counter = 0
    flushes_counter = 0
    high_cards_counter = 0

    for i in range(1, 100000 + 1):

        decks.shuffleDeck(deck)

        hand = hands.dealCards(deck)

        if isFlush(hand) == True:
            flushes_counter = flushes_counter + 1
        elif pairsCounting(hand) == 2:
            two_pairs_counter = two_pairs_counter + 1
        elif pairsCounting(hand) == 1:
            pairs_counter = pairs_counter + 1
        else:
            high_cards_counter = high_cards_counter + 1

        iterations_n = iterations_n + 1

        if iterations_n == 10000:
            pairs_counters.append(pairs_counter)
            two_pairs_counters.append(two_pairs_counter)
            flushes_counters.append(flushes_counter)
            high_cards_counters.append(high_cards_counter)
            iterations_n = 0

    bins = list(range(10000, 100000 + 1, 10000))

    pairs_shares = []
    two_pairs_shares = []
    flushes_shares = []
    high_cards_shares = []
    for i in range(0, len(bins)):
        pairs_shares.append(100 * pairs_counters[i] / bins[i])
        two_pairs_shares.append(100 * two_pairs_counters[i] / bins[i])
        flushes_shares.append(100 * flushes_counters[i] / bins[i])
        high_cards_shares.append(100 * high_cards_counters[i] / bins[i])

    print("# of hands".rjust(12), end="")
    print("pairs".rjust(10), end="")
    print("%".center(10), end="")
    print("2 pairs".rjust(10), end="")
    print("%".center(10), end="")
    print("flushes".rjust(10), end="")
    print("%".center(10), end="")
    print("high card".rjust(10), end="")
    print("%".center(10))
    for i in range(0, len(bins)):
        print(format(bins[i], ',d').rjust(12), end="")
        print(str(pairs_counters[i]).rjust(10), end="")
        print("{0:05.2f}".format(pairs_shares[i], '02d').center(10), end="")
        print(str(two_pairs_counters[i]).rjust(10), end="")
        print("{0:05.2f}".format(two_pairs_shares[i], '02d').center(10), end="")
        print(str(flushes_counters[i]).rjust(10), end="")
        print("{0:05.2f}".format(flushes_shares[i], '02d').center(10), end="")
        print(str(high_cards_counters[i]).rjust(10), end="")
        print("{0:05.2f}".format(high_cards_shares[i]).center(10))

if __name__ == "__main__":
    play_rounds()