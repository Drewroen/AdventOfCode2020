f = open("Day7.txt", "r")

rules = f.read().split('\n')

rules_split = list(map(lambda rule: rule.split(' contain '), rules))

def get_total_bags(color):
    total_bags = 0
    for rule in rules_split:
        if color in rule[0] and 'no other bags' in rule[1]:
            return 1
        elif color in rule[0]:
            bag_types = rule[1].split(', ')
            bag_info = list(map(lambda bag: [int(bag[0]), bag[1] + ' ' + bag[2]], map(lambda bag: bag.split(' '), bag_types)))
            for bag in bag_info:
                total_bags = total_bags + (bag[0] * (get_total_bags(bag[1])))
            return total_bags + 1


val = get_total_bags('shiny gold')
print(val - 1)