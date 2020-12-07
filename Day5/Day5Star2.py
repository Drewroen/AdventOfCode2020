f = open("Day5.txt", "r")

passes = list(f.read().split('\n'))

seat_list = []

for boarding_pass in passes:
    bf = boarding_pass[0:7].replace('B', '1').replace('F', '0')
    lr = boarding_pass[7:].replace('R', '1').replace('L', '0')
    seat_list.append(int(bf, 2) * 8 + int(lr, 2))

seat_list.sort()
print(seat_list)
for i in range(1, len(seat_list)):
    if seat_list[i-1] + 2 == seat_list[i]:
        print(seat_list[i-1] + 1)