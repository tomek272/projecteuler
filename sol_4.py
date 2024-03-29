"""
Problem 4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main(n_max):
    palindromes = []
    for n in range(1,n_max+1):
        m = 1
        for m in range(1,n_max+1):
            product = m * n
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
    return max(palindromes), palindromes


if __name__ == "__main__":
    solution, _ = main(n_max=999)
    print(solution)