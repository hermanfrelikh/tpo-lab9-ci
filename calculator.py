class Calculator:
    """Калькулятор с простой бизнес-логикой — объект модульного тестирования"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def is_prime_number(self, n):
        # простое число — натуральное больше 1, которое делится только на 1 и на себя
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("Ожидается целое число")
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def average(self, numbers):
        if not numbers:
            raise ValueError("Список пуст")
        return sum(numbers) / len(numbers)
