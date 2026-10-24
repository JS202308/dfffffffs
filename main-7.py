import math
# password = "Пароль"
# numeric_pass = ""
# for char in password:
#     numeric_pass += str(ord(char))

# print(int(numeric_pass) % 1000)

# class Hash:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def _hash(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         idx = self._hash(key)
#         self.table[idx].append((key, value))

#     def search(self, key):
#         idx = self._hash(key)
#         for item in self.table[idx]:
#             if item[0] == key:
#                 return item[1]

#     def delete(self, key):
#         idx = self._hash(key)
#         for i in range(len(self.table[idx])):
#             if self.table[idx][i][0] == key:
#                 value = self.table[idx][i][1]
#                 del self.table[idx][i]
#                 return value

#     def __str__(self):
#         return str(self.table)

# table = Hash(size=10)
# table.insert("Ананас" ,20)
# table.insert("БАнан" ,18)
# table.insert("Цукор" ,100)
# table.insert("яблуко" ,43)
# table.insert("Хліб" ,150)

# print(table)

# Умова: Напишіть функцію, яка приймає рядок і повертає словник, де ключами є символи, а значеннями — кількість їх входжень у рядок.
# Приклад: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# def count_chars(s):
#     result = {}
#     for char in s:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1
#     return result

# print(count_chars("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Умова: Знайдіть перший символ у рядку, який зустрічається лише один раз. Якщо такого немає — поверніть None.
# Приклад: "swiss" -> 'w'

# def look_for_let(s):
#     result = {}
#     for char in s:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1
#     return result

# print(look_for_let("swiss"))

# Реалізуйте клас HashTable з мультиплікативним хешуванням та методами для роботи з таблицею.
A = 0.6180339887
# Підказка:
# h(k) = math.floor(m × (k × A mod 1))

class Hash:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return math.floor(self.size * (hash(key) * A % 1))

    def insert(self, key, value):
        idx = self._hash(key)
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self._hash(key)
        for item in self.table[idx]:
            if item[0] == key:
                return item[1]

    def delete(self, key):
        idx = self._hash(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                value = self.table[idx][i][1]
                del self.table[idx][i]
                return value

    def __str__(self):
        return str(self.table)


size = 10
key = "Hello word!"
h_key = abs(hash(key)) % 2**32
normalize_key = h_key / 2**32
# print(normalize_key * A)

h = math.floor(size*((normalize_key * A) % 1))
# print(h)

# Лінійне зондування
def linear_probe(hash_table, key, m):
    index = key % m
    for i in range(m):
        pos = (index + i) % m
        if hash_table[pos] is None:
            return pos
    return None

# Квадратичне зондування
def quadratic_probe(hash_table, key, m, c1=1, c2=3):
    index = key % m
    for i in range(m):
        pos = (index + c1 * i + c2 * i * i) % m
        if hash_table[pos] is None:
            return pos
    return None

# Подвійне гешування
def double_hashing(hash_table, key, m):
    h1 = key % m
    h2 = 1 + (key % (m - 1))
    for i in range(m):
        pos = (h1 + i * h2) % m
        if hash_table[pos] is None:
            return pos
    return None

# Реалізуйте функцію mod_hash_list(keys, m),
# яка приймає список чисел та параметр m (розмір геш‑таблиці).
# Обчисліть хеш‑значення для кожного ключа за формулою: h(k) = k mod m
# Проведіть тестування для заданого списку ключів.

def mod_hash_list(keys, m):
    hash_keys = []
    for key in keys:
        hash_keys.append(key % m)
    return hash_keys
    

keys = [123, 456, 789, 101112, 131415, 161718]
m = 10
# print("Модульне гешування (m=10):", mod_hash_list(keys, m))

# Дано функцію analyze_mod_hash. Доповніть її так,
# щоб вона виводила всі ключі що колізують (мають однакове хеш-значення).


def analyze_mod_hash(keys, m):
    # Ваше завдання: знайдіть та виведіть колізії
    # Підказка: використайте словник де ключ — хеш, значення — список ключів
    collisions = {}
    for key in keys:
        h = key % m
        if h not in collisions:
            collisions[h] = []

        collisions[h].append(key)

    for h, bucket in collisions.items():
        if len(bucket) > 1:
            print(f"h={h}: {bucket}")

keys = list(range(1, 30))  # невеликий список щоб зручно читати
m = 7
analyze_mod_hash(keys, m)

def insert_linear(table: list, key: int, m: int) -> int:
    index = key % m
    for i in range(m):
        pos = (index + i) % m
        if table[pos] is None or table[pos] == "DELETED":
            table[pos] = key
            return pos
    return -1

# Тест:
# table1 = [None] * 5
# insert_linear(table1, 10, 5)  # 10 % 5 = 0 -> індекс 0
# insert_linear(table1, 15, 5)  # колізія в 0 -> йде у слот 1
# print("Задача 1. Таблиця після вставки:", table1)  # [10, 15, None, None, None]

# Умова: Напишіть функцію get_quadratic_probe_sequence(key, m, c1, c2, steps),
# яка повертає список із перших steps індексів за формулою:
# pos = (key % m + c1 * i + c2 * i^2) % m

def get_quadratic_probe_sequence(key, m, c1, c2, steps):
    sequence = []
    for i in range( steps):
        pos = (key % m + c1 * i + c2 * i^2) % m
        sequence.append(pos)

    return sequence


# print("Задача 4. Послідовність індексів:", get_quadratic_probe_sequence(key=7, m=11, c1=1, c2=3, steps=4))
# i=0: 7; i=1: (7+1+3)%11=0; i=2: (7+2+12)%11=10; i=3: (7+3+27)%11=4 -> [7, 0, 10, 4]

# Умова: Реалізуйте insert_double_hashing(table, key, m).
# h1(k) = k % m
# h2(k) = 1 + (key % (m - 1))
# pos = (h1 + i * h2) % m


def insert_double_hashing(table: list, key: int, m: int):
    h1 = key % m
    h2 = 1 + (key % (m - 1))

    for i in range(m):
        pos = (h1 + i * h2) % m
        if table[pos] is None:
            table[pos] = key
            return pos 
    return None


# Тест:
t7 = [None] * 7
insert_double_hashing(t7, 7, 7)   # h1 = 0, h2 = 1 + (7%6) = 2 -> слот 0
insert_double_hashing(t7, 14, 7)  # h1 = 0 (колізія), h2 = 1 + (14%6) = 3 -> i=1: (0 + 3) % 7 = 3
print("Задача 7. Таблиця (подвійне гешування):", t7)  # [7, None, None, 14, None, None, None]