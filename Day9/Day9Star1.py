f = open("Day9.txt", "r")

vals = list(map(lambda num: int(num), f.read().split('\n')))

def sum_combo_exists(sum, num_list):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == sum:
                return True
    return False

for position in range(25, len(vals)):
    if sum_combo_exists(vals[position], vals[position-25:position]) is False:
        print(vals[position])
        break