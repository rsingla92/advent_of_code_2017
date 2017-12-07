'''
Advent of Code 2017, day 1 part 1.

Compute a checksum for a spreadsheet.
For each row, find the two numbers divisble by each other. Compute the difference.
Sum the differences for each row.

'''

SPREADSHEET_FILENAME = 'day_2_part_1_input.txt'
TEST_SPREADSHEET = 'test_input.txt'


def read_spreadsheet(filename):
    with open(filename) as myFile:
        rows = [row.split() for row in myFile]
    return rows


def compute_checksum(rows):
    sum_of_quotients = 0
    for row in rows:
        int_row = [int(i) for i in row]
        sum_of_quotients += find_divisible_nums(int_row)
    return sum_of_quotients


def find_divisible_nums(row):
    # Iterate over each pair of in the row, and check divisibility
    # using the modulo function
    quotient = 0
    for i,i_val in enumerate(row):
        for j,j_val in enumerate(row):
            if i == j:
                break
            elif i_val % j_val == 0:
                quotient = i_val / j_val
            elif j_val % i_val == 0:
                quotient = j_val / i_val
    return quotient


if __name__ == '__main__':
    spreadsheet = read_spreadsheet(TEST_SPREADSHEET)
    print "Checksum is " + str(compute_checksum(spreadsheet))

    spreadsheet = read_spreadsheet(SPREADSHEET_FILENAME)
    print "Checksum is " + str(compute_checksum(spreadsheet))

