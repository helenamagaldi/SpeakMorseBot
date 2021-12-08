from morse_dict import MORSE_CODE_DICT


def decrypt(message):
    message += " "

    decipher = ""
    citext = ""

    for letter in message:
        if (letter != " "):
            i = 0
            citext += letter

        else:
            i += 1

            if i == 2:
                decipher += " "

            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""

    return decipher

def main():

	message = str(input("give me your morse"))
	result = decrypt(message)
	print (result)

if __name__ == '__main__':
	main()
