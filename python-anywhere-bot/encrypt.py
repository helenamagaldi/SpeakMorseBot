from morse import MORSE_CODE_DICT


def encrypt(received_message):
    if received_message.find("/encrypt ") != -1:
        received_message = received_message[8:]

    received_message = received_message.upper()

    cipher = ""

    for letter in received_message:
    	if letter != " ":
    		cipher += MORSE_CODE_DICT[letter] + " "
    	else:
    		cipher += " "

    return cipher
