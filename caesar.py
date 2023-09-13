def cipher(key = 3):
    message = input('Type your short message:  ')
    message = message.upper()
    st = "Here is the ciphered text: "
    for x in message:
        x = ord(x) + key
        x = (x-65)%26
        x += 65
        st = st + chr(x)
    print(st)

cipher1(1000)
    
