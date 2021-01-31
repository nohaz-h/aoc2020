def readdata(infile):
    # data = open(infile).read().split('\n')
    data = open(infile).read()
    return data


def dataprep(data):
    data = data.replace('bags', 'bag').replace('no ', '0 ')
    data = data.replace('bag.', 'bag')
    data = data.split('\n')[:-1]
    return data


def searchbag(data, pattern):
    out = []
    for d in data:
        d1, d2 = d.split(' contain ')
        if d2.count(pattern) > 0:
            out.append(d1)
    return out


def part01(data, bag):
    listbags = set(searchbag(data, bag))
    patterns = listbags

    for _ in range(100):
        temp = []
        for b in patterns:
            _ = [temp.append(i) for i in searchbag(data, b)]
        patterns = set(temp) - listbags
        listbags = listbags.union(set(temp))
        if len(patterns) == 0:
            break

    print('Part 1 - Total number of colour bags containing ' +
          f'at least one "{bag}" = {len(listbags)}')


def sumbag(data, pattern):
    out = []
    for d in data:
        d1, d2 = d.split(' contain ')
        if d1.count(pattern) > 0:
            for d2d in d2.split(', '):
                d2dv, d2dn = d2d.split(' ', 1)
                _ = [out.append(i) for i in [d2dn] * int(d2dv)]
            return out


def part02(data, bag):
    patterns = [i for i in sumbag(data, bag)]
    sumbag2 = len(patterns)

    for _ in range(100):
        temp = []
        for p in set(patterns):
            _ = [temp.append(i) for i in sumbag(data, p) * patterns.count(p)]

        if len(temp) == 0:
            print(f'Part 2 - Total number of bags inside "{bag}"= {sumbag2}')
            return

        sumbag2 += len(temp)
        patterns = temp


if __name__ == '__main__':
    infile = './data/input.day07'
    data = readdata(infile)
    dataE = dataprep(data)

    bag = 'shiny gold bag'
    part01(dataE, bag)
    part02(dataE, bag)
