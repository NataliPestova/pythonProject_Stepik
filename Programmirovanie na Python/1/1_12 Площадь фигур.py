Type = input()

if Type == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif Type == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
elif Type == 'круг':
    r = int(input())
    S = 3.14 * (r**2)
else:
    S = 0

print(S)