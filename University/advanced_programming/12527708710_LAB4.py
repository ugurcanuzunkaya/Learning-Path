from math import sin
from math import cos
from math import atan

mullist = ['Multiplication', "multiplication", "MULTIPLICATION", "mul", "Mul", "MUL"]
addlist = ["Addition", "addition", "ADDITION", "add", "Add", "ADD"]
sublist = ["Substraction", "substraction", "SUBSTRACTION", "sub", "Sub", "SUB"]
divlist = ["Division", "division", "DIVISION", "Div", " div", "DIV"]


class ComplexMethodsReal:
    real = 0
    imaginary = 0
    real2 = 0
    imaginary2 = 0
    angle = 0
    angle2 = 0

    def __init__(self, real, imaginary, real2, imaginary2):
        self.real = real
        self.imaginary = imaginary
        self.real2 = real2
        self.imaginary2 = imaginary2
        self.angle = atan(imaginary/real)
        self.angle2 = atan(imaginary2/real2)

    def addition(self):
        return self.real + self.real2, self.imaginary + self.imaginary2

    def substraction(self):
        return self.real - self.real2, self.imaginary - self.imaginary2

    def multiplication(self):
        return self.real * self.real2, self.angle + self.angle2

    def division(self):
        return self.real / self.real2, self.angle - self.angle2


class ComplexMethodsAbsolute:
    absolute = 0
    angle = 0
    absolute2 = 0
    angle2 = 0

    def __init__(self, absolute, angle, absolute2, angle2):
        self.imaginary = absolute * sin(angle)
        self.real = absolute * cos(angle)
        self.imaginary2 = absolute2 * sin(angle2)
        self.real2 = absolute2 * cos(angle2)
        self.angle = angle
        self.angle2 = angle2

    def addition(self):
        return self.real + self.real2, self.imaginary + self.imaginary2

    def substraction(self):
        return self.real - self.real2, self.imaginary - self.imaginary2

    def multiplication(self):
        return self.real * self.real2, self.angle + self.angle2

    def division(self):
        return self.real / self.real2, self.angle - self.angle2


ask = input("What type you are writing? (absolute value and phase angle or real and imaginary parts)")

if ask == "real and imaginary parts":
    firstcomplexreal = float(input("Enter real part of first complex number: "))
    firstcompleximaginary = float(input("Enter imaginary part of first complex number: "))
    secondcomplexreal = float(input("Enter real part of second complex number: "))
    secondcompleximaginary = float(input("Enter imaginary part of second complex number: "))
    complexnumbers = ComplexMethodsReal(firstcomplexreal, firstcompleximaginary, secondcomplexreal,
                                        secondcompleximaginary)
    arithmeticoperation = input("Which arithmetic operation you want? ")
    if arithmeticoperation in addlist:
        a, b = complexnumbers.addition()
        print(a, "+", str(b) + "_")
    if arithmeticoperation in sublist:
        a, b = complexnumbers.substraction()
        print(a, "+", str(b) + "_")
    if arithmeticoperation in mullist:
        a, b = complexnumbers.multiplication()
        print(a, "∠", b)
    if arithmeticoperation in divlist:
        a, b = complexnumbers.division()
        print(a, "∠", b)

if ask == "absolute value and phase angle":
    firstcomplexabsolute = float(input("Enter absolute value of first complex number: "))
    firstcomplexangle = float(input("Enter phase angle of first complex number: "))
    secondcomplexabsolute = float(input("Enter absolute value of second complex number: "))
    secondcomplexangle = float(input("Enter phase angle of second complex number: "))
    complexnumbers = ComplexMethodsAbsolute(firstcomplexabsolute, firstcomplexangle, secondcomplexabsolute,
                                            secondcomplexangle)
    arithmeticoperation = input("Which arithmetic operation you want? ")
    if arithmeticoperation in addlist:
        a, b = complexnumbers.addition()
        print(a, "+", str(b) + "_")
    if arithmeticoperation in sublist:
        a, b = complexnumbers.substraction()
        print(a, "+", str(b) + "_")
    if arithmeticoperation in mullist:
        a, b = complexnumbers.multiplication()
        print(a, "∠", b)
    if arithmeticoperation in divlist:
        a, b = complexnumbers.division()
        print(a, "∠", b)
