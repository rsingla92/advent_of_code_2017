'''

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

'''
from math import sqrt, floor, fabs


def calculate_spiral_coords(n):
    # Determine the radius of the spiral 'n' is in.
    # If the spiral length is u, then the last element is at u^2.
    # The next spiral is u^2 + 1 right, continuing u up, then u+1
    # leftwards, u+1 downwards, and u+2 right.

    # Calculate u
    u = floor(sqrt(n))
    if u % 2 == 0:
        u -= 1

    radius = (u - 1) // 2
    n -= u ** 2

    if n == 0:
        return radius, radius

    n -= 1

    if n < u:
        return radius+1, radius-n

    n -= u

    if n < u + 1:
        return radius +  1 - n, radius - u

    n -= u+1

    if n < u + 1:
        return radius - u, radius - u + n

    n -= u + 1

    if n < u + 2:
        return radius - u + n, radius + 1


def calculate_steps(n):
    x, y = calculate_spiral_coords(n)
    print 'x: ' + str(x) + ' y: ' + str(y)
    return fabs(x)+fabs(y)


if __name__ == '__main__':
    test_1 = 1
    print 'Test 1 result is ' + str(calculate_steps(test_1))

    test_2 = 12
    print 'Test 2 result is ' + str(calculate_steps(test_2))

    test_3 = 23
    print 'Test 3 result is ' + str(calculate_steps(test_3))

    test_4 = 1024
    print 'Test 4 result is ' + str(calculate_steps(test_4))

    my_input = 347991
    print 'My result is ' + str(calculate_steps(my_input))

