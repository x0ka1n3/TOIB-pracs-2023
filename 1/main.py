import hashlib

def hashpwd(password):
	return hashlib.sha256(password.encode()).hexdigest()

if __name__ == '__main__':
	print(hashpwd(input("Your very strong password: ")))