__author__ = 'Ruslanas'

from operator import xor


def ksa(key):
    s = []
    for i in range(256):
        s.append(i)

    j = 0
    key_length = len(key)
    for i in range(len(s)):
        j = (j + s[i] + ord(key[i % key_length])) % 256
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp

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

        out.append(s[(s[i] + s[j]) % 256])

    return out


def main():
    print(rc4('Key', 'Plaintext'))
    print(rc4('Wiki', 'pedia'))
    print(rc4('Secret', 'Attack at dawn'))


def rc4(key, plain_text):
    key_stream = prga(key, len(plain_text))
    encrypted = ''

    for i in range(len(plain_text)):
        encrypted += "%02x" % xor(key_stream[i], ord(plain_text[i]))

    return encrypted.upper()


if __name__ == '__main__':
    main()
