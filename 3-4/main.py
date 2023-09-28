import re

strongpwdregex = r"^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$"

def checkpwdstrength(password):
	if re.findall(strongpwdregex, password): 	return 1
	else:										return 0
		

if __name__ == '__main__':
	choice = input("""
		-------MENU-------
		1. Check one password
		2. Check file
		Choice: """)
	
	if choice == "1":
		print("P@ssw0rd strong") if checkpwdstrength(input("Give me your strong password: ")) else print("Password is not P@assw0rd (weak)")
	elif choice == "2":
		with open(input("Filename: "), "r") as file:
			for line in file.readlines():
				if checkpwdstrength(line): print(line)