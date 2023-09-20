def cipher(key = 3):
    message = input('Type your short message:  ')
    message = message.upper()
    st = ""
    st_x = ""
    for x in message:
        x = ord(x)
        print(x)
        x = (x-65)%26
        print(x)
        x += 65
        st_x += str(x)
        st += chr(x)
    print("Here is the ciphered text: ")
    print(st)
    print("Here is numbered: ")
    print(st_x)

    message_1 = st

    st = ""
    st_x = ""
    for x in message_1:
        x = ord(x)
        x = (x-65)%26
        x += 65
        st_x += str(x)
        st += chr(x)
    print("Here is the plaintext text: ")
    print(st)
    print("Here is numbered: ")
    print(st_x)

cipher(1000)
    
