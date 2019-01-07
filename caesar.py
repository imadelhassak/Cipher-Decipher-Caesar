

def caesar(plaintext, shift):
	ciphertext=""
	for ch in plaintext:
		if ch.isalpha():
			stayInAlphabet = ord(ch) + shift
			if stayInAlphabet > ord('z'):
				stayInAlphabet -= 26
			finalLetter =chr(stayInAlphabet)
		ciphertext += finalLetter

	print("Your ciphertext is :", ciphertext)

caesar('Hello', 6)
#NKrru

def D_scaesar(ET, shift):
	cleartext=""
	for ch in ET:
		if ch.isalpha():
			stayInAlphabet = ord(ch) - shift
			if stayInAlphabet > ord('z'):
				stayInAlphabet -= 26
			finalLetter =chr(stayInAlphabet)
		cleartext += finalLetter

	print("Your clear text  is :", cleartext)

D_scaesar('NKrru', 6)