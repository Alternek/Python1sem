# Биссектриса из среднего угла

def len_segment(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def len_bis(a, b, c):
    return (a * b * (a + b + c) * (a + b - c)) ** 0.5 / (a + b)


A = [int(i) for i in input("Введите через пробел 2 целочисленные координаты 1 точки треугольника:").split()]
B = [int(i) for i in input("Введите через пробел 2 целочисленные координаты 2 точки треугольника:").split()]
C = [int(i) for i in input("Введите через пробел 2 целочисленные координаты 3 точки треугольника:").split()]
AB = len_segment(A, B)
BC = len_segment(B, C)
AC = len_segment(A, C)
if AB <= BC <= AC or AC <= BC <= AB:
    bis = len_bis(AB, AC, BC)
elif BC <= AB <= AC or AC <= AB <= BC:
    bis = len_bis(BC, AC, AB)
else:
    bis = len_bis(AB, BC, AC)
print('Длина биссектрисы среднего угла - {:.5g}'.format(bis))
