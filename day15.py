with open("input_15.txt") as f:
    content = f.readlines()

starting_numbers = [int(x) for x in content[0].split(",")]


# part 1
def start_game(start_nums, rounds):
    spoken_nums = list(reversed(start_nums))
    print("Starting numbers: " + str(spoken_nums))
    while len(spoken_nums) < rounds:
        last_num = spoken_nums[0]
        print("Last number: " + str(last_num))
        last_spoken_nums = spoken_nums[1:]
        if last_num in last_spoken_nums:
            last_two = []
            for i, n in enumerate(spoken_nums):
                if n == last_num:
                    last_two.append(i)
                if len(last_two) == 2:
                    break
            curr_num = last_two[1] - last_two[0]
            spoken_nums = [curr_num] + spoken_nums
        else:
            curr_num = 0
            spoken_nums = [curr_num] + spoken_nums
    return spoken_nums[0]


# print(start_game(starting_numbers, 2020))


# part 2
def populate_start_nums_cache(start_nums):
    start_nums_cache = {}
    for idx, val in enumerate(start_nums):
        start_nums_cache[val] = [idx]
    return start_nums_cache


def start_game_v2(start_nums, rounds):
    curr_position = len(start_nums)
    spoken_nums = populate_start_nums_cache(start_nums)
    print("Starting numbers: " + str(spoken_nums))
    last_number = start_nums[-1]
    print("First last number: " + str(last_number))
    while curr_position < rounds:
        if curr_position % 10000 == 0:
            print("Current position: " + str(curr_position))
        if last_number in spoken_nums:
            if len(spoken_nums[last_number]) > 1:
                last = spoken_nums[last_number][-1]
                prev = spoken_nums[last_number][-2]
                next_number = last - prev
                if next_number in spoken_nums:
                    spoken_nums[next_number].append(curr_position)
                else:
                    spoken_nums[next_number] = [curr_position]
                last_number = next_number
            else:
                next_number = 0
                if next_number in spoken_nums:
                    spoken_nums[next_number].append(curr_position)
                else:
                    spoken_nums[next_number] = [curr_position]
                last_number = next_number
        else:
            spoken_nums[last_number] = [curr_position]
            next_number = 0
            if next_number in spoken_nums:
                spoken_nums[next_number].append(curr_position)
            else:
                spoken_nums[next_number] = [curr_position]
            last_number = next_number
        curr_position += 1
    return last_number


print(start_game_v2(starting_numbers, 30000000))

