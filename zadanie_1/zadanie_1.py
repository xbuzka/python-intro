names = ["Ala", "Bartek", "Celina"]
age = [23, 30, 19]

print("Lista par (imię, wiek):")
for para in zip(names, age):
    print(para)

print()

print("Lista z numeracją:")
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

print()

try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Błąd: próba dzielenia przez zero!")

print()

try:
    liczba = int("tekst")
except ValueError:
    print("Błąd: nie można zamienić tekstu na liczbę!")