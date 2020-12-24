crab_cups = "496138527"


# part 1
def play_crab_cups(cups, moves):
    move = 1
    min_cup = find_min_cup(cups)
    max_cup = find_max_cup(cups)
    while move < moves + 1:
        curr_cup_position = move - 1

        if curr_cup_position >= len(cups):
            curr_cup_position = curr_cup_position % len(cups)

        current_cup = cups[curr_cup_position]

        positions_picked_up = set()
        if curr_cup_position + 4 < len(cups):
            pick_up = cups[curr_cup_position + 1:curr_cup_position + 4]
            positions_picked_up = set(range(curr_cup_position + 1, curr_cup_position + 4))
        else:
            pick_up = ""
            i = curr_cup_position + 1
            while len(pick_up) < 3:
                if i < len(cups):
                    pick_up = pick_up + cups[i]
                    positions_picked_up.add(i)
                else:
                    i = i % len(cups)
                    pick_up = pick_up + cups[i]
                    positions_picked_up.add(i)
                i += 1

        # remove picked up cups from cups
        reposition_cups = ""
        for idx, cup in enumerate(cups):
            if idx not in positions_picked_up:
                reposition_cups = reposition_cups + cup

        dest_cup_label = int(current_cup) - 1

        if str(dest_cup_label) in pick_up or dest_cup_label < min_cup:
            dest_cup_label = dest_cup_label - 1
            if str(dest_cup_label) in pick_up or dest_cup_label < min_cup:
                if dest_cup_label < min_cup:
                    dest_cup_label = max_cup
                while str(dest_cup_label) in pick_up:
                    dest_cup_label = dest_cup_label - 1
                    if dest_cup_label < min_cup:
                        dest_cup_label = max_cup

        dest_cup = str(dest_cup_label)

        # find dest_cup
        dest_position = find_cup(dest_cup, reposition_cups)

        # add picked up cups to repositioned cups
        add_back_pick_up = reposition_cups[:dest_position + 1] + pick_up + reposition_cups[dest_position + 1:]

        # is current cup where it's supposed to be? use current cup as pivot for positioning cups
        new_current_cup_pos = find_cup(current_cup, add_back_pick_up)

        if new_current_cup_pos == curr_cup_position:
            cups = add_back_pick_up
        else:
            pivoted_cups = add_back_pick_up
            while new_current_cup_pos != curr_cup_position:
                pivoted_cups = pivoted_cups[1:len(pivoted_cups)] + pivoted_cups[0]
                new_current_cup_pos = find_cup(current_cup, pivoted_cups)
            cups = pivoted_cups

        move += 1

    return cups


def find_min_cup(cups):
    min_cup = 100
    for c in cups:
        if int(c) < min_cup:
            min_cup = int(c)
    return min_cup


def find_max_cup(cups):
    max_cup = -1
    for c in cups:
        if int(c) > max_cup:
            max_cup = int(c)
    return max_cup


def find_cup(cup_to_find, cups):
    for i, cup in enumerate(cups):
        if cup == cup_to_find:
            return i
    return "Failed to find cup"


def get_cup_labels(cups):
    one_pos = find_cup('1', cups)
    cup_labels = cups[one_pos + 1:] + cups[:one_pos]
    return cup_labels


current_cups = play_crab_cups(crab_cups, 100)
print(get_cup_labels(current_cups))

