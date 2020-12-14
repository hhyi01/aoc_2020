with open("input_14.txt") as f:
    content = f.readlines()

bit_mask_instructions = [x.strip() for x in content]

print(bit_mask_instructions)


# part 1
def convert_to_binary(val):
    binary_rep = ""
    quotient = int(val / 2)
    diff = val - (quotient * 2)
    binary_rep = str(diff) + binary_rep
    while quotient != 0:
        val = quotient
        quotient = int(quotient / 2)
        diff = val - (quotient * 2)
        binary_rep = str(diff) + binary_rep
    if len(binary_rep) < 36:
        len_zeroes = 36 - len(binary_rep)
        add_zeroes = "0" * len_zeroes
        binary_rep = add_zeroes + binary_rep
    return binary_rep


def convert_to_decimal(binary_val):
    deci_val = 0
    binary_reversed = binary_val[::-1]
    for i in range(len(binary_val)):
        curr_val = int(binary_reversed[i])
        add_to_decimal = curr_val * (2**i)
        deci_val += add_to_decimal
    return deci_val


def apply_mask(curr_mask, binary_value):
    new_binary_value = ""
    for j in range(len(curr_mask)):
        if curr_mask[j] != "X":
            if curr_mask[j] != binary_value[j]:
                new_binary_value = new_binary_value + curr_mask[j]
            else:
                new_binary_value = new_binary_value + binary_value[j]
        else:
            new_binary_value = new_binary_value + binary_value[j]
    return new_binary_value


def run_bitmask_instructions(bitmask_instructions):
    mask = ""
    memory = {}
    for inst in bitmask_instructions:
        if "mask" in inst:
            mask = inst.split(" = ")[1]
        if "mem" in inst:
            curr_inst = inst.split(" = ")
            address, val_to_write = curr_inst[0].replace("mem[", "").replace("]", ""), int(curr_inst[1])
            val_in_binary = convert_to_binary(val_to_write)
            val_with_mask = apply_mask(mask, val_in_binary)
            binary_in_dec = convert_to_decimal(val_with_mask)
            memory[address] = binary_in_dec
    return memory


def sum_values_in_memory(memory_values):
    return sum(memory_values.values())


results = run_bitmask_instructions(bit_mask_instructions)
print(sum_values_in_memory(results))
