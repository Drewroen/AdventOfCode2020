f = open("Day9.txt", "r")

vals = list(map(lambda num: int(num), f.read().split('\n')))

expected_value = 22477624

def list_equals_value(num_list):
    return sum(num_list) == expected_value

found_value = False

for i in range(len(vals)):
    for j in range(i, len(vals)):
        if list_equals_value(vals[i:j]) is True and found_value is False:
            correct_list = vals[i:j]
            print(max(correct_list) + min(correct_list))
            found_value = True