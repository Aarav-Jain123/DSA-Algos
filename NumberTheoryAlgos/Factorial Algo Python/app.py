def factorial_calculator(n):
    if n == 0:
        return 0
    else:
        # numbers_list = []
        factorial = 1
        while n >= 1:
            factorial *= n
            # numbers_list.append(n)
            n -= 1
        return factorial