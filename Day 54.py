import math


def sum_of_series(n):
    """
    Calculates the sum of the series:
    1/1! + 1/2! + 1/3! + ... + 1/N!

    Parameters:
        n (int): The number of terms in the series.

    Returns:
        float: The sum of the series.
        str: Error message if n is not positive.
    """
    if n <= 0:
        return "N should be a positive integer."

    total_sum = 0

    for i in range(1, n + 1):
        total_sum += 1 / math.factorial(i)

    return total_sum


try:
    N = int(input("Enter a positive integer N: "))

    if N <= 0:
        print("Please enter a positive integer.")
    else:
        result = sum_of_series(N)
        print(f"The sum of the series for N = {N} is: {result:.6f}")

except ValueError:
    print("Invalid input! Please enter a positive integer.")