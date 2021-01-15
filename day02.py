infile = './data/input.day02'

data = open(infile).read().split('\n')[:-1]

def answer(data):
    counter = 0
    for d in data:
        pos, letter, password = d.split(' ')
        minpos, maxpos = pos.split('-')
        # only read first character in letter
        letter = letter[0]
        minpos, maxpos = int(minpos), int(maxpos)
        #
        countletter = password.count(letter)
        #
        if (countletter >= minpos) and (countletter <= maxpos):
            counter += 1

    print(f'Total valid password is {counter}')
    return counter


def answer2(data):
    counter = 0
    for d in data:
        pos, letter, password = d.split(' ')
        minpos, maxpos = pos.split('-')
        # only read first character in letter
        letter = letter[0]
        minpos, maxpos = int(minpos), int(maxpos)
        #
        countletter = password.count(letter)
        #
        test1 = password[minpos - 1] == letter
        test2 = password[maxpos - 1] == letter
        if (test1 or test2) and (not (test1 and test2)):
            counter += 1

    print(f'Total valid password is {counter}')
    return counter


print(len(data))
answer(data)
answer2(data)
##

