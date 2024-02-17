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


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Invalid command or contact name."
        except IndexError:
            return "Invalid number of arguments."

    return inner

contacts = {}

# Завдання 4

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def remove_contact(args, contacts):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact removed."
    else:
        return "Contact not found."

def list_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    while True:
        command = input("Enter a command: ").strip().lower().split()
        
        if not command:
            continue
        
        if command[0] == "add":
            if len(command) == 3:
                print(add_contact(command[1:], contacts))
            else:
                print("Enter the argument for the command")
        elif command[0] == "phone":
            if len(command) == 2:
                print(get_contact(command[1:], contacts))
            else:
                print("Enter the argument for the command")
        elif command[0] == "remove":
            if len(command) == 2:
                print(remove_contact(command[1:], contacts))
            else:
                print("Enter the argument for the command")
        elif command[0] == "all":
            print(list_all_contacts(contacts))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
