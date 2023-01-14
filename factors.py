#!/usr/bin/python3
import sys
''' This is a Factorization Challenge '''


def factorize(n):
    '''
        factorize(n)
        ===========
        Computes the factors of a number n
        ---------------------------------
    '''
    if type(n) is not int:
        raise TypeError('n must be a positive integer')

    for d in range(2, 10):
        if n % d == 0:
            print("{}={}*{}".format(n, n // d, d))
            return

    sqrn = n ** 0.5 #get the square root of n
    prime = 11;

    while prime < sqrn:
        if n % prime == 0:
            print("{}={}*{}".format(n, n // prime, prime))
            return
        else:
            prime += 2
    
    print("{}={}*{}".format(n, n , 1))
    return

def factors(filename):
    with open(filename, encoding='utf-8') as my_file:
        for i in my_file:
            result = factorize(int(i))  

if __name__ == "__main__":
    factors(sys.argv[1])        
        
'''
    for div in range(2, 10):
        
        try:
            if n % div == 0 and div != 1:
                print("{}={}*{}".format(n, n / div, div))
                break
            elif div in range(11, n/2 + 1):
                if n % div == 0:
                    print("{}={}*{}".format(n, n / div, div))
                    break 
        
        except Exception:
            for i in range(3, round(n ** 0.5), 2):
                if n % i == 0:
                    print("{}={}*{}".format(n, n / i, i))

    if __name__ == "__main__":
        import doctest
        import sys
    
        f = sys.argv[1]
        doctest.testfile(f)
'''