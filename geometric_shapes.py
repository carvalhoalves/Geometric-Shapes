from abc import ABC, abstractmethod
from clear import clear_screen
from constant import CIRCLE, RECTANGLE, TRIANGLE
from input_analysis import analyze_number
from math import pi, sqrt


class Shape(ABC):  # Geometric Shape
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def load_input(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def __diameter(self):
        return 2 * self.__radius

    @classmethod
    def load_input(cls):
        print('\n\nVocê escolheu realizar o cálculo da área de um círculo.'
              '\n\nO valor referente a seu raio deve ser informado em centímetros.')

        radius = input('\n\nDigite o valor do raio deste círculo e pressione ENTER.'
                       '\n> ')
        radius = analyze_number(radius, 'radius')

        return Circle('Círculo', radius)

    def __str__(self):
        return f'\n . {self.name}' \
               f'\n' \
               f'\n    . Área' \
               f'\n        {self.area():.2f} cm²' \
               f'\n' \
               f'\n    . Diâmetro' \
               f'\n        {self.__diameter()} cm' \
               f'\n' \
               f'\n    . Raio' \
               f'\n        {self.__radius} cm'


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length
        self.__width = width

    @staticmethod
    def __analyze_shape(length, width):
        return 'Retângulo' if length != width else 'Quadrado'

    def area(self):
        return self.__length * self.__width

    @classmethod
    def load_input(cls):
        print('\n\nVocê escolheu realizar o cálculo da área de um retângulo.'
              '\n\nOs valores referentes a seu comprimento e sua largura devem ser informados em centímetros.')

        length = input('\n\nDigite o valor do comprimento do retângulo e pressione ENTER.'
                       '\n> ')
        length = analyze_number(length, 'length')

        width = input('\n\nDigite o valor da largura do retângulo e pressione ENTER.'
                      '\n> ')
        width = analyze_number(width, 'width')

        return Rectangle(Rectangle.__analyze_shape(length, width), length, width)

    def __str__(self):
        return f'\n . {self.name}' \
               f'\n' \
               f'\n    . Área' \
               f'\n        {self.area():.2f} cm²' \
               f'\n' \
               f'\n    . Comprimento' \
               f'\n        {self.__length} cm' \
               f'\n' \
               f'\n    . Largura' \
               f'\n        {self.__width} cm'


class Triangle(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.__side = side  # 'side' IS A DICTIONARY THAT CONTAINS THE THREE SIDES (A, B, C) OF THE TRIANGLE.

    def area(self):
        s = self.__semiperimeter()

        return sqrt(s * (s - self.__side['A']) * (s - self.__side['B']) * (s - self.__side['C']))  # HERON'S FORMULA

    @staticmethod
    def __exists(side):  # THE TRIANGLE EXISTS, IF
        return side['A'] + side['B'] > side['C'] and \
               side['A'] + side['C'] > side['B'] and \
               side['B'] + side['C'] > side['A']

    @classmethod
    def load_input(cls):
        side = {'A': 0, 'B': 0, 'C': 0}

        print('\n\nVocê escolheu realizar o cálculo da área de um triângulo.'
              '\n\nOs valores de cada um de seus três lados devem ser informados em centímetros.')

        while True:
            for key in ['A', 'B', 'C']:
                value = input(f"\n\nDigite o valor do lado '{key}' do triângulo e pressione ENTER."
                              f"\n> ")
                value = analyze_number(value, 'value', key=key)

                side[key] = value

            if Triangle.__exists(side):
                return Triangle('Triângulo', side)
            else:
                clear_screen()

                print(f"\n\nA composição de lados 'A': {side['A']}, 'B': {side['B']} e 'C': {side['C']} não satisfaz a "
                      f"condição de existência de um triângulo."
                      f"\n\nA partir deste conjunto de medidas, não é possível realizar a construção desta figura."
                      f"\n"
                      f"\n\nA seguir, informe novamente – em centímetros – os valores de cada um dos três lados do "
                      f"triângulo."
                      f"\n\nLeve em consideração a condição que define sua existência, apresentada abaixo."
                      f"\n"
                      f"\n\nSejam A, B e C os três lados prováveis do triângulo T."
                      f"\n\n . T existirá se, e somente, se "
                      f"\n\n   . A + B > C"
                      f"\n\n   . A + C > B"
                      f"\n\n   . B + C > A")

    def __semiperimeter(self):
        return .5 * (self.__side['A'] + self.__side['B'] + self.__side['C'])

    def __str__(self):
        return f'\n . {self.name}' \
               f'\n' \
               f'\n   . Área' \
               f'\n       {self.area():.2f} cm²' \
               f'\n' \
               f'\n   . Lados' \
               f"\n       A. {self.__side['A']} cm" \
               f"\n" \
               f"\n       B. {self.__side['B']} cm" \
               f"\n" \
               f"\n       C. {self.__side['C']} cm" \
               f'\n' \
               f'\n   . Tipo' \
               f'\n       {self.__type()}'

    def __type(self):
        if self.__side['A'] == self.__side['B']:
            if self.__side['A'] == self.__side['C']:
                return 'Equilátero'
            else:
                return 'Isósceles'
        else:
            if self.__side['A'] == self.__side['C']:
                return 'Isósceles'
            else:
                if self.__side['B'] == self.__side['C']:
                    return 'Isósceles'
                else:
                    return 'Escaleno'


def calculate_area(geometric_shape):
    if geometric_shape == CIRCLE():
        geometric_shape = Circle.load_input()
    else:
        if geometric_shape == RECTANGLE():
            geometric_shape = Rectangle.load_input()
        else:
            if geometric_shape == TRIANGLE():
                geometric_shape = Triangle.load_input()

    clear_screen()

    print(geometric_shape)
