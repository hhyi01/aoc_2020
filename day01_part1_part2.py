
with open("input_01.txt") as f:
    content = f.readlines()

expense_entries = {int(x.strip()) for x in content}

target = 2020

# part 1
for entry in expense_entries:
    seeking = target - entry
    if seeking in expense_entries:
        print(entry * seeking)
        break


# part 2
for entry in expense_entries:
    target2 = target - entry
    for entry2 in expense_entries:
        seeking = target2 - entry2
        if seeking in expense_entries:
            print(entry * seeking * entry2)
            break
