try:
    def maxdig(N):
        if N < 10:
            return N
        else:
            last_digit = N % 10
            remaining_digits = N // 10
            max_rest = maxdig(remaining_digits)
            return max(last_digit, max_rest)

    N = int(input("Введите целое неотрицательное число N: "))
    result = maxdig(N)
    if N > 0:
        print("Наибольшая цифра в числе N:", result)
    else:
        print('Введено отрицательное число!')

except ValueError:
    print('Введено нецелочисленное значение числа N!')
