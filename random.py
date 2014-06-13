# pseudo random number generators
__author__ = 'Ruslanas'

def middle_square(seed, digits=4):
    square = seed * seed
    return int(square % 10**int(digits + digits / 2) / 10**int(digits / 2))


if __name__ == '__main__':
    # generate circular sequence
    n = 540
    for i in range(10):
        n = middle_square(n)
        print(n)