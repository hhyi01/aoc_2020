import json

with open("input_17.txt") as f:
    content = f.readlines()

initial_state = [x.strip() for x in content]


# part 1
def find_neighbors(coordinates):
    neighbors = []
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]
    for x, y, z in [(x+i, y+j, z+n) for i in (-1, 0, 1) for j in (-1, 0, 1) for n in (-1, 0, 1)
                    if i != 0 or j != 0 or n != 0]:
        neighbors.append([x, y, z])
    return neighbors


def add_neighbors(neighbor_list, new_state):
    for n in neighbor_list:
        current_n = json.dumps(n)
        if current_n not in new_state:
            new_state[current_n] = "."
    return new_state


def count_active_neighbors(current_state, neighbors):
    active_neighbors = 0
    for neighbor in neighbors:
        current_neighbor = json.dumps(neighbor)
        if current_neighbor in current_state:
            neighbor_state = current_state[current_neighbor]
            if neighbor_state == "#":
                active_neighbors += 1
    return active_neighbors


def populate_initial_state(init_state):
    results = {}
    z = 0
    for idx1, x in enumerate(initial_state):
        for idx2, y in enumerate(initial_state[idx1]):
            coord = json.dumps([idx1, idx2, z])
            results[coord] = initial_state[idx1][idx2]
    return results


def execute_cycle(previous_state):
    next_grid_state = previous_state.copy()
    for c in previous_state:
        current_c = json.loads(c)
        adj_coord = find_neighbors(current_c)
        next_grid_state = add_neighbors(adj_coord, next_grid_state)

    for c2 in next_grid_state:
        c2_d = json.loads(c2)
        neighborhood = find_neighbors(c2_d)
        active_n = count_active_neighbors(previous_state, neighborhood)
        if next_grid_state[c2] == ".":
            if active_n == 3:
                next_grid_state[c2] = "#"
        elif next_grid_state[c2] == "#":
            if active_n < 2 or active_n > 3:
                next_grid_state[c2] = "."
    return next_grid_state


initial_state = populate_initial_state(initial_state)
print(initial_state)

cycles = {
    0: initial_state
}

for i in range(0, 6):
    print("Cycle number: " + str(i))
    curr_state = cycles[i]
    next_state = execute_cycle(curr_state)
    print("Next state: " + str(next_state))
    cycles[i+1] = next_state
    cnt = 0
    for coordinates in next_state:
        if next_state[coordinates] == "#":
            cnt += 1
    print("Active count after cycle: " + str(cnt))










