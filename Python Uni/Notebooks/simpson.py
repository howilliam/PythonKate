def Simpson(f, a, b, n=500):
    """
    Return the approximation of the integral of f
    from a to b using Simpson's rule with n intervals.
    """
    if a > b:
        print('Error: a={:g} > b={:g}'.format(a, b))
        return None
    # check that n is even:
    if n % 2 != 0:
        print('Warning: n={:d} is not an even integer!\nn={:d} will be used'.format(n, n+1))
        n = n+1 # make n even
    h = (b - a)/float(n)
    sum1 = 0
    for i in range(1, n//2 + 1):
        sum1 += f(a + (2*i-1)*h)
    sum2 = 0
    for i in range(1, n//2):
        sum2 += f(a + 2*i*h)
    integral = (b-a)/(3*n)*(f(a) + f(b) + 4*sum1 + 2*sum2)
    return integral