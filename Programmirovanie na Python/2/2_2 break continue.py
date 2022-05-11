a = int(input())
while    a <= 100:
    if a < 10:
        a = int(input())
        continue
    elif a > 100:
        break
    else:
        print(a)
        a = int(input())
