# aoc_day2.py

f = open("aoc_day2_input.txt", "r")

rules = []
passwords = []
for line in f:
	colon_index = line.find(":")
	rules.append(line[0:colon_index])
	passwords.append(line[colon_index + 1:len(line)])

num_valid = 0
print("Test: ", rules[0], " ", passwords[0])


# Part 1
for i in range(0, len(rules)):
	min_value = int(rules[i][0:rules[i].find("-")])
	max_value = int(rules[i][rules[i].find("-")+1:len(rules[i])-1])
	letter = rules[i][len(rules[i])-1]

	if min_value <= passwords[i].count(letter) <= max_value:
		num_valid += 1

print("Part 1: ", num_valid)

# Part 2

# password rules

    # 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    # 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    # 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

num_valid = 0
for i in range(0, len(rules)):
	pos1 = int(rules[i][0:rules[i].find("-")])
	pos2 = int(rules[i][rules[i].find("-")+1:len(rules[i])-1])
	letter = rules[i][len(rules[i])-1]

	print(pos1)
	print(pos2)
	print(passwords[i][pos1])
	print(passwords[i][pos2])
	print(letter)
	print(rules[i])
	print(passwords[i])

	if passwords[i][pos1] == letter and passwords[i][pos2] != letter:
		num_valid += 1
	elif passwords[i][pos2] == letter and passwords[i][pos1] != letter:
		num_valid += 1
	else:
		pass

print("Part 2: ", num_valid)


