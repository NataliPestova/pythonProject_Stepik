X = float(input())
Y = float(input())
Operat = input()

if Operat == '+':
    print(X+Y)
elif Operat == '-':
    print(X-Y)
elif Operat == '/':
    if Y == 0:
        print('Деление на 0!')
    else:
        print(X/Y)
elif Operat == '*':
    print(X*Y)
elif Operat == 'mod':
    if Y == 0:
        print('Деление на 0!')
    else:
        print(X % Y)
elif Operat == 'div':
    if Y == 0:
        print('Деление на 0!')
    else:
        print(X // Y)
elif Operat == 'pow':
    print(X**Y)
