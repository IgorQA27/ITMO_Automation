class rectangle():
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length

    def area(self):
        return self.weight * self.length


a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
obj = rectangle(a, b)
print("Площадь прямоугольника:", obj.area())

print()



class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


    def multiplication(self):
        return self.a * self.b


    def division(self):
        return self.a / self.b


    def subtraction(self):
        return self.a - self.b


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
obj = Math(a, b)
print("Результат сложения:", obj.addition())
print()


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
obj = Math(a, b)
print("Результат деления:", obj.multiplication())


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
obj = Math(a, b)
print("Результат умножения:", obj.division())
print()


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
obj = Math(a, b)

print("Результат вычитания:", obj.substraction())
print()
















