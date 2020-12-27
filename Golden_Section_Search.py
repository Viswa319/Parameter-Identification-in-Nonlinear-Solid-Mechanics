"""
Created on Sun Dec 27 15:15:05 2020

@author: Sai Viswanadha Sastry Upadhyayula

Golden section search algorithm for finding minimum of a 1-D function
"""
import numpy as np
def GoldenSectionSearch(k1,k2,function):
    """
    Golden section search algorithm for finding minimum of a 1-D function    

    Parameters
    ----------
    k1 : int
        lower bound.
    k2 : int
        upper bound.
    function : function
        function for which minimum is to be found.

    Returns
    -------
    float
        argument where f(x) has its minimum.
        
    Example
    --------
     f = lambda x: (x-2)**2
     x = GoldenSectionSearch(1, 5,function)
    	print(x)
     1.9999999330223426

    """
    phi = (1+np.sqrt(5))/2 # golden ratio
    tol = 10**(-7) # tolerance value
    n = np.log(tol/(k2-k1))/np.log(1/phi)
    k3 = k2 - ((k2-k1)/phi)
    k4 = k1 + ((k2-k1)/phi)
    f3 = function(k3)
    f4 = function(k4)
    i = 3
    while abs(k3-k4)>tol:
        if f4 > f3:
            # update
            k2 = k4
            k4 = k3
            f4 = f3
            # compute
            k3 = k2 - ((k2-k1)/phi)
            f3 = function(k3)
        else:
            #update
            k1 = k3
            k3 = k4
            f3 = f4
            #compute
            k4 = k1 + ((k2-k1)/phi)
            f4 = function(k4)
        i+=1
    print('{:^10}'.format('number of necessary iterations estimated: %d' %(np.ceil(n))))
    print('{:^10}'.format('number of necessary iterations obtained: %d' %(np.ceil(i))))
    return (k1+k2)/2
    
def function(x):
    f = (x-2)**2
    return f
x1 = 1
x2 = 5
xopt = GoldenSectionSearch(x1,x2,function)
print('{:^10}'.format('function is minimum at: %18.16f' %(xopt)))
print('{:^10}'.format('minimum value of function is: %18.16f' %(function(xopt))))