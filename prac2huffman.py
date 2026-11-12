
import heapq

text = input("Enter a string: ")

# Count frequency
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# Create min heap
heap = [[f, ch] for ch, f in freq.items()]
heapq.heapify(heap)

# Build Huffman tree
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    heapq.heappush(heap, [a[0] + b[0], [a[1], b[1]]])

# Generate codes
codes = {}

def generate(node, code=""):
    if isinstance(node, str):
        codes[node] = code
    else:
        generate(node[0], code + "0")
        generate(node[1], code + "1")

generate(heap[0][1])

# Display codes
print("Huffman Codes:")
for ch in codes:
    print(ch, ":", codes[ch])

#time complexity is O(nlogn)
