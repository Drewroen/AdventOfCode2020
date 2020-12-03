f = open("Day1.txt", "r")

numbers = list(map(lambda val: int(val), f.read().split('\n')))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print("The sum of the three numbers that equals 2020 is: " + str(numbers[i] * numbers[j] * numbers[k]))