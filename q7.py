from fractions import Fraction
from itertools import combinations
import matplotlib.pyplot as plt


def get_numbers(n):
    all_numbers = {Fraction(1, 1)}
    for _ in range(n):
        new_numbers = set()
        for number in all_numbers:
            new_numbers.add(Fraction(number.denominator, 2 * number.numerator))
        all_numbers |= new_numbers
        new_numbers.clear()
        for pair in combinations(all_numbers, 2):
            new_numbers.add(
                Fraction(
                    pair[0].numerator + pair[1].numerator,
                    pair[0].denominator + pair[1].denominator,
                )
            )
        all_numbers |= new_numbers
    return all_numbers


if __name__ == "__main__":
    m = ["blue", "green", "yellow", "orange", "red", "purple"]
    for i in range(6, 0, -1):
        temp = get_numbers(i)
        plt.scatter([float(k) for k in temp], [i for _ in temp], marker=",", c=m[i - 1])
    plt.xlabel("Value")
    plt.ylabel("Iteration")
    plt.show()
