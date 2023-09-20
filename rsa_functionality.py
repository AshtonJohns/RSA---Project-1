from asyncio.windows_events import NULL
import math
import random
import math

from gcd import gcd

class rsa_functionality(object):

    def __init__(self):
        self.M = NULL
        self.C = NULL



    # For private user to decrypt public user's message
    def decrypt_received_message(self):

        if self.M == NULL:
            print("Sorry, no received messages at the moment\n")
            exit()
        
        decrypted_message = self.encrypt_or_decrypt_message(encrypt=False)

        for x in self.M:
            x = ord(x)
            x = (x-65)%26
            x += 65
            temp_M += chr(x)

        print("Decrypted message: " + str(decrypted_message))


    # For public user to send an encrypted message
    def send_encrypted_message(self):

        if self.M != NULL:
            answer = input("\nYou have a message currently that is encrypted and ready for the private user to read. Do you want to overwrite it? y/n: ")

            if answer == 'y':
                pass
            elif answer == 'n':
                exit()
            else:
                print("\nNo answer provided, you will be taken to the main menu\n")
                exit()

        self.M = input("\nEnter message: ")

        if isinstance(self.M,str) == False:
            print("Sorry, please enter a valid String. You will now be taken to the main menu\n")
            exit()

        # DO SOMETHING ON SELF.M!!!!!
        self.M = self.M.upper()

        temp_M = ''
        for x in self.M:
            x = ord(x)
            x = (x-65)%26
            x += 65
            temp_M += chr(x)

        self.M = int(temp_M)

        print("Your message you typed converted: " + str(self.M))

        # Returns Ciphertext
        self.C = self.encrypt_or_decrypt_message()

        print("\nMessage encrypted and sent...\n")

        print(self.C)

    # For public user to authenticate a digital signature
    def auth_digital_sig(self):
        
        print("Hello World")


    
    def generating_RSA_keys(self):
        
        # Get n and phi
        self.n,self.phi = self.picking_p_and_q()

        # Get public (e) /private (d) keys
        self.e = self.generate_public_key()

        self.d = self.generate_private_key()


    def picking_p_and_q(self):
        
        # prime #'s p and q
        p = self.finding_prime_number()
        q = self.finding_prime_number()

        # length n
        n = p*q

        # phi
        phi = (q-1)*(p-1)

        return n,phi


    # Dr. Hu
    def testPrime_brute_force(self,psuedo_prime):
        # a brute force method to test primality
        if psuedo_prime == 2:
            return True
        else:
            for b in range(2, math.floor(math.sqrt(psuedo_prime))):
                if math.gcd(psuedo_prime, b) > 1:
                    return False
                else:
                    continue
            return True

    # Dr. Hu
    def finding_prime_number(self):
        # Finding a pseudo-prime number using Fermat's test, then use testPrime_brute_force() method to test if it's PRIME

        # n1,n2: very large integers
        # k: constant integer, large enough so that probability of p not being prime is p ≤ (1/2)^k, 
        # in this case, (1/2)^k can be arbitrarily small
        n1=1000
        n2=1500
        k=150
        p = random.randint(n1,n2)
        # pseudo_prime = False
        prime = False

        while not prime: # original: while not pseudo_prime - REVISE
            for i in range(k):
                j = random.randint(2, p)
                if pow(j, p-1, p) > 1:
                    p = random.randint(n1, n2)
                    break
            # pseudo_prime = True
            #Now test if prime (should be evaluated to True), and so continue the loop if not
            prime = self.testPrime_brute_force(p)

        return p
    
    
    # Dr. Hu
    def extended_gcd(self, a = 1, b = 1):
        
        if b == 0:
            return (1, 0, a)
        (x,y,d) = self.extended_gcd(b, a%b)
        return y, x - a//b*y, d

    # Dr. Hu
    def generate_public_key(self):
        
        e = random.randint(2,self.phi)
        while gcd(e,self.phi) != 1:
            e = random.randint(2,self.phi)
        return e
    
    # Dr. Hu
    def generate_private_key(self):

        x = self.extended_gcd(self.e, self.phi)
        d = x[0] % self.phi
        return d

    def encrypt_or_decrypt_message(self, encrypt = True):
        
        #encrypt
        if encrypt:
            # C = M^e mod n
            C = ((self.M)**(self.e)) % self.n

            return C
        #decrypt
        else:
            # M = C^d mod n
            M = ((self.C)**(self.d)) % self.n

            return M