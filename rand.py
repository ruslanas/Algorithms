# pseudo random number generators
__author__ = 'Ruslanas'

def middle_square(seed, digits=4):
    square = seed * seed
    half_digits = digits >> 1
    return int(square % 10**(digits + half_digits) / 10**half_digits)

def print_sequence(seed, func=middle_square, length=10):
    n = seed
    for i in range(length):
        n = func(n)
        print(n)

def linear_congruential_sequence(seed, m=30, a=31, c=7):
    return (a * seed + c) % m

def find_loops(length=5, digits=4):
    """
    Find circular sequences less than length long
    :param length:
    :param digits:
    :return:
    """
    bad_seeds = []
    for seed in range(10**digits - 1):
        n = seed
        for k in range(length):
            n = middle_square(n)
            # loop closed or known loop encountered
            bad = n in bad_seeds
            if n == seed or bad:
                if not bad:
                    bad_seeds.append(seed)
                    print("%d in %d steps closes" % (seed, k+1))
                else:
                    print("%d in %d steps reaches bad seed %d" % (seed, k+1, n))
                break
    return bad_seeds

if __name__ == '__main__':
    print(find_loops())