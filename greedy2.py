print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()

aktivitas = [
    ("A1", 1, 4),
    ("A2", 3, 5),
    ("A3", 0, 6),
    ("A4", 5, 7),
    ("A5", 8, 9)
]

selected = []
last_finish = 0

for name, start, finish in aktivitas:
    if start >= last_finish:
        selected.append((name, start, finish))
        last_finish = finish

print("Aktivitas terpilih:")
for act in selected:
    print(act)

print("Total aktivitas terpilih =", len(selected))
