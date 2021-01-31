def readdata(infile):
    data = open(infile).read().split('\n')[:-1]

    return data


def decoder(d):
    d = d.replace('F', '0').replace('B', '1')
    d = d.replace('L', '0').replace('R', '1')
    rowno, colno = int(d[:7], 2), int(d[7:], 2)
    seatID = rowno * 8 + colno
    return seatID


def dataprep(data):
    return [decoder(d) for d in data]


def part01(data):
    print(f'Part 1 - Max SeatID = {max(data)}')


def part02(data):
    data.sort()
    for i in range(len(data)):
        if data[i+1] - data[i] == 2:
            print(f'Part 2 - Your SeatID is = {data[i] + 1}')
            return
    return


if __name__ == '__main__':
    infile = './data/input.day05'
    data = readdata(infile)
    dataE = dataprep(data)
    part01(dataE)
    part02(dataE)
