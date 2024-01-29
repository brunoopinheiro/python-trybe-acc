from math import factorial


def map_factorial(numbers: list):
    result = []

    for num in numbers:
        result.append(factorial(num))

    return result


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    map_factorial(input_list)
