import time

A = [3, 5, 9, 12]
target = 17
n = len(A)

total_subset = 0
start = time.time()

print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()
print("Subset yang memenuhi target:")

for i in range(2**n):
    subset = []
    total = 0
    
    for j in range(n):
        if i & (1 << j):
            subset.append(A[j])
            total += A[j]
    
    total_subset += 1
    
    if total == target:
        print(subset)

end = time.time()

print("Total subset diperiksa:", total_subset)
print("Runtime:", (end - start) * 1000, "ms")
