from collections import defaultdict

def caching_fibonacci():
    cache = defaultdict(int)

    def fibonacci(n):
        if n < 0:
            return 0
        elif n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]
    
    return fibonacci
fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610


# 2 завдання
 
import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'  
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total = sum(numbers_generator)
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


