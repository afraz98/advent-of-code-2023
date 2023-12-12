card_ranking = "23456789TJQKA"
joker_card_ranking = "J23456789TQKA"

def nth_most_common(cards):
    return list(reversed(sorted([(card, cards.count(card)) for card in list(set(cards))], key=lambda x: x[1])))

def replace_jokers(cards):
    if cards == 'JJJJJ':
        return cards
    # Find the most common card in the hand that isn't a joker
    card_to_replace = list(map(lambda occurrences: occurrences[0], filter(lambda occurrences: occurrences[0] != "J", nth_most_common(cards))))[0]
    return cards.replace("J", card_to_replace)

def order(card):
    return card_ranking.index(card)

def is_five_of_a_kind(cards):
    return cards[0] == cards[1] == cards[2] == cards[3] == cards[4]

def is_four_of_a_kind(cards):
    for i in range(0,2):
        if cards[i] == cards[i+1] == cards[i+2] == cards[i+3]:
            return True
    return False

def is_full_house(cards):
    temp = list(cards)
    for i in range(0,3):
        if temp[i] == temp[i+1] == temp[i+2]:
            temp = [j for j in temp if j != temp[i]]
            return temp[0] == temp[1]
    return False

def is_three_of_a_kind(cards):
    for i in range(0, 3):
        if cards[i] == cards[i+1] == cards[i+2]:
            return True
    return False

def is_two_pair(cards):
    temp = cards
    for i in range(0, 4):
        if cards[i] == cards[i+1]:
            temp = [j for j in temp if j != temp[i]]
            for i in range(0, 2):
                if temp[i] == temp[i+1]:
                    return True
    return False

def is_pair(cards):
    for i in range(0, 4):
        if cards[i] == cards[i+1]:
            return True
    return False

def rank(hand):
    cards, bet = hand
    
    # Sort each hand by lexicographical order before sorting by class
    cards = ''.join(sorted(cards, key=order))
    
    if is_five_of_a_kind(cards):
        return 6
    if is_four_of_a_kind(cards):
        return 5
    if is_full_house(cards):
        return 4
    if is_three_of_a_kind(cards):
        return 3
    if is_two_pair(cards):
        return 2
    if is_pair(cards):
        return 1

    # High card
    return 0

def find_best_possible_hand(cards):
    # TODO: Find possible hand with N wildcards (N > 0)
    return cards

def joker_rank(hand):
    cards, bet = hand
    
    # Sort each hand by lexicographical order before sorting by class
    cards = ''.join(sorted(cards, key=order))
    cards = replace_jokers(cards)
    return rank((cards, bet))

def solve_part_one(filename):
    input = [line.strip("\r\n").split(" ") for line in open(filename, "r")]

    # Sort by the class of the hand. 
    # Five of a kind > Four of a kind > Full house > Three of a kind > Two pair > One Pair > High Card
    sorted_hands = sorted(input, key=lambda hand: (rank(hand), [card_ranking.index(card) for card in hand[0]]))

    # Sort by the rank of each card
    return sum([(int(sorted_hands.index(hand))+1)*int(hand[1]) for hand in sorted_hands])

def solve_part_two(filename):
    input = [line.strip("\r\n").split(" ") for line in open(filename, "r")]

    # Sort by the class of the hand. 
    # Five of a kind > Four of a kind > Full house > Three of a kind > Two pair > One Pair > High Card
    sorted_hands = sorted(input, key=lambda hand: (joker_rank(hand), [joker_card_ranking.index(card) for card in hand[0]]))

    # Sort by the rank of each card
    return sum([(int(sorted_hands.index(hand))+1)*int(hand[1]) for hand in sorted_hands])

print(solve_part_one("day7.txt"))
print(solve_part_two("day7.txt"))