def readdata(infile):
    data = open(infile).read().split('\n\n')
    data = [ i.replace('\n', ' ') for i in data ]

    return data


def decoder(d):
    d = d.replace('F', '0').replace('B', '1')
    d = d.replace('L', '0').replace('R', '1')
    rowno, colno = int(d[:7], 2), int(d[7:], 2)
    seatID = rowno * 8 + colno
    return seatID


def dataprep(data):
    return [i.replace('\n', ' ').strip() for i in data]


def countq(data):
    return len(set(data.replace(' ', '')))


def part01(data):
    yesq = [countq(d) for d in data]
    print(f'Part 1 - Total sum =  {sum(yesq)}')


def countq2(data):
    q = set(data.split(' ')[0])
    for d in data.split(' '):
        q = q.intersection(set(d))

    return len(q)


def part02(data):
    yesq = [countq2(d) for d in data]
    print(f'Part 2 - Total sum =  {sum(yesq)}')


if __name__ == '__main__':
    infile = './data/input.day06'
    data = readdata(infile)
    dataE = dataprep(data)
    part01(dataE)
    part02(dataE)
