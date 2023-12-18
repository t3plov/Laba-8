try:
    print('Все вводимые значения типа float(вещественные)')

    def CircleS(R):
        S = 2 * 3.14 * R
        return S

    rad1 = float(input('Введите радиус круга:'))
    S1 = CircleS(rad1)
    print('Площадь первого круга:', S1)

    rad2 = float(input('Введите радиус круга:'))
    S2 = CircleS(rad2)
    print('Площадь второго круга:', S2)

    rad3 = float(input('Введите радиус круга:'))
    S3 = CircleS(rad3)
    print('Площадь третьего круга:', S3)
except ValueError:
    print('Введено неверное значение!')

