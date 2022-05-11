"""
9. Дано ціле число N (> 0). Знайти число, отримане при прочитанні числа N справа наліво та добуток
його цифр.
Скорий Євген 141
"""

def multiplication(n):
    mult = 1
    while n > 0:
        digit = n % 10
        mult = mult * digit
        n = n // 10
    print("Добуток цифр числа = ", mult)

def reverse(n):
    numb = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        numb = numb * 10
        numb = numb + digit
    print("Обернете число = ", numb)


n = int(input("Введіть число N(N > 0): "))

if n > 0:
    multiplication(n)
    reverse(n)
else:
    print("Помилка: число повинно бути більше нуля")