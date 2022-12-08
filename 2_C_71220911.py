a = input ("Masukkan angka : ")
b = input ("Masukkan angka yg dihitung : ")

count = 0

for c in a:
    if c==b:
        count += 1
print(f'Angka {b} muncul sebanyak {count} kali')

