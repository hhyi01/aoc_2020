from itertools import combinations

with open("input_10.txt") as f:
    content = f.readlines()

# adapters = sorted([int(x.strip()) for x in content])
adapters = [int(x.strip()) for x in content]

jolt_distribution = {
    "1": 0,
    "2": 0,
    "3": 0
}


# part 1
def populate_jolt_distribution(adapter_list, jolt_dict):
    start_jolt = 0
    for i, adapter in enumerate(adapter_list):
        if i == 0:
            net_jolt = str(adapter - start_jolt)
            jolt_dict[net_jolt] += 1
        else:
            net_jolt = str(adapter - adapter_list[i-1])
            jolt_dict[net_jolt] += 1
    # device adapter
    jolt_dict["3"] += 1
    return jolt_dict


# print(populate_jolt_distribution(adapters, jolt_distribution))
# print("1-jolt x 3-jolt: " + str(jolt_distribution["1"]*jolt_distribution["3"]))


# part 2
def verify_arrangement(adapters_list, last_adapter):
    adapters_sorted = sorted(adapters_list)
    start_jolt = 0
    valid_arrangement = True
    for i, adapter in enumerate(adapters_sorted):
        if i == 0:
            net_jolt = adapter - start_jolt
            if net_jolt > 3:
                valid_arrangement = False
                return valid_arrangement
        else:
            net_jolt = adapter - adapters_sorted[i-1]
            if net_jolt > 3:
                valid_arrangement = False
                return  valid_arrangement
    # device adapter
    if last_adapter - adapters_sorted[len(adapters_sorted)-1] != 3:
        valid_arrangement = False
        return valid_arrangement
    return valid_arrangement


def find_adapter_combinations(adapters_list):
    final_adapter = sorted(adapters_list)[len(adapters_list)-1] + 3
    combos = set()
    current_set_verified = verify_arrangement(adapters_list, final_adapter)
    test_list = sorted(adapters_list)
    if current_set_verified:
        combos.add(str(test_list))
    else:
        return "Unable to use all adapters."
    curr_len = len(test_list) - 1
    while curr_len > 0:
        com = combinations(test_list, curr_len)
        for i in list(com):
            # print("This combo: " + str(sorted(i)))
            is_valid = verify_arrangement(i, final_adapter)
            if is_valid:
                combos.add(str(sorted(i)))
        curr_len -= 1
        print("Current length: " + str(curr_len))
        print("Combo count: " + str(len(combos)))
    return len(combos)


print(find_adapter_combinations(adapters))