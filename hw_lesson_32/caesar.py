class Caesar:
    def __init__(self, shift):
        self.__shift = shift
        self.__alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                           'h', 'i', 'j', 'k', 'l', 'm', 'n',
                           'o', 'p', 'q', 'r', 's', 't', 'u',
                           'v', 'w', 'x', 'y', 'z']

        encryptor = dict(zip(self.__alphabet, self.__alphabet[self.__shift:]+self.__alphabet[:self.__shift]))
        decryptor = {value: key for key, value in encryptor.items()}
        self.__caesar = {"encryptor": encryptor, "decryptor": decryptor}

    def encrypt(self, message):
        encrypted_message = ""
        for letter in message.lower():
            if letter.isalpha():
                encrypted_message += self.__caesar["encryptor"][letter]
            else:
                encrypted_message += letter
        return encrypted_message

    def decrypt(self, encrypted_message):
        dencrypted_message = ""
        for letter in encrypted_message:
            if letter.isalpha():
                dencrypted_message += self.__caesar["decryptor"][letter]
            else:
                dencrypted_message += letter
        return dencrypted_message

    def __call__(self, shift):  # it changes shift of encryption
        self.__init__(shift)


if __name__ == "__main__":
    print("Caesar cipher algorithm")
