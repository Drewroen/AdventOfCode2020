f = open("Day16.txt", "r")

rules = f.read().split('\n')

valid_ranges = []
for rule in rules:
    if ':' in rule:
        vala = rule.split(':')[1]
        valb = vala.split('or')
        for valc in valb:
            vald = valc.strip().split('-')
            if len(vald) == 2:
                valid_ranges.append([int(vald[0]), int(vald[1])])

total_sum = 0

for vals in rules[rules.index('nearby tickets:')+1:]:
    for vals2 in vals.split(','):
        valid = False
        for rule in valid_ranges:
            vals3 = int(vals2)
            if vals3 >= rule[0] and vals3 <= rule[1]:
                valid = True
                break
        if valid == False:
            total_sum += int(vals2)

print(total_sum)