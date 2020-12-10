f = open("Day10.txt", "r")

vals = list(map(lambda num: int(num), f.read().split('\n')))

vals.sort()

info_list = {}

def get_total_options(values, number):
    if info_list.get(number, -1) != -1:
        return info_list.get(number)
    total = 0
    found_val = False
    for i in values:
        if i > number and i - number <= 3:
            found_val = True
            total = total + get_total_options(list(filter(lambda _val: _val > i, values)), i)
        else:
            break
    if found_val is False:
        return 1
    info_list[number] = total
    return total
            
print(get_total_options(vals, 0))