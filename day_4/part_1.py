'''



'''

MY_FILENAME = 'input.txt'


def check_duplicates(filename):
    with open(filename) as myFile:
        passphrases = [line.split() for line in myFile]

    valid_count = 0

    for passphrase in passphrases:
        # For Part 2, sort each word in the passphrase to make them the same.
        passphrase = [''.join(sorted(p)) for p in passphrase]
        if len(passphrase) != len(set(passphrase)):
            continue
        else:
            valid_count += 1

    print '# of valid passphrases are: ' + str(valid_count)
    return

if __name__ == '__main__':
    check_duplicates(MY_FILENAME)