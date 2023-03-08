# Function that calculates the number of pairs in hand:
def pairsCounting(cards):
    '''
    Gets a list of ranks from cards in a hand.
    Creates a new list of all unique ranks.
    Calculates the frequency of each unique rank in the hand.
    Calculates number of pairs based off of the rank's frequency (three of a kind is counted as a one pair).

    :param cards:
    :return pairs_n:
    '''
    all_ranks = [cards[0][0], cards[1][0], cards[2][0], cards[3][0], cards[4][0]]

    unique_ranks = []
    for i in all_ranks:
        if i not in unique_ranks:
            unique_ranks.append(i)

    counters = []
    for i in unique_ranks:
        counter = 0
        for j in all_ranks:
            if i == j:
                counter = counter + 1
        counters.append(counter)

    pairs_n = 0
    for i in counters:
        if i == 4:
            pairs_n = 2
            break
        elif i == 2 or i == 3:
            pairs_n = pairs_n + 1

    return pairs_n
