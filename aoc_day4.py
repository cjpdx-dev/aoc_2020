# chris jacobs
# advent of code - day 4
# dec 21st 2020

import re

def check_valid_data(passport):

    # conditions:
    #
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    # regex conditions
    
    re_byr = "byr:{1920, 2002}"
    test_string = "ecl:utc byr:2029 hcl:#efcc98 iyr:2023"


def check_valid_passport(passport, valid_passports):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    optional_cid = "cid"

    all_req_fields_found = True
    for field in required_fields:
        if field not in passport:
            all_req_fields_found = False

    # if all_req_fields_found:
        # if check_valid_data(passport):
            # valid_passports.append(passport)

    return all_req_fields_found


# Input Setup
# BUG: skips the last passport if there aren't two new lines at the end of the input file
# FIXED: added conditional if line is None
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

print(num_valid)
print(len(valid_passports))


# part 2
re_byr = "byr:([1][9][2-9][0-9]|2000|2001|2002)"
test_string = "ecl:utc byr:2000 hcl:#efcc98 iyr:2023"
x = re.search(re_byr, test_string)
print(x)