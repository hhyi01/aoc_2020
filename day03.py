
with open("input_03.txt") as f:
    content = f.readlines()

map_rows = [x.strip() for x in content]

# part 1


def count_trees(slope):
    start_steps = 0
    tree_count = 0
    for i, row in enumerate(map_rows):
        if i % slope[1] == 0:
            if start_steps > len(row) - 1:
                idx = start_steps % len(row)
            else:
                idx = start_steps
            thing = row[idx]
            if thing == "#":
                tree_count += 1
            start_steps += slope[0]
    return tree_count


print(count_trees([3, 1]))

# part 2
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_counts_x = 1

for curr_slope in slopes:
    curr_tree_count = count_trees(curr_slope)
    tree_counts_x = tree_counts_x * curr_tree_count

print(tree_counts_x)
