infile = './data/input.day03'

data = open(infile).read().split('\n')[:-1]


def answer(data, dx, dy):
    maplen = len(data)
    mapwid = len(data[0])

    x, y = 0, 0
    countTree = 0
    counter = 0

    while True:
        x = ((x + dx) % mapwid)
        y += dy

        if data[y][x] == '#':
            countTree += 1

        counter += 1
        if (y >= maplen - 1):
            print(f'for slope ({dx}, {dy}) Total trees = {countTree}')
            return countTree


#
total = answer(data, 1, 1) * \
        answer(data, 3, 1) * \
        answer(data, 5, 1) * \
        answer(data, 7, 1) * \
        answer(data, 1, 2)
print(f'Multiplication of trees found is {total}')
