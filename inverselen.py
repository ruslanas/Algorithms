__author__ = 'Ruslanas Balčiūnas'

# brute force
def inverse_length(l):
    n = 0
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                n += 1
    return n
