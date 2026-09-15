def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factor = []
    for i in range(1, number + 1):
        if number % i == 0:
            factor.append(i)
    if sum(factor) - number == number:
        return "perfect"
    elif sum(factor) - number > number:
        return "abundant"
    elif sum(factor) - number < number:
        return "deficient"