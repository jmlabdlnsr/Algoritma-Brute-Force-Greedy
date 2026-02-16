print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()

import heapq

class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

symbols = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

heap = []
for s, f in symbols.items():
    heapq.heappush(heap, Node(f, s))

while len(heap) > 1:
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    heapq.heappush(heap, Node(n1.freq + n2.freq, None, n1, n2))

root = heap[0]
codes = {}

def generate(node, code=""):
    if node.symbol:
        codes[node.symbol] = code
        return
    generate(node.left, code + "0")
    generate(node.right, code + "1")

generate(root)

fixed_bits = 3
original_bits = sum(f * fixed_bits for f in symbols.values())
compressed_bits = sum(symbols[s] * len(codes[s]) for s in symbols)

print("Huffman Codes:")
for s in codes:
    print(s, symbols[s], codes[s], len(codes[s]))

print("Total bits (original):", original_bits)
print("Total bits (compressed):", compressed_bits)
print("Compression ratio:", compressed_bits / original_bits)
