import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    matches = re.finditer(pattern, text)

    for match in matches:
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    total = 0
    
    for number in func(text):
        total += number

    return total