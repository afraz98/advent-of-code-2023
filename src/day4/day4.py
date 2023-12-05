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

def solve_part_one(filename):
    return tally_points([line.strip("\t\r\n").replace(":", "").split(" ") for line in open(filename, 'r')])

print(solve_part_one("day4.txt"))