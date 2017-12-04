import numpy as np

a = np.zeros(shape=(50,50))

for i in range(49):
    a[i][i+1] = 1 - 0.02*(i+1)

a[49][0] =1

a = np.asmatrix(a)

I = np.zeros(shape = (50,50))

for i in range(50):
    I[i][i] = 1

I = np.asmatrix(I)

E = np.ones(shape = (50,1))

E = np.asmatrix(E)

b = I - a

c = b.getI()*E

c[0]
