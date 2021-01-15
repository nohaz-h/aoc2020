infile = './data/input.day01'

data = open(infile).read().split('\n')[:-1]
target = 2020

data = [int(i) for i in data]


def answer(data, target):
    for i in data:
        for j in data:
            if i + j == target:
                return (i, j, i*j)


def answer2(data, target):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == target:
                    return (i, j, k, i*j*k)


part01 = answer(data, 2020)
print(f'{part01[0]} * {part01[1]} = {part01[2]}')
#
part02 = answer2(data, 2020)
print(f'{part02[0]} * {part02[1]} * {part02[2]} = {part02[3]}')
#
