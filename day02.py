
with open("input_02.txt") as f:
    content = f.readlines()

passwords_policies = [x.strip() for x in content]

valid_count = 0

# part 1
for policy_pw in passwords_policies:
    parse_policy = policy_pw.split(" ")
    char_count_low = int(parse_policy[0].split("-")[0])
    char_count_high = int(parse_policy[0].split("-")[1])
    char = parse_policy[1].replace(":", "")
    password = parse_policy[2]
    print("Char count low: " + str(char_count_low))
    print("Char count high: " + str(char_count_high))
    print("Password: " + password)
    char_count = password.count(char)
    if char_count_low <= char_count <= char_count_high:
        valid_count += 1

print("Valid count first policy: " + str(valid_count))

valid_count2 = 0

# part 2
for policy_pw in passwords_policies:
    parse_policy = policy_pw.split(" ")
    char_pos1 = int(parse_policy[0].split("-")[0])
    char_pos2 = int(parse_policy[0].split("-")[1])
    char = parse_policy[1].replace(":", "")
    password = parse_policy[2]
    print("Char count low: " + str(char_pos1))
    print("Char count high: " + str(char_pos2))
    print("Password: " + password)
    char_at_pos1 = password[char_pos1 - 1]
    char_at_pos2 = password[char_pos2 - 1]
    if char_at_pos1 != char_at_pos2:
        if char_at_pos1 == char or char_at_pos2 == char:
            valid_count2 += 1

print("Valid count second policy: " + str(valid_count2))
