class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    a = int(input("Введите длину прямоугольника: "))
    b = int(input("Введите ширину прямоугольника: "))
    obj = rectangle(a, b)
    print("Площадь прямоугольника:", obj.area())



