import hashlib
import json
import sys
import requests


class Cryptography:

	def __init__(self):
		self.__alfabeto = 'abcdefghijklmnopqrstuvwxyz'
		self.__url_challenge = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
		self.__url_answer = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='
		self.__dados = ''

	def generate_data(self, token):
		url = self.__url_challenge + token
		challenge = requests.get(url)
		if challenge.status_code == 404:
			print('Erro ao gerar dados')
			sys.exit()
		with open('answer.json', 'w') as answer:
			json.dump(challenge.json(), answer)

	def encrypt_message(self, message, numero_casas):
		cifrado = ''
		for caractere in message.lower():
			if caractere in self.__alfabeto:
				index = self.__alfabeto.find(caractere) + numero_casas
				if index >= 26:
					index -= 26
				cifrado += self.__alfabeto[index]
			else:
				cifrado += caractere


	def decrypt_message(self, message, numero_casas):
		decifrado = ''
		for caractere in message:
			if caractere in self.__alfabeto:
				index = self.__alfabeto.find(caractere) - numero_casas
				decifrado += self.__alfabeto[index]
			else:
				decifrado += caractere
		with open('answer.json', 'r') as answer:
			dados = json.load(answer)
		self.__dados['decifrado'] = decifrado
		with open('answer.json', 'w') as answer:
			json.dump(dados, answer)
		return print(f'DECIFRADO: {decifrado}')

	def read_data(self):
		with open('answer.json', 'r') as answer:
			self.__dados = json.load(answer)
		return self.__dados

