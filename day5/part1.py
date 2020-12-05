

def process_this(start, end, min_column, max_column, line, upper_half, lower_half):
    for i in range(start, end):
        char = line[i]
        if char == upper_half:
            min_column = ((max_column - min_column + 1)/ 2)  + min_column
        else:
            max_column = ((max_column - min_column) / 2) + min_column
    return min_column


def get_seat_id(line):
    row = process_this(0, 7, 0, 127, line, 'B', 'F')
    column = process_this(7, 10, 0, 7, line, 'R', 'L')
    seat_id = (row * 8) + column
    return seat_id


def process_seat_number_file():
    seats = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            seats.append(get_seat_id(line))
    return sorted(seats)


sorted_seats = process_seat_number_file()
for i in range(1, len(sorted_seats)-1):
    if sorted_seats[i-1] + 1 != sorted_seats[i]:
        print('My Seat Number: {}'.format(sorted_seats[i-1] + 1))
print('Max Seat ID: {}'.format(sorted_seats[-1]))
