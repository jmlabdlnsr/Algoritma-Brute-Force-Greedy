text = "ALGORITMASTRATEGIALGORITMA"
pattern = "RIT"

leng_text = len(text)
leng_pattern = len(pattern)
count = 0

print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()
print("Panjang Teks:", leng_text)
print("Panjang Pattern:", leng_pattern)
print("Kemungkinan Posisi:", leng_text - leng_pattern + 1)
print()

for i in range(leng_text - leng_pattern + 1):
    j = 0
    while j < leng_pattern and text[i + j] == pattern[j]:
        count += 1
        j += 1

    if j == leng_pattern:
        print("Pattern ditemukan pada indeks ke", i)

    count += (j < leng_pattern)
print("Jumlah perbandingan karakter:", count)