# -*- coding: utf-8 -*-
__author__ = 'Ruslanas Balčiūnas'

# divide and conquer algorithm
def merge_sort(l):
    if len(l) < 2:
        return l

    i = j = 0
    c = []

    half = len(l) >> 1

    a = merge_sort(l[:half])
    b = merge_sort(l[half:])

    for k in range(0, len(l)):

        if i >= len(a) or j >= len(b):
            c += b[j:] + a[i:]
            return c

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    return c
