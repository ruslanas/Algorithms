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


def rc4_encrypt(key, plain_text):
    plain_text = plain_text.encode('utf-8')
    key_stream = prga(key, len(plain_text))
    encrypted = ''

    for i in range(len(plain_text)):
        encrypted += "%02x" % xor(key_stream[i], plain_text[i])

    return encrypted.upper()


def rc4_decrypt(key, cypher):
    key_stream = prga(key, len(cypher) >> 1)
    decrypted = []
    for i in range(0, len(cypher), 2):
        b = (xor(key_stream[i >> 1], int('0x' + cypher[i:i+2], 16)))
        decrypted.append(b)

    return bytes(decrypted).decode('utf-8')


def main():
    print(rc4_decrypt('Key', rc4_encrypt('Key', 'Plaintext')))
    print(rc4_encrypt('Wiki', 'pedia'))
    print(rc4_encrypt('Secret', 'Attack at dawn'))


if __name__ == '__main__':
    main()
