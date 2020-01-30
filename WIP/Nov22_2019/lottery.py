PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

legal_numbers = list()


def num_prime_factors(num):

    global PRIMES

    num_primes = 0

    for prime in PRIMES:
        if num % prime == 0:
            num_primes += 1

    return num_primes


def init_globals():

    global legal_numbers

    legal_numbers = range(1, 71)


def remove_primes():

    global legal_numbers
    global PRIMES

    remove = list()

    for num in legal_numbers:
        if num in PRIMES:
            remove.append(num)

    for num in remove:
        legal_numbers.remove(num)

def remove_single_prime_factors():

    global legal_numbers

    remove = list()

    for num in legal_numbers:
        if num_prime_factors(num) == 1:
            remove.append(num)
            print "{0}, {1}".format(num, num_prime_factors(num))

    for num in remove:
        legal_numbers.remove(num)


def find_sets_equal_product():

    global legal_numbers
    pass



def main():

    global legal_numbers

    init_globals()
    print legal_numbers

    remove_primes()
    print legal_numbers

    remove_single_prime_factors()
    print legal_numbers


main()
