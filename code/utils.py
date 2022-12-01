def rl(fn):
    file1 = open(fn, 'r')
    return [l.strip() for l in file1.readlines()]