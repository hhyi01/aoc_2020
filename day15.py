with open("input_15.txt") as f:
    content = f.readlines()

starting_numbers = [int(x) for x in content[0].split(",")]


# part 1
def start_game(start_nums, rounds):
    spoken_nums = list(reversed(start_nums))
    print("Starting numbers: " + str(spoken_nums))
    while len(spoken_nums) < rounds:
        last_num = spoken_nums[0]
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


print(start_game(starting_numbers, 2020))

