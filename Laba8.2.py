import math

try:
    def u(x, y):
        return x - y

    def v(x, y):
        return x**2 + math.sin(y)

    def F(u, v):
        return math.exp(u*v) + v

    def calculate_R(x, y):
        u_1 = u(x, y)
        v_1 = v(x, y)
        F_1 = F(u_1, v_1)
        R = math.log(abs(F_1)) + math.sqrt(u_1 * v_1)
        return R

    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    if y <= 1 and y >= -1:
        result = calculate_R(x, y)
        print("Значение R:", result)
    else:
        print('Введено значение, не удовлетворяющее отрезку [-1, 1]')
except ValueError:
    print('Введено неверное значение')
