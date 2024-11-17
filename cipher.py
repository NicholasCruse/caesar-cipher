def encrypt_text(Message,Rshift):
    ans = ""
    # iterate over the given Message
    for Letter in range(len(Message)):
        char = Message[Letter]
        # check if the character is a letter.
        if char.isalpha():
            # check if space is there then simply add space.
            if char==" ":
                ans+=" "
            # check if a character is uppercase then encrypt it accordingly.
            elif (char.isupper()):
                ans += chr((ord(char) + Rshift-65) % 26 + 65)
            # check if a character is lowercase then encrypt it accordingly.
            else:
                ans += chr((ord(char) + Rshift-97) % 26 + 97)
        #Keeps Non-alphabetic characters unchange or erased.
        else:
            ans += char
    
    return ans

Message = input("Input your Message to be encrypted.")
Rshift = 5
print("The Message Text is: " + Message)
print("The pattern is Shifted over to the right by: " + str(Rshift))
print("The encrypted Text is: " + encrypt_text(Message,Rshift))