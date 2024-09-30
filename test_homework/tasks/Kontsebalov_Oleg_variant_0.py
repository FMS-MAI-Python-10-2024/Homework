def Wow(a : int, b : int) -> None:
    sum = a + b

    if sum <= 10:
        print("Пикай Хорька!")
    elif 10 < sum <= 100:
        print("Каждый дуб когда был жёлудём...")
    elif 100 < sum <= 1000:
        print("One shot - one kill.")
    else:
        print("Хафизов нехороший человек.")


a, b = map(int, input().split())
Wow(a, b)