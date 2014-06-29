__author__ = 'Ruslanas'


def ksa(key):
    s = []
    for i in range(255):
        s.append(i)

    j = 0
    for i in range(255):
        j = (j + s[i] + ord(key[i % len(key)])) % 256
        tmp = s[j]
        s[j] = s[i]
        s[i] = tmp

    return s

def prga(key, length):
    s = ksa(key)
    i = 0
    j = 0
    out = []
    for k in range(length):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp

        out.append(hex(s[(s[i] + s[j]) % 256]))

    return out

if __name__ == '__main__':
    print(prga("Key", 10))