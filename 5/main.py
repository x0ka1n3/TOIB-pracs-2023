import hashlib
import requests

api = "https://api.pwnedpasswords.com/range/"

def checkpwnedpwd(password):
	pwdhash = hashlib.sha1(password.encode()).hexdigest().upper()
	response = requests.get(api+pwdhash[:5]).text
	for suffix in response.split("\n"):
		if pwdhash[:5]+suffix.split(":")[0] == pwdhash: print(f"Password found {suffix.split(':')[1]} times"); return
	print("Password not found in any breaches")

if __name__ == '__main__':
	checkpwnedpwd(input("Give me your password: "))