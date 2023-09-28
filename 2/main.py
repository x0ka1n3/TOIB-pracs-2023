import string
import random

def genstrongpwd(length=8):
	if length=="": length=8
	chrdict = string.ascii_letters+string.digits
	return "".join(random.choices(chrdict, k=int(length)))


if __name__ == '__main__':
	length = input("Password length (default 8): ")
	print(genstrongpwd(length))