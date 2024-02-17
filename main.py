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
    pattern = r'\b\d+(?:\.\d+)?(?:e[+-]?\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total = sum(numbers_generator)
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


#завдання 4

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please provide valid input."
        except ValueError:
            return "Invalid input format. Please try again."
        except IndexError:
            return "Index out of range. Please try again."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def search_contact(name, contacts):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"{name} not found in contacts."

@input_error
def display_all_contacts(contacts):
    if contacts:
        return "\n".join([f"{name}: {contacts[name]}" for name in contacts])
    else:
        return "No contacts available."
