import requests
import os
from bs4 import BeautifulSoup
import sys

def main():
	print(">>> Starting ctf-starter...")
	#IP = input("Enter the IP address of this mf box:")
	IP = sys.argv[1]
	if len(sys.argv) > 2:
		print(">>>too many arguments, quitting")
		exit()
	try:
		r = requests.get(f'http://{IP}')
	
		if r.status_code == 200:
			print(">>> Found a HTTP server, diggin for a wordlist now...")
			soup = BeautifulSoup(r.content, 'html.parser')
			text = soup.get_text().strip()
			f = open(f"{IP}words.txt", "x")
			f.write(text)
			f.close()
			print(">>> created a text file!")
	except:
		print(">>> No HTTP web server found")





if __name__ == '__main__':
	main()
