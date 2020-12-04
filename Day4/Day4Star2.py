import re

f = open("Day4.txt", "r")

def valid_values(byr, ecl, eyr, hcl, hgt, iyr, pid):
    try:
        if (int(byr) >= 1920 and int(byr) <= 2002) is False:
            return False

        if ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
            return False

        if (int(eyr) >= 2020 and int(eyr) <= 2030) is False:
            return False

        if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl):
            return False

        if hgt[-2:] == 'in':
            if (int(hgt[:-2]) <= 76 and int(hgt[:-2]) >= 59) is False:
                return False
        elif hgt[-2:] == 'cm':
            if (int(hgt[:-2]) <= 193 and int(hgt[:-2]) >= 150) is False:
                return False
        else:
            return False

        if (int(iyr) >= 2010 and int(iyr) <= 2020) is False:
            return False

        if (len(pid) == 9 and int(pid)) is False:
            return False
    except:
        return False

    return True

passports = list(f.read().split('\n\n'))

valid_passports = 0

expected_headers = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
expected_headers_with_cid = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

for passport in passports:
    passport_info = passport.replace('\n', ' ').split(" ")
    passport_info.sort()
    passport_headers = list(map(lambda value: value[0:3], passport_info))
    info_without_cid = list(filter(lambda value: value[0:3] != 'cid', passport_info))
    if passport_headers == expected_headers or passport_headers == expected_headers_with_cid:
        passport_values = list(map(lambda value: value[4:], info_without_cid))
        if (valid_values(passport_values[0], passport_values[1], passport_values[2], passport_values[3], passport_values[4], passport_values[5], passport_values[6])):
            valid_passports = valid_passports + 1

print(str(valid_passports) + " valid passports")