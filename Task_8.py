"""
 Дано дійсне A та ціле число N (> 0). Вивести 1 – A + A2 – A3 + ... + (–1)^N*AN.
 Скорий Євген 141
"""

A=float(input("Введіть дійсне A = "))
N=int(input("Введіть ціле N = "))

a = 1
result = 1

if N > 0:
    for i in range(N):
        a *= -A
        result += a
    print("Відповідь: ", result)
else:
    print("Помилка: Введіть N > 0")