f = open("Day16.txt", "r")

rules = f.read().split('\n')

valid_ranges = {}
for rule in rules:
    if ':' in rule:
        valtype = rule.split(':')[0]
        vala = rule.split(':')[1]
        valb = vala.split('or')
        if 'your ticket' not in valtype and 'nearby tickets' not in valtype:
            valid_ranges[valtype] = []
            for valc in valb:
                vald = valc.strip().split('-')
                if len(vald) == 2:
                    valid_ranges[valtype].append([int(vald[0]), int(vald[1])])

# print(valid_ranges)

total_sum = 0

your_ticket = rules[rules.index('your ticket:')+1:rules.index('your ticket:')+2]

list_of_tickets = rules[rules.index('nearby tickets:')+1:]

organized_rules = {}


for i in range(len(list_of_tickets)):
    for j in list_of_tickets[i].split(','):
        valid = False
        for rule in valid_ranges.values():
            for r in rule:
                if int(j) >= r[0] and int(j) <= r[1]:
                    valid = True
        if valid == False:
            list_of_tickets[i] = None

list_of_tickets = list(filter(lambda ticket: ticket != None, list_of_tickets))

for i in range(len(list_of_tickets[0].split(','))):
    for j, k in valid_ranges.items():
        found_column = True
        for ticket in list_of_tickets:
            pos_val = ticket.split(',')[i]
            within_one_range = False
            for l in k:
                if int(pos_val) >= l[0] and int(pos_val) <= l[1]:
                    within_one_range = True
            if within_one_range == False:
                found_column = False
        if found_column is True:
            if organized_rules.get(j) is None:
                organized_rules[j] = [i]
            else:
                organized_rules[j].append(i)

filtered = False
vals_to_filter = []
while not filtered:
    filtered = True
    for i, j in organized_rules.items():
        if len(j) != 1:
            filtered = False
        if len(j) == 1:
            vals_to_filter.append(j[0])
        if len(j) != 1:
            organized_rules[i] = list(filter(lambda val: val not in vals_to_filter, j))

total = 1

your_ticket = your_ticket[0].split(',')

for i, j in organized_rules.items():
    if 'departure ' in i:
        total = total * int(your_ticket[j[0]])

print(total)