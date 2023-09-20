
import math
import random
from math import *


class main():
    
    def picking_p_and_q(self):
        
        # prime #'s p and q
        p = 1
        q = 1

        

        # length n
        n = p*q

        # phi
        phi = (q-1)(p-1)


    # Dr. Hu
    def testPrime_brute_force(psuedo_prime):
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
            C = (self.M)^(self.e) % self.n

            return C
        #decrypt
        else:
            # M = C^d mod n
            self.M = (self.C)^(self.d) % self.n

        return self.M
        
  
        

    #PLACEHOLDERS FOR TESTING - REVISE
    def helloWorld1():
        print("Hello world1")
    def helloWorld2():
        print("Hello world2")
    def helloWorld3():
        print("Hello world3")
    def helloWorld4():
        print("Hello world4")
    def helloWorld5():
        print("Hello world5")
    def helloWorld6():
        print("Hello world6")

    print("RSA keys have been generated")
    #GET KEYS HERE - REVISE

    dict_of_options = {1:('Please select your user type','1. A public user','2. The owner of the keys','3. Exit program'),
                    2:('As a public user what would you like to do?','1. Send an encrypted message','2. Authenticate a digital signature','3. Exit'),
                    3:('As the owner of the keys what would you like to do?', '1. Decrypt a received message','2. Digitally sign a message','3. Show the keys','4. Generating a new set of the keys','5. Exit'),}

    dict_of_operations = {'2a':helloWorld1,
                        '2b':helloWorld2,
                        '3a':helloWorld3,
                        '3b':helloWorld4,
                        '3c':helloWorld5,
                        '3d':helloWorld6}

    #Start with key here
    key = 1

    #run while loop until cont = false
    cont = True

    while cont: 

        # Find printable options in dict_of_options
        if key in dict_of_options:

            #will store the options, and where a choice must be made on the option
            list_of_options = []

            #get the value from the dict_of_options without parenthese [()], quote ['], or comma [,]
            options_string = str(dict_of_options.get(key))
            options_string = options_string.replace("(","")
            options_string = options_string.replace(")","")
            options_string = options_string.replace("'","")

            #add these options to the list
            list_of_options = options_string.split(", ")

            #print the options where a choice must be made
            for seperated_list_of_options in list_of_options:
                if seperated_list_of_options.startswith(".",1):
                    print("\t" + seperated_list_of_options)
                else:
                    print(seperated_list_of_options)
            
            #user input corresponds to options to choose from
            option = input("\nEnter your choice: ")

            #main menu (start)
            if key == 1:
                if option == '1':
                    key = 2
                elif option == '2':
                    key = 3
                elif option == '3':
                    # exit program
                    cont = False
            #public user
            elif key == 2:
                if option == '1':
                    key = '2a'
                elif option == '2':
                    key = '2b'
                elif option == '3':
                    key = 1
            #key owner 
            elif key == 3:
                if option == '1':
                    key = '3a'
                elif option == '2':
                    key = '3b'
                elif option == '3':
                    key = '3c'
                elif option == '4':
                    key = '3d'
                elif option == '5':
                    key = 1
            #invalid choice
            else:
                #reset
                print("Wrong selection, back to menu\n")
                key = 1

        # Find associated option operations in dict_of_operations
        else:
            if key == '2a' or key == '2b':
                functn = dict_of_operations[key]
                functn()
                # go back to public user menu
                key = 2
            else:
                functn = dict_of_operations[key]
                functn()
                # go back to key owner menu
                key = 3

    #Finished
    print("\nBye for now!")

if __name__ == "__main__":
    main()


        


