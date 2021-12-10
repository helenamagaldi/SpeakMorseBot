from morse import MORSE_CODE_DICT


def decrypt(received_message):
    if received_message.find("/decrypt ") != -1:
        received_message = received_message[8:]

    received_message = received_message.upper()
    received_message += " "
    decipher = " "
    citext = ""
    i = 0

    for letter in received_message:
        if (letter != " "):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += " "
            else:
                if citext in list(MORSE_CODE_DICT.values()):
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    citext = ""

    return decipher