from math import pi

# calculates the circumference
# parameters: r (radius)
def circumference(r):
    return 2 * pi * r

# calculates the area of the circle
# parameters: r (radius)
def circle_area(r):
    return pi * r * r

# calculates the area of the sphere
# parameters: r (radius)
def sphere_area(r):
    return 4 * pi * r * r

# calculates the volume of the sphere
# parameters: r (radius)
def sphere_volume(r):
    return 4 / 3 * pi * r * r * r

# calculates the perimeter of the rectangle
# parameters: x, y (sides)
def rectangle_perimeter(x, y):
    return 2 * (x + y)

# calculates the area of the rectangle
# parameters: x, y (sides)
def rectangle_area(x, y):
    return x * y

print("\ncircumference(10) C =", circumference(10))
print("circle_area(10) A =", circle_area(10))
print("sphere_area(10) A =", sphere_area(10))
print("sphere_volume(10) V =", sphere_volume(10))
print("rectangle_perimeter(10) P =", rectangle_perimeter(10, 20))
print("rectangle_area(10) V =", rectangle_area(10, 20), "\n")
