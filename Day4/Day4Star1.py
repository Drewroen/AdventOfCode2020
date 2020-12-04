f = open("Day4.txt", "r")

passports = list(f.read().split('\n\n'))

valid_passports = 0

expected_headers = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
expected_headers_with_cid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
expected_headers.sort()
expected_headers_with_cid.sort()

for passport in passports:
    passport_headers = passport.replace('\n', ' ').split(" ")
    headers = list(map(lambda val: val.split(":")[0], passport_headers))
    headers.sort()
    if headers == expected_headers or headers == expected_headers_with_cid:
        valid_passports = valid_passports + 1

print(str(valid_passports) + " valid passports")