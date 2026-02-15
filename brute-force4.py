print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()

alphabet = ['a', 'b', 'c', '1', '2']
target = "b1a"
L = 3

count = 0
found = False

for c1 in alphabet:
    for c2 in alphabet:
        for c3 in alphabet:
            password = c1 + c2 + c3
            count += 1

            if password == target:
                print("Password ditemukan:", password)
                print("Percobaan ke:", count)
                found = True
                break
        if found:
            break
    if found:
        break

print("Total kombinasi diperiksa:", count)
print("Total kemungkinan:", len(alphabet) ** L)
