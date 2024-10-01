a, b = map(int, input().split())
summ = a + b

if summ <= 10:
    print("Пикай Хорька!")
elif 10 < summ <= 100:
    print("Каждый дуб когда был жёлудём...")
elif 100 < summ <= 1000:
    print("One shot - one kill.")
else:
    print("Хафизов нехороший человек.")
