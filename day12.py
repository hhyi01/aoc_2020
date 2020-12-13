with open("input_12.txt") as f:
    content = f.readlines()

nav_instructions = [x.strip() for x in content]

print(nav_instructions)

left_directions = {
    "N": ["W", "S", "E"],
    "W": ["S", "E", "N"],
    "S": ["E", "N", "W"],
    "E": ["N", "W", "S"]
}

right_directions = {
    "N": ["E", "S", "W"],
    "E": ["S", "W", "N"],
    "S": ["W", "N", "E"],
    "W": ["N", "E", "S"]
}


# part 1
def get_units(navigation_inst):
    d_units = 0
    if "N" in navigation_inst:
        d_units = int(navigation_inst.replace("N", ""))
    if "E" in navigation_inst:
        d_units = int(navigation_inst.replace("E", ""))
    if "S" in navigation_inst:
        d_units = int(navigation_inst.replace("S", ""))
    if "W" in navigation_inst:
        d_units = int(navigation_inst.replace("W", ""))
    if "F" in navigation_inst:
        d_units = int(navigation_inst.replace("F", ""))
    return d_units


def set_facing(nav_inst, current_facing, facing_directions):
    if "L" in nav_inst:
        degrees = int(nav_inst.replace("L", ""))
        facing_pos = int(degrees / 90)
        new_facing = facing_directions[current_facing][facing_pos - 1]
    else:
        degrees = int(nav_inst.replace("R", ""))
        facing_pos = int(degrees / 90)
        new_facing = facing_directions[current_facing][facing_pos - 1]
    return new_facing


def apply_nav_instructions(instructions, facing, left_dict, right_dict):
    # index 0 East/West, index 1 North/South
    curr_coord = [0, 0]
    curr_facing = facing
    for nav in instructions:
        print("Nav: " + nav)
        if "F" in nav:
            units = get_units(nav)
            print("Units: " + str(units))
            if curr_facing == "E" or curr_facing == "W":
                if curr_facing == "E":
                    curr_coord[0] += units
                else:
                    curr_coord[0] -= units
            if curr_facing == "N" or curr_facing == "S":
                if curr_facing == "N":
                    curr_coord[1] += units
                else:
                    curr_coord[1] -= units
        if "N" in nav or "S" in nav or "E" in nav or "W" in nav:
            units = get_units(nav)
            if "N" in nav:
                curr_coord[1] += units
            if "E" in nav:
                curr_coord[0] += units
            if "S" in nav:
                curr_coord[1] -= units
            if "W" in nav:
                curr_coord[0] -= units
        if "L" in nav or "R" in nav:
            if "L" in nav:
                curr_facing = set_facing(nav, curr_facing, left_dict)
            else:
                curr_facing = set_facing(nav, curr_facing, right_dict)
        print("Current coordinates: " + str(curr_coord))
    return abs(curr_coord[0]) + abs(curr_coord[1])


print(apply_nav_instructions(nav_instructions, "E", left_directions, right_directions))
