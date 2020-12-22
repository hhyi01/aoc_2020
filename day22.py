from collections import deque

with open("input_22.txt") as f:
    content = f.readlines()

player_data = [x.strip() for x in content]


# part 1
def parse_cards(data):
    cards = {}
    for dpt in data:
        if "Player" in dpt:
            curr_player = dpt.replace(":", "")
            cards[curr_player] = deque()
        elif dpt != "":
            cards[curr_player].append(dpt)
    return cards


def play_combat(cards_data):
    curr_round = 1
    while len(cards_data['Player 1']) > 0 and len(cards_data['Player 2']) > 0:
        # print("Cards: " + str(cards_data))
        player1 = cards_data['Player 1'].popleft()
        player2 = cards_data['Player 2'].popleft()
        if int(player1) > int(player2):
            winning_player = 'Player 1'
            cards_data[winning_player].append(player1)
        else:
            winning_player = 'Player 2'
            cards_data[winning_player].append(player2)
        if cards_data[winning_player][-1] == player1:
            cards_data[winning_player].append(player2)
        else:
            cards_data[winning_player].append(player1)
        print(winning_player + " wins the round! " + " Round: " + str(curr_round))
        curr_round += 1
    return cards_data


def calculate_score(cards_data):
    for player in cards_data:
        if len(cards_data[player]) > 0:
            winner = player
    score = 0
    multiplier = len(cards_data[winner])
    for card in cards_data[winner]:
        score += int(card) * multiplier
        multiplier -= 1
    return score


starting_decks = parse_cards(player_data)
game_resuts = play_combat(starting_decks)
print(calculate_score(game_resuts))

