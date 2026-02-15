print("Nama : Jamal Abdul Nasir")
print("NPM  : 247006111015")
print("Kelas: A")
print()

coins = [25, 10, 5, 1]
target = 68

remaining = target
total_coins = 0
used_coins = []

print("Target =", target)
print("Koin tersedia =", coins)
print()

for coin in coins:
    while remaining >= coin:
        remaining -= coin
        total_coins += 1
        used_coins.append(coin)
        print("ambil", coin, "sisa", remaining)

print()
print("Koin yang digunakan =", used_coins)
print("Total Koin =", total_coins)
