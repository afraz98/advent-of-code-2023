def tally_points(games):
    sum = 0
    for game in games:
        points = 0
        
        game = list(filter(lambda x: x != '', game))[2:]
        winning_numbers, actual_numbers = ":".join(game).split("|")

        winning_numbers = list(filter(lambda x: x != '', winning_numbers.split(":")))
        actual_numbers = list(filter(lambda x: x != '', actual_numbers.split(":")))

        for number in actual_numbers:
            if number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        sum += points
    return sum

def tally_cards(games):
    card_multipliers = [1 for i in range(0, len(games))]
    
    for game in games:
        game_index = games.index(game)
        print("Game %s is starting" % (game_index + 1))
        
        matches = 0

        multiplier = card_multipliers[game_index]
        winning_numbers, actual_numbers = ":".join(game[2:]).split("|")

        # Filter out spaces left over from double-spacing
        winning_numbers = list(filter(lambda x: x != '', winning_numbers.split(":")))
        actual_numbers = list(filter(lambda x: x != '', actual_numbers.split(":")))

        # Find matching numbers
        for number in actual_numbers:
            if number in winning_numbers:
                matches += 1

        print("Card %s had %s matches" % (game_index+1, matches))

        # Increment multipliers for each successive card
        for i in range((game_index + 1), (game_index + 1) + matches):
            print("Adding %s copies of card %s" % (multiplier, i+1))
            card_multipliers[i] += 1 * multiplier

    return sum(card_multipliers)

def solve_part_one(filename):
    return tally_points([line.strip("\r\n").replace(":", "").split(" ") for line in open(filename, 'r')])

def solve_part_two(filename):
    return tally_cards([line.strip("\r\n").replace(":", "").split(" ") for line in open(filename, 'r')])


# print(solve_part_one("day4.txt"))
print(solve_part_two("day4_test.txt"))
# print(solve_part_two("day4.txt"))