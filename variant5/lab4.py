def can_reach_one(n):
    # Створюємо масив dp, де dp[i] = True якщо число i досяжне
    dp = [False] * (n + 1)
    dp[n] = True  # Починаємо з числа N

    for i in range(n, 0, -1):
        if dp[i]:
            # Хід 1: відняти 3
            if i - 3 >= 1:
                dp[i - 3] = True
            # Хід 2: поділити на 2 (тільки якщо парне)
            if i % 2 == 0:
                dp[i // 2] = True

    return dp[1]


# Зчитуємо число від користувача
n = int(input("Введіть число N: "))

if can_reach_one(n):
    print("YES")
else:
    print("NO")