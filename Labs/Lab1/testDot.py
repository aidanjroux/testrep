import numpy as np
import numpy.linalg as la
import math
def driver():
    n = 2
    x = np.linspace(0,np.pi,n)
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 6*x**3 + 2*np.sin(x)
    y = f(x)
    w = g(x)
    y = np.array([1,0])
    w = np.array([0,1])
    matrix = np.array([[1, 2], [3, 4]])
    # evaluate the dot product of y and w
    dp = dotProduct(y,w,n)
    # print the output
    print('the dot product is : ', dp)
    #mult = matrixVectorMult(y,matrix,n)
    mult = np.dot(matrix,y)
    print('the vector is : ', mult)
    return

    
def dotProduct(x,y,n):
# Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp

def matrixVectorMult(x,matrix,n):
# Computes the dot product vector and matrix
    vector = np.array([0,0])
    for j in range(n):
        vector = np.array([dotProduct(x,matrix[0,:],n),dotProduct(x,matrix[1,:],n)])
    return vector



driver()