def sum_two_numbers(a, b):
    """
    Retorna a soma de dois números recebidos por parâmetro.

    Exemplos
    --------
    >>> sum_two_numbers(0, 0)
    0
    >>> sum_two_numbers(1, 2)
    3
    >>> sum_two_numbers(1.5, 2)
    3.5
    >>> sum_two_numbers("2", 2)
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    """
    return a + b
