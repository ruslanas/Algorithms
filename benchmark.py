# -*- coding: utf-8 -*-
# run on regular intervals to collect metric about computer performance during work day
# results are analyzed by R later

__author__ = 'Ruslanas Balčiūnas'

from msort import merge_sort
from os.path import expanduser
import time
import timeit
import random

l = []

# generate same sequence on every run
random.seed(1)

for i in range(0, 100000):
    l.append(random.randrange(0, 100))

def test():
    merge_sort(l)

if __name__ == '__main__':
    # write duration and current time to a file
    t = timeit.timeit("test()", number=1, setup='from __main__ import test')

    f = open('C:\\Users\\Ruslanas\\PycharmProjects\\Algorithms\\benchmark.dat', 'a')

    output = "%s %s\n" % (t, time.strftime('%Y-%m-%d %H:%M:%S'))
    f.write(output)
    f.close()
    print('Done.')
