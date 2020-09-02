import numpy as np
import math as mt

def func(x)
	return (mt.pow(x, 4) + 5.0 * mt.pow(x,3) + 2.5 * mt.pow(x,2) + -5.0 * mt.pow(x,1) + 5.0)
		
	
def secant_method(func, x0, alpha=1.0, tol=1E-9, maxit=200):
    """
    Uses the secant method to find f(x)=0.  
    
    INPUTS
    
        * f     : function f(x)
        * x0    : initial guess for x
        * alpha : relaxation coefficient: modifies Secant step size
        * tol   : convergence tolerance
        * maxit : maximum number of iteration, default=200        
    """
    # You can write more than one command per line in Python:
    x, xprev = x0, 1.001*x0
    f, fprev = func(x), func(xprev)
    
    rel_step = 2.0 *tol
    k = 0
    print('{0:12} {1:12} {2:12} {3:12} {4:12}'\
    .format('Iteration', 'x', 'f(x)', 'Rel step', 'alpha * Delta x'))
    
    while (abs(f) > tol) and (rel_step) > tol and (k<maxit):        
        rel_step = abs(x-xprev)/abs(x)
        
        # Full secant step
        dx = -f/(f - fprev)*(x - xprev)
        
        # Update `xprev` and `x` simultaneously
        xprev, x = x, x + alpha*dx
        
        # Update `fprev` and `f`:
        fprev, f = f, func(x)
        
        k += 1
        
        print('{0:10d} {1:12.5f} {2:12.5f} {3:12.5f} {4:12.5f}'\
        .format(k, xprev, fprev, rel_step, alpha*dx))
                
    return x
