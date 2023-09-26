def gcd(a=1, b=1):
    ''' The gcd function implements Euclid's
    GCD algorithm to find the greatest common
    divisor of two positive integers a and b'''
    
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# print(gcd(412, 260))
# print(gcd(260, 412))

def extended_gcd(a =1, b = 1):
    ''' The extended_gcd function implements the
    extension of Euclid's GCD algorithm to find integers x and y
    such that ax + by = gcd(a, b) '''
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a%b)
    return y, x - a//b*y, d

# x, y, d = extended_gcd(144, 900)
# print(x, y, d)
# x, y, d = extended_gcd(412, 260)
# print(x, y, d)
        
