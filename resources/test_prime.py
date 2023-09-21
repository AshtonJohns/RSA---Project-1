import math
def testPrime_brute_force(a = 10):
    """ Test if a is prime with brute force"""
    for b in range(2, int(math.sqrt(a))):
        if math.gcd(a, b) > 1:
            print(a, '= '+str(math.gcd(a,b)) + '*' + \
                  str(a//math.gcd(a,b)) +'. Not prime.')
            return False
        else:
            continue
    return True

print(testPrime_brute_force(137))

def Fermat(p = 137):
    '''Test if p is prime with Fermat\'s little theorem\n'''
    t = True
    for i in range(1, p):
        if pow(i, p-1, p) != 1:
            t = False
            break
    if not t:
        print(p, 'is not prime.', i)
    else:
        print(p, 'is prime.')
Fermat(3271)

def Carmichael(c = 561):
    ''' Demonstrate a Carmichael number, say 561, all of
       x < 561 and i relatively prime to it, i passes
       Fermat Little Theorem'''

    k = 0
    m = 0
    for i in range(c):
        if pow(i, c-1, c)==1:
            k += 1
        else:
            m+= 1
    print(k, "numbers in Z_" +str(c) +" pass Fermat's test.")
    print(m, "numbers do not pass Fermat's test.")
    print('The probability of a number randomly picked from Z_' \
          +str(c))
    print(' that passes Fermat\'s test is '+ str(k/c))
Carmichael()




