# aoc day 3
# chris jacobs
# dec 16th 2020

# Input Setup
f = open("aoc_day3_input.txt", "r")
to_list = lambda row: list(row)
rows = [to_list(line.strip('\n')) for line in f]
last_index = len(rows[0])-1
final_row = len(rows)-1

print(len(rows))

# Part 1
num_trees = 0
cur_index = 0
cur_row = 0

at_last_row = False
while not at_last_row:

	if cur_index <= last_index - 3:

		if cur_row == final_row:
			at_last_row = True

		else:
			cur_index += 3
			cur_row += 1

			if rows[cur_row][cur_index] == "#":
				num_trees += 1

			print("Row: ", cur_row)
			print("Index: ", cur_index)
			print("Tree?: ", rows[cur_row][cur_index])

	else:
		cur_index = 2 - (last_index - cur_index)
		cur_row += 1

		if rows[cur_row][cur_index] == "#":
			num_trees += 1

		print("Row: ", cur_row)
		print("Index: ", cur_index)
		print("Tree?: ", rows[cur_row][cur_index])

print(num_trees)

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_for_each_slope = []

for slope in slopes:
	cur_index = 0
	cur_row = 0
	num_trees = 0

	at_last_row = False
	while not at_last_row:

		if cur_index <= last_index - slope[0]:

			if cur_row == final_row:
				at_last_row = True
			
			else:
				cur_index += slope[0]
				cur_row += slope[1]

				if rows[cur_row][cur_index] == "#":
					num_trees += 1

		else:
			cur_index = (slope[0] - 1) - (last_index - cur_index)
			cur_row += slope[1]

			if cur_row > final_row:
				at_last_row = True

			elif rows[cur_row][cur_index] == "#":
				num_trees += 1

			else:
				pass

	print(num_trees)
	trees_for_each_slope.append(num_trees)

print(trees_for_each_slope)

x = 1
for num_trees in trees_for_each_slope:
	x = x * num_trees

print(x)






