# chris jacobs
# advent of code - day 4
# dec 21st 2020

import re

def check_valid_data(passport):
    re_byr = "(byr:19[2-9][0-9])|(byr:200[0-2])"
    re_iyr = "(iyr:201[0-9])|(iyr:2020)"
    re_eyr = "(eyr:202[0-9])|(eyr:2030)"
    re_hgt = "(hgt:1[5-8][0-9]cm)|(hgt:19[0-3]cm)|(hgt:[5][9]in)|(hgt:[6][0-9]in)|(hgt:7[0-6]in)"
    re_hcl = "(hcl:#[a-f0-9]{6}[^\w])|(hcl:#[a-f0-9]{6}$)"
    re_ecl = "ecl:(amb|blu|brn|gry|grn|hzl|oth)"
    re_pid = "(pid:[0-9]{9}[^\d])|(pid:[0-9]{9}$)"

    regexs = (re_byr, re_iyr, re_eyr, re_hgt, re_ecl, re_pid, re_hcl)
    data_is_valid = True
    for regex in regexs:
        if re.search(regex, passport) is None:
            data_is_valid = False
            break
    return data_is_valid


def check_valid_passport(passport, valid_passports):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    all_req_fields_found = True
    for field in required_fields:
        if field not in passport:
            all_req_fields_found = False

    if all_req_fields_found:
        if check_valid_data(passport):
            valid_passports.append(passport)

    return all_req_fields_found


# Input Setup
# BUG: skips the last passport if there aren't two new lines at the end of the input file
f = open("aoc_day4_input.txt", "r")

valid_passports = []
list_of_passports = []
passport = ""
for line in f:
    if line == '\n' or line is None:
        list_of_passports.append(passport)
        passport = ""
    else:
        passport = passport + line.strip() + " "

num_valid = 0
for passport in list_of_passports:
    if check_valid_passport(passport, valid_passports):
        num_valid += 1

print("Part 1 Answer: " + str(num_valid))  # 219

# part 2
print("Part 2 Answer (num valid passports): " + str(len(valid_passports)))  # 127




