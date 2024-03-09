from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print('S =', rect_1.get_area())
print('S =', rect_2.get_area())

squara_1 = Square(5)
squara_2 = Square(10)

print(squara_1.get_area_square(), squara_2.get_area_square())

figures = [rect_1, rect_2, squara_1, squara_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

radius = Circle(4)
print(radius.get_area_circle())

