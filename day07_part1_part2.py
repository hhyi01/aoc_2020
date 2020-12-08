with open("input_07.txt") as f:
    content = f.readlines()

bags_data = [x.strip() for x in content]

count_bags = 0


# part 1
def parse_bag_data1(data):
    bags_rules = {}
    for bag in data:
        outer_bag_color, inner_bags = bag.split(" contain ")[0], bag.split(" contain ")[1]
        outer_bag_color = outer_bag_color.split(" ")[0] + " " + outer_bag_color.split(" ")[1]
        inner_bags_colors = [x.split(" ")[1] + " " + x.split(" ")[2]
                             for x in inner_bags.split(", ") if x != "no other bags."]
        bags_rules[outer_bag_color] = inner_bags_colors
    return bags_rules


def search_bag_rules(rules_data, curr_bag, target_bag, visited, path, bag_count):
    visited[curr_bag] = True
    path.append(curr_bag)
    if curr_bag == target_bag:
        if path[0] != target_bag:
            outer_colors.add(path[0])
    else:
        if rules_data[curr_bag] is not 0:
            for bag in rules_data[curr_bag]:
                if not visited[bag]:
                    bag_count += int(rules_data[curr_bag][bag])
                    search_bag_rules(rules_data, bag, target_bag, visited, path, bag_count)
    path.pop()
    visited[curr_bag] = False


def view_paths(start_bag, target_bag, data):
    visited = dict((key, False) for key in data)
    path = []
    search_bag_rules(data, start_bag, target_bag, visited, path, 0)


# bag_rules = parse_bag_data1(bags_data)

target = "shiny gold"
outer_colors = set()

# for this_bag in bag_rules:
#     view_paths(this_bag, target, bag_rules)

# print("Shiny bag count: " + str(len(outer_colors)))


# part 2
def parse_bag_data2(data):
    bags_rules = {}
    for bag in data:
        outer_bag_color, inner_bags = bag.split(" contain ")[0], bag.split(" contain ")[1]
        outer_bag_color = outer_bag_color.split(" ")[0] + " " + outer_bag_color.split(" ")[1]
        inner_bags_colors = dict((x.split(" ")[1] + " " + x.split(" ")[2], x.split(" ")[0])
                                 for x in inner_bags.split(", ") if x != "no other bags.")
        if len(inner_bags_colors) > 0:
            bags_rules[outer_bag_color] = inner_bags_colors
        else:
            bags_rules[outer_bag_color] = 0
    return bags_rules


bag_rules = parse_bag_data2(bags_data)
print(bag_rules)

for this_bag in bag_rules:
    view_paths(target, this_bag, bag_rules)
