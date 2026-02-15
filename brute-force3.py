import itertools

kota = ['A', 'B', 'C', 'D']

jarak = {
    ('A','B'):10, ('A','C'):15, ('A','D'):20,
    ('B','A'):10, ('B','C'):35, ('B','D'):25,
    ('C','A'):15, ('C','B'):35, ('C','D'):30,
    ('D','A'):20, ('D','B'):25, ('D','C'):30
}

start = 'A'
kota_lain = ['B', 'C', 'D']

min_jarak = float('inf')
rute_terpendek = None
jumlah_rute = 0

for perm in itertools.permutations(kota_lain):
    total = 0
    sekarang = start

    for k in perm:
        total += jarak[(sekarang, k)]
        sekarang = k

    total += jarak[(sekarang, start)]
    jumlah_rute += 1

    if total < min_jarak:
        min_jarak = total
        rute_terpendek = (start,) + perm + (start,)

print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()
print("Jumlah rute diperiksa:", jumlah_rute)
print("Rute terpendek:", " -> ".join(rute_terpendek))
print("Total jarak minimum:", min_jarak)
