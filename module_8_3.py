# Домашнее задание по теме "Создание исключений"
# Класс исключений IncorrectVinNumber
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

# Класс исключений IncorrectCarNumbers
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

# Класс Car
class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__check = False
        self.__is_valid_vin(vin_number)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int): # Выбрасывает исключение с сообщением, если передано не целое число
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if not (1000000 <= vin_number <= 9999999): # Выбрасывает исключение с сообщением, если переданное число находится не в диапазоне
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        self.__vin = vin_number
        self.__check = True # если исключения не были выброшены
        return self.__check

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str): # Выбрасывает исключение с сообщением, если передана не строка
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6: # Выбрасывает исключение с сообщением, если переданная строка не ровно из 6 символов
            raise IncorrectCarNumbers("Неверная длина номера")
        self.__numbers = numbers
        self.__check = True # если исключения не были выброшены
        return self.__check

# Пример выполняемого кода
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')