f = open("Day7.txt", "r")

rules = f.read().split('\n')

rules_split = list(map(lambda rule: rule.split(' contain '), rules))

new_bag_found = True

valid_colors = ['shiny gold']

while new_bag_found:
    new_bag_found = False
    current_colors = valid_colors.copy()
    for rule in rules_split:
        for color in valid_colors:
            if color in rule[1]:
                valid_colors.append(rule[0].split(' bags')[0])
                # new_bag_found = True
    valid_colors = list(set(valid_colors))
    valid_colors.sort()
    current_colors.sort()
    if valid_colors != current_colors:
        new_bag_found = True

print(len(valid_colors) - 1)