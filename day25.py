with open("input_25.txt") as f:
    content = f.readlines()

public_keys_values = [int(x.strip()) for x in content]


# part 1
def calculate_loop_size(subject_number, modulus_m, public_key):
    curr_loop = 0
    v = 1
    while v != public_key:
        v = (v * subject_number) % modulus_m
        curr_loop += 1
    return curr_loop


def calculate_encryption_key(public_key, modulus_m, loop_size):
    curr_loop = 0
    v = 1
    while curr_loop < loop_size:
        v = (v * public_key) % modulus_m
        curr_loop += 1
    return v


card_public_key = public_keys_values[0]
door_public_key = public_keys_values[1]
card_loop_size = calculate_loop_size(7, 20201227, card_public_key)
door_loop_size = calculate_loop_size(7, 20201227, door_public_key)

print(card_loop_size, door_loop_size)

door_encryption_key = calculate_encryption_key(door_public_key, 20201227, card_loop_size)
card_encryption_key = calculate_encryption_key(card_public_key, 20201227, door_loop_size)

print(door_encryption_key, card_encryption_key)