"""
Problem 2

Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

import argparse
import pandas as pd

def main(n_max):
    df = pd.DataFrame()
    df['fib'] = fib(n_max=n_max)
    df['even'] = is_divisible(df['fib'], 2) * df['fib']
    return df['even'].sum(), df

def fib(n_max):
    m = 1
    n = 1
    fib_list = []
    while n <= n_max:
        fib_list.append(n)
        _ = n
        n = m + n
        m = _
    return fib_list

def is_divisible(number, divisor):
    return (number % divisor == 0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--n_max', type=int)
    parser.add_argument('-v','--verbose', action='store_true', default=False)
    parser.add_argument('-d','--description', action='store_true', default=False)
    args = parser.parse_args()
    if args.description:
        print(__doc__)
    sol, _ = main(n_max=args.n_max)
    print(f'Solution: {sol}')
    if args.verbose:
        print(_)
else:
    sol, _ = main(n_max=4000000)
    print(f'Solution: {sol}')


