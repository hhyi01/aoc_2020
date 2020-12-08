
with open("input_08.txt") as f:
    content = f.readlines()

instructions = [x.strip() for x in content]

accumulator = 0
executed_instructions = set()
index = 0

while index < len(instructions):
    instruction = instructions[index].split(" ")
    operation = instruction[0]
    argument = int(instruction[1])
    print("Operation: " + operation + ", Argument: " + str(argument))
    if operation == "nop":
        if index not in executed_instructions:
            executed_instructions.add(index)
        else:
            print("Repeated instruction: " + str(index))
            break
        index += 1
    if operation == "acc":
        if index not in executed_instructions:
            executed_instructions.add(index)
        else:
            print("Repeated instruction: " + str(index))
            break
        accumulator += argument
        index += 1
    if operation == "jmp":
        if index not in executed_instructions:
            executed_instructions.add(index)
        else:
            print("Repeated instruction: " + str(index))
            break
        index += argument


print("Value of accumulator: " + str(accumulator))




