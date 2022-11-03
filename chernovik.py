from math import sqrt


message = 'Добро пожаловать в самую лучшую программу для вычисления '\
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(number: int):
    """ Вычисляет квадратный корень."""
    return sqrt(number)



def calc(your_number: int):
    """Если число меньше или равно 0."""
    if your_number <= 0:
        return 
    
     

result = CalculateSquareRoot(your_number)
print('Мы вычислили квадратный корень из '
      'введённого вами числа. Это будет: '
      '{result}')


print(message)
calc (25.5)