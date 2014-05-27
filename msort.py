__author__ = 'Ruslanas Balčiūnas'

def msort(l):
    if len(l) < 2:
        return l

    i = j = 0
    c = []

    half = len(l) >> 1

    a = msort(l[:half])
    b = msort(l[half:])

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
