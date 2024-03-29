import pandas as pd

def main(upper_limit):

# Create main column with numbers from 0 to upper_limit minus one.
    df = pd.DataFrame()
    r = range(0,upper_limit)
    df['number'] = r

# Create columns which indicate whether a number is divisible by 3 or 5 and any.
    df['div_by_3'] = is_divisible(df['number'], 3)
    df['div_by_5'] = is_divisible(df['number'], 5)
    df['div_any'] = df['div_by_3'] | df['div_by_5']

# Create column which only lists numbers which are divisible by 3 or 5.
    df['divisible_numbers'] = df['number'] * df['div_any']

    sol = df['divisible_numbers'].sum()

    return sol, df

def is_divisible(number, divisor):
    return (number % divisor == 0)

if __name__ == "__main__":
    upper_limit = 1000

    sol, df = main(upper_limit)
    print(f'Solution: {sol}')
