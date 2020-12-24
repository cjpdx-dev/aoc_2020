# chris jacobs
# dec 24th 2020
# aoc day 5

# recursive method
def get_row_col_id(letters, max=127, min=0, n=0):

    # base cases
    if max - min == 1:
        if letters[n] == "F" or letters[n] == "L":
            return min
        else:
            return max

    # recursive case
    else:
        if letters[n] == "F" or letters[n] == "L":
            # row_max = row_max - ((row_max // 2) + 1)
            max = (max - ((max - min) // 2)) - 1
            row_col_id = get_row_col_id(letters, max, min, n + 1)
        elif letters[n] == "B" or letters[n] == "R":
            # row_min = row_min + ((row_max // 2) + 1)
            min = (min + ((max - min) // 2)) + 1
            row_col_id = get_row_col_id(letters, max, min, n + 1)

    return row_col_id  # is there a way to do this that avoids the ref before assignment warning?


# input setup
f = open("aoc_day5_input.txt", "r")
seats = [line.strip() for line in f]

# Part 1
max_seat_id = 0
min_seat_id = 0
for index, seat in enumerate(seats):
    seat_id = (get_row_col_id(seat[0:7]) * 8) + get_row_col_id(seat[7:], max=7, min=0, n=0)
    if index == 0:
        max_seat_id = seat_id
        min_seat_id = seat_id
    elif seat_id > max_seat_id:
        max_seat_id = seat_id
    elif seat_id < min_seat_id:
        min_seat_id = seat_id

    seats[index] = seat_id

# Part 1
print("Part 1 Answer (max_seat_id) ", max_seat_id)  # part 1 ans: 874

# Part 2
total_range = set([i for i in range(48, 875)])
missing_seat = total_range.difference(set(seats))
print("Part 2 Answer (missing_seat): ", missing_seat)







