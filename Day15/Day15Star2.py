f = open("Day15.txt", "r")

rules = f.read().split('\n')

numbers = list(map(lambda rule: int(rule), rules[0].split(',')))

def get_from_list(i, list):
    try:
        return list[i]
    except:
        return None

last_val = 0
recent_values = {}


for i in range(30000000):
    added_number = get_from_list(i, numbers)
    if added_number is None:
        if recent_values[last_val] is None or len(recent_values[last_val]) == 1:
            added_number = 0
        else:
            added_number = i - recent_values[last_val][1] - 1
    # results.append(added_number)
    if recent_values.get(added_number) is None:
        recent_values[added_number] = [i]
    else:
        recent_values[added_number].insert(0, i)
        recent_values[added_number] = recent_values[added_number][0:2]
    last_val = added_number
    if i == 30000000 - 1:
        print(added_number)