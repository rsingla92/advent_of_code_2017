'''
Advent of Code 2017, day 1 part 1.

Compute a checksum for a spreadsheet.
For each row, find the largest and smallest values. Compute the difference.
Sum the differences for each row.

'''

SPREADSHEET_FILENAME = 'day_2_part_1_input.txt'
TEST_SPREADSHEET = 'test_input.txt'


def read_spreadsheet(filename):
    # Use list comprehension to split each line
    # in the file into its own list.
    with open(filename) as myFile:
        rows = [row.split() for row in myFile]
    return rows


def compute_checksum(rows):
    sum_of_diffs = 0
    for row in rows:
        # Treat each string as an int
        int_row = [int(i) for i in row]
        diff = max(int_row) - min(int_row)
        sum_of_diffs += int(diff)
    return sum_of_diffs


if __name__ == '__main__':
    spreadsheet = read_spreadsheet(TEST_SPREADSHEET)
    print "Checksum is " + str(compute_checksum(spreadsheet))

    spreadsheet = read_spreadsheet(SPREADSHEET_FILENAME)
    print "Checksum is " + str(compute_checksum(spreadsheet))

