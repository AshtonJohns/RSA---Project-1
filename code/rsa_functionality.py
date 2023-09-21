from asyncio.windows_events import NULL
import math
import random

from gcd import gcd


class rsa_functionality(object):

    def __init__(self):
        # Plaintext
        self.M = NULL
        #list of public user's messages
        self.list_Ms = []
        #list of encrypted messages
        self.list_Cs = []
        #dictionary for key owner to choose which self.M they'd like to decrypt
        self.dict_Ms_decrypt = {}
        # Ciphertext, but as an integer!
        self.C = NULL
        # Message that will be digitally signed
        self.signed_M = NULL
        #list of signed messages that can be viewed by the public user
        self.list_signed_Ms = []
        #list of signed messages that contains the encrypted data
        self.list_authenticated_Ms = []
        #dict of signed messages for public user to choose which self.signed_M they'd like to authenticate
        self.dict_authenticated_Ms = {}
        # Original message to compare signed message
        self.not_signed_M = NULL

    #converting between strings and integers
    def message_conversion(self,message=NULL,convert_to_text=True):

        #conver to string
        if convert_to_text:
            #convert numbers to a string
            numbers = str(message)
            numbers_list = []
            #make a list of string numbers, each index containing 2 digits
            for i in range(0, len(numbers), 2):
                numbers_list.append(numbers[i:i+2])
            #temp string to append char values to 
            temp_M = ''
            #assemble word
            for x in numbers_list:
                temp_M += chr(int(x))
            
            numbers_to_string = temp_M # str of numbers but now in char
            return numbers_to_string
        #convert to integers
        else:
            #conver to uppercase to minimize troubles!
            message = message.upper()
            #temp string to append the typecasetd Unicode to
            temp_M = ''
            #get unicode for each letter in 'message', and append to temp_M
            for x in message:
                x = ord(x)
                temp_M += str(x)

            message_to_integers = int(temp_M) # convert to an integer for further operations...
            return message_to_integers


    # For private user to decrypt public user's message
    def decrypt_received_message(self):

        if len(self.list_Ms) == 0:
            print("\nSorry, no received messages at the moment\n")
            return

        print("The following messages are available: \n")

        #use for loop to show the self.M's, and then store a dictionary with an key (1,2,3,etc..) and a value (self.M)
        #reset
        self.dict_Ms_decrypt = {}
        for key, value in enumerate(self.list_Cs):
            self.dict_Ms_decrypt[key] = value
            value_str = self.list_Ms[key]
            value_len = len(value_str)
            number = key + 1
            print("\t"+str(number)+". (length == "+str(value_len)+")")

        #Choose 1,2,3,etc
        choice = input("\nEnter your choice: ")
        #conver to int
        choice = int(choice)
        choice -= 1
        #find the message in the dictionary in order to decrypt
        self.C = self.dict_Ms_decrypt.get(choice)
        
        ciphertext_in_integers = self.C
        
        decrypted_message = self.encrypt_or_decrypt_message(ciphertext_in_integers=ciphertext_in_integers,encrypt=False)

        decrypted_message = self.message_conversion(decrypted_message,convert_to_text=True)

        print("\nDecrypted message: " + decrypted_message + "\n")


    # For public user to send an encrypted message
    def send_encrypted_message(self):

        # if self.M != NULL:
        #     answer = input("\nYou have a message currently that is encrypted and ready for the private user to read. Do you want to overwrite it? y/n: ")

        #     if answer == 'y':
        #         pass
        #     elif answer == 'n':
        #         return
        #     else:
        #         print("\nNo answer provided, you will be taken to the main menu\n")
        #         return


        message_to_encrypt = input("\nEnter message: ")

        #store this into a list of messages entered by public user
        self.list_Ms.append(message_to_encrypt)

        # check user entry, if there are any restrictions, put them here - REVISE
        self.M = message_to_encrypt

        message_to_encrypt = self.message_conversion(message_to_encrypt,convert_to_text=False)

        # Returns Ciphertext
        self.C = self.encrypt_or_decrypt_message(plaintext_in_integers=message_to_encrypt,encrypt=True)

        #add to list of self.Cs
        self.list_Cs.append(self.C)

        print("\nMessage encrypted and sent...\n")


    # For private user to digitally sign a message
    def digital_sig(self,authenticate):

        #authenticate
        if authenticate:
            #check if there are any messages to authenticate
            if len(self.list_signed_Ms) == 0:
                print("\nSorry, no messages to authenticate.\n")
                return
            #display available messages
            print("\nThe following messages are available:\n")
            for key, value in enumerate(self.list_authenticated_Ms):
                self.dict_authenticated_Ms[key] = value
                number = key + 1
                print("\t" + str(number) + ". " + self.list_signed_Ms[key])
            #ask which choice
            choice = input("\nEnter your choice: ")
            choice = int(choice)
            choice -= 1
            #get value for the signed message to validate
            self.signed_M = self.dict_authenticated_Ms[choice]
            #otherwise, perform authentication by performing fast exponentiation using self.signed_M and public key self.e
            message = pow(self.signed_M,self.e,self.n)
            #conver to text
            message = self.message_conversion(message=message,convert_to_text=True)
            #check whether the message is the same as original message
            if message == self.list_signed_Ms[choice].upper():
                print("\nSignature is valid!\n")
            else:
                print("\nSignature invalid!\n")

        #sign
        else:
            message = input("\nPlease enter your message to be digitally signed: ")

            #MAKE SURE INPUT IS GOOD HERE

            #Store original message 
            self.not_signed_M = message
            #Store message into list of messages to be viewed by public user
            self.list_signed_Ms.append(message)
            #convert message into integers
            message_to_be_signed = message
            message_to_be_signed = self.message_conversion(message=message_to_be_signed,convert_to_text=False)
            #now sign it, using private key self.d
            signed_message = pow(message_to_be_signed,self.d,self.n)
            #store it into list 
            self.list_authenticated_Ms.append(signed_message)
            #self.signed_M = signed_message
            print("\nMessage signed and sent.\n")


    def generating_RSA_keys(self):
        
        # Get n and phi
        self.n,self.phi = self.picking_p_and_q()

        # Get public (e) /private (d) keys
        self.e = self.generate_public_key()

        self.d = self.generate_private_key()

        print("\nRSA keys have been generated\n")


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
        n1=100000000000
        n2=150000000000
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
    
    # show private and public keys as key owner
    def show_keys(self):
        print("\nPrivate key: " + str(self.d))
        print("\nPublic key: " + str(self.e) + "\n")      

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

    def encrypt_or_decrypt_message(self, plaintext_in_integers=NULL,ciphertext_in_integers=NULL,encrypt = True):
        
        #encrypt
        if encrypt:
            #fast exponentiation
            ciphertext = pow(plaintext_in_integers,self.e,self.n)

            return ciphertext
        #decrypt
        else:
            #fast exponentiation
            M = pow(ciphertext_in_integers,self.d,self.n)

            return M