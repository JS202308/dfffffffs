
import math
import random
import time


# ЗАВДАННЯ 1. Власна хеш-таблиця


class MyHashTable:
    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("Розмір таблиці має бути додатним")

        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        if self.table[index]:
            self.collisions += 1

        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)

        for k, value in self.table[index]:
            if k == key:
                return value

        return None

    def delete(self, key):
        index = self._hash(key)

        for i, (k, value) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return value

        return None

    def __str__(self):
        return str(self.table)


print("ЗАВДАННЯ 1")
data = [10, 20, 30, 40, 50]

for size in [5, 10, 20]:
    table = MyHashTable(size)

    for key in data:
        table.insert(key, f"Значення {key}")

    print(
        f"Розмір: {size}, "
        f"колізій: {table.collisions}, "
        f"пошук 20: {table.search(20)}"
    )

print("Видалено:", table.delete(20))
print("Після видалення:", table.search(20))



# ЗАВДАННЯ 5. 

def mod_hash(k, m):
    if m <= 0:
        raise ValueError("m має бути додатним")

    return k % m


def count_collisions(hash_values):
    return len(hash_values) - len(set(hash_values))


print("\nЗАВДАННЯ 5")
keys = list(range(1, 101))

for m in [5, 10, 20, 50, 100]:
    values = [mod_hash(k, m) for k in keys]
    collisions = count_collisions(values)

    print(
        f"m = {m:3}, "
        f"унікальних хешів = {len(set(values)):3}, "
        f"колізій = {collisions:3}"
    )



# ЗАВДАННЯ 6. Мультиплікативне хешування


def multiplicative_hash(k, m, A=0.6180339887):
    if m <= 0:
        raise ValueError("m має бути додатним")

    if not 0 < A < 1:
        raise ValueError("A має бути між 0 та 1")

    return math.floor(m * ((k * A) % 1))


print("\nЗАВДАННЯ 6")
m = 10
constants = [0.5, 0.6180339887, 0.75, 0.9]

for A in constants:
    values = [
        multiplicative_hash(k, m, A)
        for k in keys
    ]

    counts = [values.count(i) for i in range(m)]

    print(
        f"A = {A:.4f}, "
        f"колізій = {count_collisions(values)}, "
        f"мінімум у комірці = {min(counts)}, "
        f"максимум у комірці = {max(counts)}"
    )


# ЗАВДАННЯ 7. Лінійне зондування

class LinearProbingHashTable:
    DELETED = object()

    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("Розмір таблиці має бути додатним")

        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        for i in range(self.size):
            pos = (index + i) % self.size
            item = self.table[pos]

            if item is None or item is self.DELETED:
                self.table[pos] = (key, value)
                return True

            if item[0] == key:
                self.table[pos] = (key, value)
                return True

        return False

    def search(self, key):
        index = self._hash(key)

        for i in range(self.size):
            pos = (index + i) % self.size
            item = self.table[pos]

            if item is None:
                return None

            if item is self.DELETED:
                continue

            if item[0] == key:
                return item[1]

        return None

    def delete(self, key):
        index = self._hash(key)

        for i in range(self.size):
            pos = (index + i) % self.size
            item = self.table[pos]

            if item is None:
                return None

            if item is self.DELETED:
                continue

            if item[0] == key:
                self.table[pos] = self.DELETED
                return item[1]

        return None


print("\nЗАВДАННЯ 7")

chaining = MyHashTable(20)
linear = LinearProbingHashTable(20)

test_keys = [10, 30, 50, 70, 90]

for key in test_keys:
    chaining.insert(key, str(key))
    linear.insert(key, str(key))

print("Chaining: пошук 50 =", chaining.search(50))
print("Linear probing: пошук 50 =", linear.search(50))

print("Chaining: видалення 50 =", chaining.delete(50))
print("Linear probing: видалення 50 =", linear.delete(50))


random.seed(42)
n = 5000
benchmark_keys = random.sample(range(1, 10**9), n)
table_size = 10007

chain_table = MyHashTable(table_size)
linear_table = LinearProbingHashTable(table_size)

start = time.perf_counter()
for key in benchmark_keys:
    chain_table.insert(key, key * 2)
chain_insert_time = time.perf_counter() - start

start = time.perf_counter()
for key in benchmark_keys:
    linear_table.insert(key, key * 2)
linear_insert_time = time.perf_counter() - start

start = time.perf_counter()
for key in benchmark_keys:
    chain_table.search(key)
chain_search_time = time.perf_counter() - start

start = time.perf_counter()
for key in benchmark_keys:
    linear_table.search(key)
linear_search_time = time.perf_counter() - start

print("\nПорівняння продуктивності:")
print(f"Chaining — вставка: {chain_insert_time:.6f} с")
print(f"Linear probing — вставка: {linear_insert_time:.6f} с")
print(f"Chaining — пошук: {chain_search_time:.6f} с")
print(f"Linear probing — пошук: {linear_search_time:.6f} с")
