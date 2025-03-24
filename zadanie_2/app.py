import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def calculate_area(shape: str, dimensions: tuple) -> float:
    if shape == "circle" and len(dimensions) == 1:
        return 3.14159 * dimensions[0] ** 2
    elif shape == "rectangle" and len(dimensions) == 2:
        return dimensions[0] * dimensions[1]
    elif shape == "triangle" and len(dimensions) == 2:
        return 0.5 * dimensions[0] * dimensions[1]
    return -1  # Invalid input

def sort_numbers(numbers: list) -> list:
    return sorted(numbers)

def convert_date_format(date: str) -> str:
    day, month, year = date.split("-")
    return f"{year}-{month}-{day}"

def is_palindrome(text: str) -> bool:
    clean_text = ''.join(filter(str.isalnum, text)).lower()
    return clean_text == clean_text[::-1]