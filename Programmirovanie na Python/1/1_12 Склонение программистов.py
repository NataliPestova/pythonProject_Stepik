Count_programmist = int(input())
dop = ''
number = Count_programmist % 100
print(number)
if number >= 11 and number <= 19:
    dop = 'ов'
else:
    i = number % 10
    if i == 1:
        dop = ''
    elif i == 2:
        dop = 'а'
    elif i == 3:
        dop = 'а'
    elif i == 4:
        dop = 'а'
    else:
        dop = 'ов'
print(str(Count_programmist) + ' программист' + dop)