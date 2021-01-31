def readdata(infile):
    data = open(infile).read().split('\n\n')[:-1]
    data = [i.replace('\n', ' ') for i in data]

    return data


def dataprep(data):
    passports = []
    for d in data:
        passfield = {}
        for dd in d.split(' '):
            ddk, ddv = dd.split(':')
            passfield[ddk] = ddv

        passports.append(passfield)

    return passports


def part01(data):
    counter = 0
    for p in passports:
        maxfields = 8 if 'cid' in p.keys() else 7
        counter = counter + 1 if len(p.keys()) == maxfields else counter

    print(f'Part 1 - Total valid passports = {counter}')


def checkbyr(data):
    if 'byr' in data.keys():
        v = data['byr']
        if v.isnumeric():
            if int(v) >= 1920 and int(v) <= 2002:
                return True
    return False


def checkiyr(data):
    if 'iyr' in data.keys():
        v = data['iyr']
        if v.isnumeric():
            if int(v) >= 2010 and int(v) <= 2020:
                return True
    return False


def checkeyr(data):
    if 'eyr' in data.keys():
        v = data['eyr']
        if v.isnumeric():
            if int(v) >= 2020 and int(v) <= 2030:
                return True
    return False


def checkhgt(data):
    if 'hgt' in data.keys():
        v = data['hgt']
        if v[-2:] == 'cm':
            if int(v[:-2]) >= 150 and int(v[:-2]) <= 193:
                return True

        if v[-2:] == 'in':
            if int(v[:-2]) >= 59 and int(v[:-2]) <= 76:
                return True
    return False


def countmatch(data, pattern):
    return sum([pattern.count(d) for d in data])


def checkhcl(data):
    if 'hcl' in data.keys():
        v = data['hcl']
        if v[0] == '#' and len(v) == 7 and \
                countmatch(v[1:], 'abcdef0123456789') == 6:
            return True
    return False


def checkecl(data):
    if 'ecl' in data.keys():
        v = data['ecl']
        if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    return False


def checkpid(data):
    if 'pid' in data.keys():
        v = data['pid']
        if len(v) == 9 and countmatch(v, '0123456789') == 9:
            return True
    return False


def part02(passports):
    counter = 0
    for p in passports:
        checks = checkpid(p) + checkecl(p) + checkhcl(p) + checkhgt(p)
        checks = checks + checkeyr(p) + checkiyr(p) + checkbyr(p)
        if checks == 7:
            counter += 1
    print(f'Part 2 - Total valid passports = {counter}')


if __name__ == '__main__':
    infile = './data/input.day04'
    data = readdata(infile)
    passports = dataprep(data)
    part01(passports)
    part02(passports)
