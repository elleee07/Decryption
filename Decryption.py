# ELLA MARIE A. MALLARI
# BSCPE 1-4

#ask user to input their name: 
name = input("Please enter your name: ")

# input encrypted text
print("\033[0;32m=" * 80)
encrypted_text = input("\033[0;32mTYPE ENCRYPTED TEXT: ")
decrypted_text = ""
# check every symbol to substitute
for i in range(len(encrypted_text)):
    # if *, make it a
    if encrypted_text [i] == "*":
        decrypted_text += "a"
    # if &, make it e
    elif encrypted_text [i] == "&":
        decrypted_text += "e"
    # if &, make it i
    elif encrypted_text [i] == "#":
        decrypted_text += "i"
    # if &, make it o
    elif encrypted_text [i] == "+":
        decrypted_text += "o"
    # if &, make it u
    elif encrypted_text [i] == "!":
        decrypted_text += "u"
    else:
        decrypted_text += encrypted_text[i]
# print decrypted text 
