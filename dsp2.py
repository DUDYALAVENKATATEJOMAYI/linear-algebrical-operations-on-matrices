import numpy as np
a=np.array(input("enter the matrix"))
b=np.array(input("enter the matrix"))
# add()is used to add matrices
print("addition of two matrices")
print(np.add(a,b))
# substract() is used to substract matrix
print("substraction of two matrices")
print(np.subtract(a,b))
# divide() is used to divide matrices
print("matrix division")
print(np.divide(a,b))
print("multiplication of two matrices")
print(np.multiply(a,b))
print("the product of two matrices")
print(np.dot(a,b))
print("square root is")
print(np.sqrt(a))
print("the summation of elements")
print(np.sum(b))
# using "T" to transpose the matrix
print("matrix transposition")
print(a.T)
print("determinant of the matrix")
print(np.linalg.det(a))
print("inverse of the matrix")
print(np.linalg.inv(a))
print("rank of the matrix")
print(np.linalg.matrix_rank(a))
print("power of the matrix")
print(np.linalg.matrix_power(a,3))
print("eigen values of the matrix")
print(np.linalg.eigvals(a))
print("trace of the matrix")
print(np.trace(a))


