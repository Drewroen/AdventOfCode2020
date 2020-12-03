f = open("Day2.txt", "r")

def is_valid_password(min_char, max_char, char_value, password):
    total_chars = 0
    for char in password:
        if char == char_value:
            total_chars = total_chars + 1
    return total_chars >= min_char and total_chars <= max_char

text = list(f.read().split('\n'))

print(len(text))
valid_passwords = 0
for line in text:
    values = line.split(' ')
    min_max_values = values[0].split('-')
    min_value = int(min_max_values[0])
    max_value = int(min_max_values[1])
    char_value = values[1][0:1]
    password = values[2]
    if is_valid_password(min_value, max_value, char_value, password):
        valid_passwords = valid_passwords + 1

print (str(valid_passwords) + " valid passwords!")