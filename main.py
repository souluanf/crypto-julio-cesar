from util.cryptography import Cryptography

crypt = Cryptography()
token = 'SEUTOKEN'

# Gerar answer.json
crypt.generate_data(token=token)

# Pegar dados
dados = crypt.read_data()

# # Cifar dados
# # crypt.encrypt(dados['decifrado'], 3)

# Decifrar dados
crypt.decrypt_message(dados['cifrado'], dados['numero_casas'])

# # Gerar resumo_criptografico (sha1)
crypt.generate_hash()

crypt.submit_solution(token=token)
