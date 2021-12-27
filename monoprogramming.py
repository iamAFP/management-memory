# KELOMPOK 7
# 5200411213 - Abdi Febryan P
# 5200411247 - Zaki Makhasin

import os

os.system("cls")

print("-"*30)
print("Monoprogramming")
print("-"*30)
print("\n")

ram = int(input("Kapasitas RAM (GB) \t\t : "))
so = int(input("Besar Penggunaan Sistem Operasi (GB) : "))
kp = int(input("Besar Kapasitas Program (GB) \t : "))

print("\n")

tp = ram - ( so + kp )

print("-"*30)
print("Hasil")
print("-"*30)

print("Besar RAM \t\t\t : " , ram , "GB")
print("Besar Penggunaan Sistem Operasi  : " , so ,"GB")
print("Besar Program Terpakai \t\t : " , kp ,"GB")
print("Besar Memori Tidak Terpakai \t : ", tp , "GB")

