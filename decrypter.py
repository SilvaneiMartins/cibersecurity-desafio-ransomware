import os
import pyaes

# abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
key = b"testeransomwares"

# criar um novo arquivo para escrever os dados descriptografados
with open(file_name, "rb") as file:
    with open("teste.txt", "wb") as new_file:
        aes = pyaes.AESModeOfOperationCTR(key)
        while True:
            # ler o arquivo em blocos de 1024 bytes
            data = file.read(1024)
            if not data:
                break
            # descriptografar o bloco de dados
            decrypt_data = aes.decrypt(data)
            # escrever o bloco descriptografado no novo arquivo
            new_file.write(decrypt_data)

# remover o arquivo criptografado
os.remove(file_name)