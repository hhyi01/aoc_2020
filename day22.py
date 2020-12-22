from collections import deque
import itertools

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


def calculate_score(cards_data, winner):
    if winner == "":
        for player in cards_data:
            if len(cards_data[player]) > 0:
                winner = player
    score = 0
    multiplier = len(cards_data[winner])
    for card in cards_data[winner]:
        score += int(card) * multiplier
        multiplier -= 1
    return score


# part 2
def play_combat_v2(cards_data, previous_rounds, first_game_decks):
    curr_round = 1

    while len(cards_data['Player 1']) > 0 and len(cards_data['Player 2']) > 0:

        player1_cards = str(cards_data['Player 1'])
        player2_cards = str(cards_data['Player 2'])

        if len(first_game_decks) > 0:
            for game in first_game_decks:
                if game['Player 1'] == player1_cards and game['Player 2'] == player2_cards:
                    return

        next_round = {
            'Player 1': player1_cards,
            'Player 2': player2_cards
        }
        previous_rounds.append(next_round)

        player1 = cards_data['Player 1'].popleft()
        player2 = cards_data['Player 2'].popleft()

        if len(cards_data['Player 1']) >= int(player1) and len(cards_data['Player 2']) >= int(player2):
            print("Playing a sub-game to determine the winner...")
            cards_data_copy = {
                'Player 1': deque(itertools.islice(cards_data['Player 1'], 0, int(player1))),
                'Player 2': deque(itertools.islice(cards_data['Player 2'], 0, int(player2)))
            }
            # print("In sub-game: Cards: " + str(cards_data_copy))
            play_combat_v2(cards_data_copy, previous_rounds, first_game_decks)

        if len(previous_rounds) > 0:
            last_round = previous_rounds[-1]

        if len(last_round) > 0 and (last_round['Player 1'] == 'deque([])' or last_round['Player 2'] == 'deque([])'):
            if last_round['Player 1'] == 'deque([])':
                winning_player = 'Player 2'
                cards_data[winning_player].append(player2)
                cards_data[winning_player].append(player1)

            elif last_round['Player 2'] == 'deque([])':
                winning_player = 'Player 1'
                cards_data[winning_player].append(player1)
                cards_data[winning_player].append(player2)

        else:
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

    # print("Current cards - Player 1: " + str(cards_data['Player 1']) + " Player 2: " + str(cards_data['Player 2']))
    player1_cards = str(cards_data['Player 1'])
    player2_cards = str(cards_data['Player 2'])

    final_round = {
        'Player 1': player1_cards,
        'Player 2': player2_cards
    }
    previous_rounds.append(final_round)

    print("Current result: " + str(previous_rounds[-1]))
    return cards_data


starting_decks = parse_cards(player_data)
# game_resuts = play_combat(starting_decks)
game_resuts_v2 = play_combat_v2(starting_decks, [], [])
print("Game Final Results: " + str(game_resuts_v2))
print(calculate_score(game_resuts_v2, ""))

