# sort lines in msort.py
__author__ = 'Ruslanas Balčiūnas'

from msort import msort

f = open('msort.py', encoding='utf-8')
lines = f.readlines()
f.close()

stripped = []

for line in lines:
    stripped.append(line.strip())

def test():
    msort(stripped)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", number=10000, setup='from __main__ import test'))
