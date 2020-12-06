f = open("Day6.txt", "r")

answers = list(map(lambda group: ''.join(group.split('\n')), list(f.read().split('\n\n'))))

answer_sum = 0

for answer in answers:
    answer_dict = {}
    for c in answer:
        answer_dict[c] = True
    answer_sum = answer_sum + len(answer_dict.keys())

print(answer_sum)