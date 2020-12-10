with open("input_10.txt") as f:
    content = f.readlines()

adapters = sorted([int(x.strip()) for x in content])

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
def find_adapter_combinations(adapters_list):
    pass


