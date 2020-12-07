f = open("Day6.txt", "r")

answers = list(f.read().split('\n\n'))

answer_sum = 0

for answer in answers:
    answer_grouped = answer.split('\n')
    expected_answer_count = len(answer_grouped)
    answers_organized = ''.join(sorted(''.join(answer_grouped)))
    count = 0
    last_char = ''
    for a in answers_organized:
        if a != last_char:
            count = 1
            last_char = a
        elif a == last_char:
            count = count + 1

        if count == expected_answer_count:
            answer_sum = answer_sum + 1
O
print(answer_sum)