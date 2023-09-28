import string
import time
import random
import itertools

starttime = time.time()

minlen = 4
maxlen = 8

chrdict = string.ascii_letters+string.digits+"!@#$%^&*"

pwdsample = "".join(random.choices(chrdict, k=random.randint(minlen,maxlen)))

def bruteforce():
	for length in range(minlen,maxlen+1):
		for perm in itertools.permutations(chrdict, length):
			if "".join(perm) == pwdsample:
				print(f"Password '{pwdsample}' cracked for {time.time()-starttime:.2f} secs")
				return

if __name__ == '__main__':
	print(f"[Cracking {pwdsample}]")
	bruteforce()