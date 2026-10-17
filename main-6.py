def fibonaci(n):
    if n <= 1:
        return n

    return fibonaci(n-1) + fibonaci(n-2)

# print(fibonaci(6))
# 11235

def fibonaci_rec_memo(n, memo):
    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    return fibonaci_rec_memo(n-1, memo) + fibonaci_rec_memo(n-2, memo)


def start_fibonaci(n):
    dp = [-1] * (n+1)
    return fibonaci_rec_memo(n, dp)

# print(start_fibonaci(6))

def fibonaci_iter_memo(n) -> None:
    dp =[0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# print(fibonaci_iter_memo(1000))        

def factorial_rec(n):
    if n < 1:
        return 1
    return n * factorial_rec(n-1)

# print(factorial_rec(996))

def factorial_iter_memo(n):
    dp = [1] * (n+1)

    for i in range(2, n+1):
        dp[i] = i * dp[i-1]
        dp[i-2] = 1

    return dp[n]

# Ти піднімаєшся по сходах. За один крок можеш піднятись на 1 або 2 сходинки. Скільки різних способів дістатись до сходинки n?
# Кількість способів дістатись до сходинки n = способи до n-1 + способи до n-2

def n_steps(n):
    dp = [1] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[i]

# print(n_steps(6))

# Дано масив чисел (є від'ємні). Знайди підмасив із найбільшою сумою
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# На кожному кроці питай себе — чи вигідно продовжувати попередній підмасив, чи ㅤㅤㅤкраще почати новий з цього елемента?


def max_subarray(arr):
    current = arr[0]
    best = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        best = max(best, current)

    return best

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_subarray(arr))

# Жабка сидить на березі (позиція 0) і хоче дістатися до купини n.
# За один стрибок вона може подолати 1, 2 або 3 купини.
# Скількома різними способами жабка може дістатися до купини n?
# Підказка: способи(n) = способи(n-1) + способи(n-2) + способи(n-3)

def n_steps(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[i]

def ways(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[i]

# print(ways(6))


# ЗАВДАННЯ 4: Мінімальна вартість підйому сходами (Min Cost Climbing Stairs)
# Кожна сходинка має свою ціну cost[i]. Оплативши вартість сходинки, ти можеш ступити на 1 або 2 сходинки вперед.
# Починати можна зі сходинки 0 або зі сходинки 1.
# Знайди мінімальну вартість, щоб дістатися самої вершини (за межі масиву).
# Підказка: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

def min_cost(cost: list):
    n = len(cost)
    dp = [0] * (n+1)

    for i in range(2, n+1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    return dp[n]

cost1 = [10, 15, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# print(min_cost(cost2))

# ЗАВДАННЯ 5: Пограбування будинків (House Robber)
# Грабіжник планує пограбувати будинки на вулиці. У кожному будинку лежить сума nums[i].
# Якщо пограбувати два сусідні будинки, спрацює сигналізація.
# Яку максимальну суму можна викрасти, не грабуючи сусідні будинки?
# Підказка: Для кожного будинку обираємо: або пропускаємо його (dp[i-1]), або грабуємо (dp[i-2] + nums[i]).

def house(nums: list):
    if not nums:
        return 0
    if len(nums) == [1]:
        return  nums[0]
    # if nums == [] or nums is  None:
    #     return 0
    n = len(nums)
    dp = [0] * (n+1)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    

    for i in range(2, n):
        dp[i] = max(dp[i-1],  dp[i-2] + nums[i])

    return dp[n-1]

houses = [2, 7, 9, 3, 1]
print(house(houses))

# ЗАВДАННЯ 6: Розмін монет — мінімальна кількість монет (Coin Change)
# Маємо монети різних номіналів coins та цільову суму amount.
# Знайди найменшу кількість монет, яка потрібна для розміну цієї суми. Якщо розміняти неможливо — поверни -1.
# Підказка: dp[i] = min(dp[i - coin] + 1) для всіх coin <= i

def min_coin_change(coins: list, amount):
    n = len(coins)
    dp = [float("inf")] * (n+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if coin < i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1
        

coins = [1, 2, 5]
print("Мінімум монет для суми 11:", min_coin_change(coins, 11))
print("Мінімум монет для суми 3 монет [2]:", min_coin_change([2], 4))