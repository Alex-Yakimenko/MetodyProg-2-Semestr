import random
import math

N = 1000000
a = 10
h = 10


def Forth(N):

    oper = 0
    i = 0

    while i < N:
        x = random.randrange(-10, 10, 1)
        y = random.randrange(-10, 10, 1)
        z = random.randrange(-10, 10, 1)

        if (x * x) / 4 + (y * y) / 9 <= z:
            if 1 <= z <= 3:
                oper = oper + 1

        i = i + 1

    return oper / N


def Third(N):

    oper = 0
    i = 0

    while i < N:
        x_1 = random.randrange(-1000, 1000, 1)
        x_2 = random.randrange(-1000, 1000, 1)
        x_3 = random.randrange(-1000, 1000, 1)
        x_4 = random.randrange(-1000, 1000, 1)

        if x_1 * x_1 + x_2 * x_2 + x_3 * x_3 <= x_4 * x_4:
            if x_4 >= 1:
                oper = oper + 1

        i = i + 1

    return oper / N


def Second(a, h, N):

    HY = 0.0
    oper = 0
    i = 0

    while i < N:
        x_1 = random.randrange(-10, 10, 1)
        x_2 = random.randrange(-10, 10, 1)
        y_1 = random.randrange(-10, 10, 1)
        y_2 = random.randrange(-10, 10, 1)
        z_1 = random.randrange(-10, 10, 1)
        z_2 = random.randrange(-10, 10, 1)
        #print(x_1, ' ', x_2, ' ', y_1, ' ', y_2, ' ', z_1, ' ', z_2)

        if x_1 * x_1 + y_1 * y_1 + z_1 * z_1 <= a * a:
            if x_2 * x_2 + y_2 * y_2 + z_2 * z_2 <= h * h:
                HY = HY + math.sqrt((x_1 - x_2) * (x_1 - x_2) + (y_1 - y_2) * (y_1 - y_2) + (z_1 - z_2) * (z_1 - z_2))
                #print(HY)

        i = i + 1

    return (1 / HY) / N


def First(a, h, N):

    i = 0
    HY = 0
    oper = 0

    while i < N:
        x_1 = random.randrange(-100, 100, 1)
        x_2 = random.randrange(-100, 100, 1)
        x_3 = random.randrange(-100, 100, 1)
        x_4 = random.randrange(-100, 100, 1)
        x_5 = random.randrange(-100, 100, 1)

        if x_1 * x_1 + x_2 * x_2 + x_3 * x_3 + x_4 * x_4 <= a * a:
            if (-h / 2) <= x_5 <= (h / 2):
                HY = HY + x_5 * x_5

        i = i + 1

    return HY / N

print(Second(a,h,N))
