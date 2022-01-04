import requests
import os
from bs4 import BeautifulSoup
import sys

def main():
	print(">>> Starting ctf-starter...")
	IP = sys.argv[1]
	if len(sys.argv) > 2 or len(sys.argv) == 0:
		print(">>>too many arguments, quitting")
		exit()
	try:
		r = requests.get(f'http://{IP}') # assuming HTTP, as is standard for most boxes
	
		if r.status_code == 200:
			print(">>> Found a HTTP server, diggin for a wordlist now...")
			gather_wordlist(r)
			
		else:
			print(f"Non-200 response: {r.status_code}")
	except:
		print(">>> No HTTP web server found")


def gather_wordlist(r):
	soup = BeautifulSoup(r.content, 'html.parser')
			text = soup.get_text().strip()
			f = open(f"{IP}_words.txt", "x")
			f.write(text)
			f.close()
			print(">>> created a text file!")


if __name__ == '__main__':
	main()
