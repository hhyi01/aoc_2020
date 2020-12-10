with open("input_09.txt") as f:
    content = f.readlines()

xmas = [int(x.strip()) for x in content]

print(xmas)

preamble_length = 25


# part 1
def create_preamble_set(xmas_list, start_pos, preamble_len):
    preamble_set = set()
    for idx in range(start_pos, preamble_len):
        item = xmas_list[idx]
        preamble_set.add(item)
    return preamble_set


def verify_number(num, preamble_cache):
    valid_num = False
    for n in preamble_cache:
        diff = num - n
        if diff in preamble_cache and diff != num:
            valid_num = True
            return valid_num
    return valid_num


start_index = preamble_length
preamble_numbers = create_preamble_set(xmas, 0, preamble_length)

# find bad number
for index in range(start_index, len(xmas)):
    print("Preamble cache: " + str(preamble_numbers))
    curr_num = xmas[index]
    print("Current number: " + str(curr_num))
    is_valid_num = verify_number(curr_num, preamble_numbers)
    if not is_valid_num:
        print("Bad number: " + str(curr_num))
        break
    num_remove = xmas[index - preamble_length]
    print("Remove number: " + str(num_remove))
    preamble_numbers.remove(num_remove)
    num_add = xmas[index]
    print("Add number: " + str(num_add))
    preamble_numbers.add(num_add)


# part 2
example_bad_number = 127
bad_number = 14144619

start_index = 0
end_index = 0
curr_sum = xmas[start_index]

while end_index < len(xmas) and start_index < len(xmas):
    print("Current sum: " + str(curr_sum))
    if curr_sum == bad_number:
        cont_set = {xmas[x] for x in range(start_index, end_index + 1)}
        print("Contiguous set: " + str(cont_set))
        min_num = min(cont_set)
        max_num = max(cont_set)
        print("Min number: " + str(min_num))
        print("Max number: " + str(max_num))
        print("Sum min max: " + str(min_num + max_num))
        break
    elif curr_sum > bad_number:
        print("Current sum to large: " + str(curr_sum))
        curr_sum = curr_sum - xmas[start_index]
        start_index += 1
    else:
        print("Current sum too small: " + str(curr_sum))
        end_index += 1
        curr_sum += xmas[end_index]
