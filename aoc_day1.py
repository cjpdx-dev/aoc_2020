# advent of code day 1
# chris jacobs
# 12/13//2020

f = open("aoc_day1_input.txt", "r")

expense_list = []
for line in f:
	expense_list.append(int(line))

	
# solution has to be the sum of two even values or sum of two evens
# O(n) time for each list, so is this O(2n)?
evens = [value for value in expense_list if value % 2 == 0]
odds = [value for value in expense_list if value % 2 != 0]

# and now for 2 triple nested loops, making this... O(n^3) time? i'm sure there's a faster way

# Part 1
found = False
for even1 in evens:
	if found:
		break
	for even2 in evens:
		if found:
			break
		for even3 in evens:
			if even1 + even2 + even3 == 2020:
				print("found ", even1, " ", even2, " ", even3)
				print("answer", even1 * even2 * even3)
				found = True
				break


# Part 2
found = False
for odd1 in odds:
	if found:
		break
	for odd2 in odds:
		if found:
			break
		for odd3 in odds:
			if odd1 + odd2 == 2020:
				print("found ", odd1, " ", odd2, " ", odd3)
				print("answer: ", odd1 * odd2 * odd3)
				found = True
				break

# this implementation might not work for part 2? since the answer could be an odd plus an even, and then plus an odd


