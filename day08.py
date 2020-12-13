
with open("input_08.txt") as f:
    content = f.readlines()

instruction_list = [x.strip() for x in content]


# part 1
def run_instructions(instructions, index):
    accumulator = 0
    executed_instructions = set()
    repeated_instruction = False

    while index < len(instructions):
        instruction = instructions[index].split(" ")
        operation = instruction[0]
        argument = int(instruction[1])
        # print("Operation: " + operation + ", Argument: " + str(argument))
        if operation == "nop":
            if index not in executed_instructions:
                executed_instructions.add(index)
            else:
                # print("Repeated instruction: " + str(index))
                repeated_instruction = True
                break
            index += 1
        if operation == "acc":
            if index not in executed_instructions:
                executed_instructions.add(index)
            else:
                # print("Repeated instruction: " + str(index))
                repeated_instruction = True
                break
            accumulator += argument
            index += 1
        if operation == "jmp":
            if index not in executed_instructions:
                executed_instructions.add(index)
            else:
                # print("Repeated instruction: " + str(index))
                repeated_instruction = True
                break
            index += argument
    return accumulator, repeated_instruction


# print("Value of accumulator - part 1: " + str(run_instructions(instruction_list, 0)))


# part 2
# find jmp operation that should be nop or vice versa

for idx, inst in enumerate(instruction_list):
    if "nop" in instruction_list[idx]:
        instruction_list_copy = instruction_list[:]
        instruction_list_copy[idx] = instruction_list_copy[idx].replace("nop", "jmp")
        results_nop = run_instructions(instruction_list_copy, 0)
        if not results_nop[1]:
            print("Result tuple: " + str(results_nop))
            break
    if "jmp" in instruction_list[idx]:
        instruction_list_copy = instruction_list[:]
        instruction_list_copy[idx] = instruction_list_copy[idx].replace("jmp", "nop")
        results_jmp = run_instructions(instruction_list_copy, 0)
        if not results_jmp[1]:
            print("Result tuple: " + str(results_jmp))
            break
