import numpy as np

#List python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#Array Numpy

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

#ELEMENTWISE operation
#penjumlahan
hasil = a+b
hasil2 = anp + bnp

print(hasil)
print(hasil2)

#pengurangan (list tidak bisa dikurangi dengan list)
hasil = anp-bnp
print(hasil)

#perkalian (list tidak bisa dikali dengan list)
hasil = anp*bnp
print(hasil)

#pembagian (list tidak bisa dibagi dengan list))
hasil=anp/bnp
print(hasil)

#kuadrat
hasil =anp**2
print(hasil)

#multidimensi array numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil = c + d
hasil2 = c*d
print(hasil)
print(hasil2)

#Secara basic, semua operasi aritmatika di nympy adalah elementwise