f = open("Day5.txt", "r")

passes = list(f.read().split('\n'))

highest_seat = 0

for boarding_pass in passes:
    bf = boarding_pass[0:7].replace('B', '1').replace('F', '0')
    lr = boarding_pass[7:].replace('R', '1').replace('L', '0')
    highest_seat = max(highest_seat, int(bf, 2) * 8 + int(lr, 2))

print(highest_seat)