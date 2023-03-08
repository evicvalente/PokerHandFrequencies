def isFlush(cards):
    '''
    Checks if hand is a flush.
    If the suit is the same for all cards in a hand, the value True is assigned to variable hasHand.

    :param cards:
    :return hasHand:
    '''
    hasHand = False

    if cards[0][1] == cards[1][1] and cards[1][1] == cards[2][1] and cards[2][1] == cards[3][1] and cards[3][1] == \
            cards[4][1]:
        hasHand = True

    return hasHand