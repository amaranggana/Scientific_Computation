import numpy as np

#membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,6,7])

#membuat vector dengan range
c = np.arange(1,10,2)

#membuat linspace
#fungsi dari NumPy yang digunakan untuk membuat array dengan nilai-nilai yang terdistribusi secara merata (linier) dalam rentang tertentu.
d = np.linspace(1,10,4)

#array multi dimensi atau matrix
e = np.array([(1,2,3,),(5,6,7)])

# matrix dengan nilai 0
f = np.zeros((5,5))

#matrix dengan nilai 1
g = np.ones(5)

#matrix identitas
h1 = np.identity(5)
h2 = np.eye(5)

#display
print(a,"\n")
print(b,"\n")
print(c,"\n")
print(d,"\n")
print(e,"\n")
print(f,"\n")
print(g,"\n")
print(h1,"\n")
print(h2,"\n")