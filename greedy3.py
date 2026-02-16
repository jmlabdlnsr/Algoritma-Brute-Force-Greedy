print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()

items = [
    ("I1", 10, 60),
    ("I2", 20, 100),
    ("I3", 30, 120)
]

capacity = 50

items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)

remaining = capacity
total_value = 0

print("Proses pengambilan item:")

for name, weight, value in items:
    if weight <= remaining:
        remaining -= weight
        total_value += value
        print(f"→ ambil {name} penuh")
    else:
        fraction = remaining / weight
        total_value += value * fraction
        print(f"→ ambil {fraction:.2f} bagian dari {name}")
        remaining = 0
        break

print("\nTotal nilai maksimum =", total_value)
