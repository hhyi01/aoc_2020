from copy import deepcopy
import json

with open("input_11.txt") as f:
    content = f.readlines()

seat_grid = [x.strip() for x in content]

# for row in seat_grid:
#     print(row)


# part 1
def check_seat_adjacency(seat_matrix, seat_position):
    len_row = len(seat_matrix[0]) - 1
    num_rows = len(seat_matrix) - 1
    seat_matrix_copy = seat_matrix[:]
    adj_seats = 0
    up_seat = seat_position[:]
    if up_seat[0] > 0:
        up_seat[0] -= 1
    if str(up_seat) != str(seat_position):
        if seat_matrix_copy[up_seat[0]][up_seat[1]] == "#":
            adj_seats += 1
    # print("Up: " + str(up_seat) + " Same? " + str(str(up_seat) == str(seat_position)) + " Cnt: " + str(adj_seats))
    down_seat = seat_position[:]
    if down_seat[0] < num_rows:
        down_seat[0] += 1
    if str(down_seat) != str(seat_position):
        if seat_matrix_copy[down_seat[0]][down_seat[1]] == "#":
            adj_seats += 1
    # print("Down: " + str(up_seat) + " Same? " + str(str(down_seat) == str(seat_position)) + " Cnt: " + str(adj_seats))
    left_seat = seat_position[:]
    if left_seat[1] > 0:
        left_seat[1] -= 1
    if str(left_seat) != str(seat_position):
        if seat_matrix_copy[left_seat[0]][left_seat[1]] == "#":
            adj_seats += 1
    # print("Left: " + str(left_seat) + " Same? " + str(str(left_seat) == str(seat_position)) + " Cnt: " + str(adj_seats))
    right_seat = seat_position[:]
    if right_seat[1] < len_row:
        right_seat[1] += 1
    if str(right_seat) != str(seat_position):
        if seat_matrix_copy[right_seat[0]][right_seat[1]] == "#":
            adj_seats += 1
    # print("Right: " + str(right_seat) + " Same? " + str(str(right_seat) == str(seat_position)) + " Cnt: " + str(adj_seats))
    up_right_diag = seat_position[:]
    # check if valid seat
    if up_right_diag[0] > 0 and up_right_diag[1] < len_row:
        up_right_diag[0] -= 1
        up_right_diag[1] += 1
    if str(up_right_diag) != str(seat_position):
        if seat_matrix_copy[up_right_diag[0]][up_right_diag[1]] == "#":
            adj_seats += 1
    # print("Up right diag: " + str(up_right_diag) + " Same? " + str(str(up_right_diag) == str(seat_position)) + " Cnt: " + str(adj_seats))
    up_left_diag = seat_position[:]
    if up_left_diag[0] > 0 and up_left_diag[1] > 0:
        up_left_diag[0] -= 1
        up_left_diag[1] -= 1
    if str(up_left_diag) != str(seat_position):
        if seat_matrix_copy[up_left_diag[0]][up_left_diag[1]] == "#":
            adj_seats += 1
    # print("Up Left diag: " + str(up_left_diag) + " Same? " + str(
    #     str(up_left_diag) == str(seat_position)) + " Cnt: " + str(adj_seats))
    down_right_diag = seat_position[:]
    if down_right_diag[0] < num_rows and down_right_diag[1] < len_row:
        down_right_diag[0] += 1
        down_right_diag[1] += 1
    if str(down_right_diag) != str(seat_position):
        if seat_matrix_copy[down_right_diag[0]][down_right_diag[1]] == "#":
            adj_seats += 1
    # print("Down right diag: " + str(down_right_diag) + " Same? " + str(
    #     str(down_right_diag) == str(seat_position)) + " Cnt: " + str(adj_seats))
    down_left_diag = seat_position[:]
    if down_left_diag[0] < num_rows and down_left_diag[1] > 0:
        down_left_diag[0] += 1
        down_left_diag[1] -= 1
    if str(down_left_diag) != str(seat_position):
        if seat_matrix_copy[down_left_diag[0]][down_left_diag[1]] == "#":
            adj_seats += 1
    # print("Down left diag: " + str(down_left_diag) + " Same? " + str(
    #     str(down_left_diag) == str(seat_position)) + " Cnt: " + str(adj_seats))
    return adj_seats


def count_occupied_seats(curr_seat_matrix):
    occupied_seats = 0
    for curr_row in curr_seat_matrix:
        for curr_seat in curr_row:
            if curr_seat == "#":
                occupied_seats += 1
    return occupied_seats


def run_simulation(curr_seats):
    next_iteration = []
    print("Layout used ")
    print_seat_orientation(curr_seats)
    print("\n\n")
    for idx1, current_row in enumerate(curr_seats):
        new_row = ""
        for idx2, current_seat in enumerate(current_row):
            adj_count = check_seat_adjacency(curr_seats, [idx1, idx2])
            # print("Seat position: " + str([idx1, idx2]))
            # print("Adj count: " + str(adj_count))
            if current_seat == "L":
                if adj_count == 0:
                    new_row = new_row + "#"
                else:
                    new_row = new_row + current_seat
            elif current_seat == "#":
                if adj_count >= 4:
                    new_row = new_row + "L"
                else:
                    new_row = new_row + current_seat
            else:
                new_row = new_row + current_seat
        next_iteration.append(new_row)
    return next_iteration


def print_seat_orientation(matrix):
    for r in matrix:
        print(r)


simulations = {
    "0": seat_grid[:]
}

curr_occupied_count = 0
# start with any value here
prev_occupied_count = -1
sim_num = 0

while curr_occupied_count != prev_occupied_count:
    print("Simulation number: " + str(sim_num) + "\n")
    current_layout = simulations[str(sim_num)]
    if sim_num > 0:
        prev_occupied_count = curr_occupied_count
    curr_occupied_count = count_occupied_seats(current_layout)
    next_iter = run_simulation(current_layout)
    sim_num += 1
    simulations[str(sim_num)] = next_iter
    print("Occupied now: " + str(curr_occupied_count))
    print("Last occupied: " + str(prev_occupied_count))


