f = open("Day1.txt", "r")

def is_not_empty(value):
    return value != ''

text = filter(is_not_empty, f.read().split('\n'))

numbers = list(map(lambda val: int(val), text))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print("The sum of the three numbers that equals 2020 is: " + str(numbers[i] * numbers[j] * numbers[k]))