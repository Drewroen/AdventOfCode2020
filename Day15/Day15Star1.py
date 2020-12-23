f = open("Day15.txt", "r")

rules = f.read().split('\n')

numbers = list(map(lambda rule: int(rule), rules[0].split(',')))

def get_from_list(i, list):
    try:
        return list[i]
    except:
        return None

results = []

for i in range(2020):
    added_number = get_from_list(i, numbers)
    if added_number is None:
        if results[-1] not in results[:-1]:
            added_number = 0
        else:
            added_number = i - (len(results) - 1 - results[:-1][::-1].index(results[-1]))
    results.append(added_number)

print(results[-1])