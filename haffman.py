import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text) -> None:
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1

    heap = [HuffmanNode(char, freq_) for char, freq_ in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq. heappop(heap)
        right = heapq.heappop (heap)
        heapq.heappush(heap, HuffmanNode(freq=left.freq+right.freq, left=left, right=right))

    return heap[0] if heap else None

def build_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    build_codes(node.left, current_code + "0", codes)
    build_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)


def huffman_decode(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root
    return decoded_text

# if __name__ == "__main__":
#     text = "HI"
#     huffman_tree = build_huffman_tree(text)
#     codes = build_codes(huffman_tree)
#     print("Коди Хаффмана для символів:")
#     for char, code in codes.items():
#         print(f"'{char}': {code}")

#     encoded_text = huffman_encode(text, codes)
#     print("\nЗакодований текст:")
#     print(encoded_text)

#     decoded_text = huffman_decode(encoded_text, huffman_tree)
#     print("\nДекодований текст:")
#     print(decoded_text)

    # Умова: Закодуйте за допомогою наданого коду коротке слово "DATA". Виведіть на екран отриманий двійковий рядок.

# Умова: Для тексту "ABRACADABRA" побудуйте коди Хаффмана
# та виведіть у консоль довжину бітового коду (кількість символів 0 та 1) тільки для літери 'R'.

# if __name__ == "__main__":
#     text = "ABRACADABRA"

#     huffman_tree = build_huffman_tree(text)
#     codes = build_codes(huffman_tree)

#     print("Коди Хаффмана:")
#     for char, code in codes.items():
#         print(f"'{char}': {code}")

#     print("\nДовжина бітового коду для літери 'R':")
#     print(len(codes['R']))


# Умова: Закодуйте слово "HI", а потім за допомогою функції
# huffman_decode розкодуйте отриманий бітовий рядок назад у
# текст та виведіть його на екран, щоб переконатися у правильності.

# if __name__ == "__main__":
#     text = "HI"
#     huffman_tree = build_huffman_tree(text)
#     codes = build_codes(huffman_tree)
#     print("Коди Хаффмана:")
#     for char, code in codes.items():
#         print(f"'{char}': {code}")

#     encoded_text = huffman_encode(text, codes)
#     print("\nЗакодований текст:")
#     print(encoded_text)
#     decoded_text = huffman_decode(encoded_text, huffman_tree)

#     print("\nРозкодований текст:")
#     print(decoded_text)

#     print("\nПеревірка:")
#     print(text == decoded_text)

# Умова: Візьміть рядок "BANANA". Порахуйте, скільки біт він
# займає у звичайному форматі (якщо кожен символ кодується
# стандартними 8 бітами) і скільки біт він займає після кодування Хаффмана. Виведіть обидва значення.

if __name__ == "__main__":
    text = "BANANA"
    normal_bits = len(text) * 8
    huffman_tree = build_huffman_tree(text)
    codes = build_codes(huffman_tree)
    encoded_text = huffman_encode(text, codes)
    huffman_bits = len(encoded_text)
    saving = ((normal_bits - huffman_bits) / normal_bits) * 100
    print("Звичайне кодування:")
    print(normal_bits, "біт")

    print("\nКодування Хаффмана:")
    print(huffman_bits, "біт")

    print("\nЕкономія:")
    print(round(saving, 2), "%")

import gzip

text = "# Умова: Закодуйте за допомогою наданого коду коротке слово # DATA.|
Виведіть на екран отриманий двійковий рядок."

encoded_text = text.encode("utf-8")
compressed_text = gzip.compress(encoded_text)

len_text = len(encoded_text)
len_comp_text = len(compressed_text)
result = len_comp_text * 100 // len_text
print(f"Початкова довзина {len_text} бiт, \nnісля стискання стало {len_comp_text}")