# sort lines in msort.py
__author__ = 'Ruslanas Balčiūnas'

from msort import merge_sort

f = open('msort.py', encoding='utf-8')
lines = f.readlines()
f.close()

print('Sorting', len(lines), 'lines')

stripped = []

for line in lines:
    stripped.append(line.strip())

def test():
    merge_sort(stripped)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", number=10000, setup='from __main__ import test'))
