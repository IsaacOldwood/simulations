import math
from fractions import Fraction as frac

def farey(num,iterations=100,print_iterations=10):
    # Initialise.
    a = 1
    b = 0
    c = 1
    d = 1
    mediant = frac(a+b,c+d)
    i = 0
    print (f'Lower: {b}/{d}  Mediant: {a+b}/{c+d}  Upper: {a}/{c}')

    # Loop.
    while (mediant != num) and (i < iterations):
        if (b/d <= num <= mediant):
            a = mediant.numerator
            c = mediant.denominator
        elif (mediant <= num <= a/c):
            b = mediant.numerator
            d = mediant.denominator
        else:
            print(f'Oops should not get here. {num} {mediant}')

        # Recalculate.
        mediant = frac(a+b,c+d)

        # Print current iterations.
        if (i % print_iterations == 0):
            print (f'Lower: {b}/{d}  Mediant: {a+b}/{c+d}  Upper: {a}/{c}')
        # Increment.
        i += 1

    # Print fraction.
    if (mediant == num):
        print (f'Exact fraction found! Your input: {num} Fraction: {str(mediant)}')
    elif (i == iterations):
        print (f'Maximum iterations reached. Your input: {num} Approximation: {str(mediant)}')
    else:
        print('Should not be printed')

if __name__ == '__main__':
    farey(0.75, 1000, 100)