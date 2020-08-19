PI = 3.14159265359

def triangle_area(base, height):
    return base*height/2


def square_perimeter(edge):
    return 4*edge


def square_area(edge):
    return edge ** 2


def circle_perimeter(radius):
    return 2*PI*radius


def circle_area(radius):
    return PI * radius ** 2


print(circle_area(1))
