import math
import sys

with open("input_05.txt") as f:
    content = f.readlines()

seats = [x.strip() for x in content]


# part 1
def determine_seat(bsp_data):
    start_row = 0
    end_row = 127
    start_seat = 0
    end_seat = 7
    for c in bsp_data:
        if c == "F":
            keep_lower = math.floor((end_row + start_row)/2)
            end_row = keep_lower
        if c == "B":
            keep_upper = math.ceil((end_row + start_row)/2)
            start_row = keep_upper
        # start_row and end_row will be equal
        row = end_row
        if c == "R":
            seat_upper = math.ceil((end_seat + start_seat)/2)
            start_seat = seat_upper
        if c == "L":
            seat_lower = math.floor((end_seat + start_seat)/2)
            end_seat = seat_lower
        final_seat = end_seat
    return row * 8 + final_seat


highest_id = -sys.maxsize
lowest_id = sys.maxsize
seats_taken = set()

for ticket in seats:
    seat_id = determine_seat(ticket)
    seats_taken.add(seat_id)
    if seat_id > highest_id:
        highest_id = seat_id
    if seat_id < lowest_id:
        lowest_id = seat_id


# part 2
print(highest_id)
print(lowest_id)

my_seat = 0

for seat in range(lowest_id, highest_id):
    if seat not in seats_taken:
        my_seat = seat

print(my_seat)
