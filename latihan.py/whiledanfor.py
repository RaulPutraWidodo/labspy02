import random

n = int(input("Masukkan nilai n: "))
count = 0

while count < n:
    rand_num = random.random()  # Membangkitkan bilangan acak antara 0 dan 1
    if rand_num < 0.5:
        print(rand_num)
        count += 1
