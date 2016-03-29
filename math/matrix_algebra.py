# Matrix Algebra

import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1., -1.],[0, 1.]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5]).reshape([4, 1])

# --  1. Matrix dimensions --
for n, i in enumerate([A, B, C, D, u, w]):
    print '1.{})'.format(n)
    print '\t', i.shape

# --  2. Vector operations --
print
print '2.1)',  u + v
print '2.2)', u - v
print '2.3)', 6*u
print '2.4)', np.dot(u, v)
print '2.5)', np.linalg.norm(u)

# -- 3. Matrix operations ==
print '3.1)\n', 'ValueError' # A + C    # ValueError
print '3.2)\n', A - C.T
print '3.3)\n', C.T + 3 * D
print '3.4)\n', B * A
print '3.5)\n', 'ValueError' # B * A.T  #ValueError
print '3.6)\n', 'ValueError' # B * C  #ValueError
print '3.7)\n', C * B
print '3.8)\n', np.linalg.matrix_power(B, 4)
print '3.9)\n', A * A.T
print '3.10)\n', D.T * D

