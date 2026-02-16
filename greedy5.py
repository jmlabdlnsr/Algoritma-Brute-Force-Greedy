print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()

jobs = [
    ("J1", 100, 2),
    ("J2", 19, 1),
    ("J3", 27, 2),
    ("J4", 25, 1),
    ("J5", 15, 3)
]

jobs.sort(key=lambda x: x[1], reverse=True)

max_deadline = max(job[2] for job in jobs)
slots = [None] * max_deadline
total_profit = 0

for job in jobs:
    name, profit, deadline = job
    for t in range(deadline - 1, -1, -1):
        if slots[t] is None:
            slots[t] = name
            total_profit += profit
            break

print("Jadwal:")
for i in range(len(slots)):
    print(f"Slot {i+1}: {slots[i]}")

print("Total Profit:", total_profit)