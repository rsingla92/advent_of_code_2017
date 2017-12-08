'''

Advent of Code 2017, day 6 part 1.

Given a sequence of numbers, find the max number and redistribute its value
among the other numbers to create a new sequence.

Repeat this process until you've encountered a sequence you've found before.
Count how many times it takes until you've found this sequence.

'''

from math import ceil

TEST_INPUT = '0 2 7 0'
MY_INPUT = '11 11 13 7 0 15 5 5 4 4 1 1 7 1 15 11'


def run_redistribution(old_config):
    num_banks = len(old_config)

    max_val = max(old_config)
    max_idx = old_config.index(max_val)
    old_config[max_idx] = 0

    subtrahend = ceil(float(max_val) / float(num_banks))

    val = max_val
    idx = max_idx

    while val > 0:
        idx += 1
        old_config[idx % num_banks] += subtrahend
        val -= subtrahend

    print 'New Config is: ' + str(old_config)
    redistributed_config = old_config
    return redistributed_config


def detect_infinite_cycles(initial_config):

    config_dict = {}
    config = initial_config.split()
    config = [int(i) for i in config]

    count = 0

    count_dict = {}

    while True:
        new_config = run_redistribution(config)
        count += 1
        count_dict[count] = str(new_config)

        if str(new_config) in config_dict:
            print 'Detected previously seen config: ' + str(new_config)
            print 'Redistributions ran ' + str(count)

            config_instances = {i for i, v in count_dict.items() if v == str(new_config)}

            config_instances = list(config_instances)
            print 'There are ' + str(config_instances[1] - config_instances[0]) + ' steps in the cycle'
            break
        else:
            config_dict[str(new_config)] = 1

    return


if __name__ == '__main__':
    detect_infinite_cycles(MY_INPUT)