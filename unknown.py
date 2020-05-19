import cryptography
import os
import time

class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

def banner ():
	os.system('cls' if os.name == 'nt' else 'clear')
	print (bcolors.RED + bcolors.BOLD)	
	print ("""		 -------------------------------------
	          _  _ _  _ _  _ _  _ ____ _ _ _ _  _ ©
		  |  | |\ | |_/  |\ | |  | | | | |\ |
		  |__| | \| | \_ | \| |__| |_|_| | \|
 
		 -------------------------------------""")
	print (bcolors.ENDC)


def Unknownlinencryption():	
	banner()			
	encryptloop=0
	while encryptloop <10:
		print (bcolors.RED,	" Line encryption mode ")
		inputstr = input ("  Enter your line >> ")
		if inputstr == "":
		    main()
		else:
			from cryptography.fernet import Fernet
			Algorithm_key = Fernet.generate_key()
			file = open('Unknown.key', 'wb')
			file.write(Algorithm_key) 
			file.close()
			file = open('Unknown.key', 'rb')
			Algorithm_key = file.read() 
			file.close()
			from cryptography.fernet import Fernet
			text_data = inputstr.encode()
			f = Fernet(Algorithm_key)
			encrypted = f.encrypt(text_data)
			print (bcolors.ENDC,	bcolors.GREEN,	"Encrypted data >>", end="")
			print(bcolors.ENDC,	bcolors.WHITE, end="")
			print (encrypted[7:],	bcolors.ENDC)
			print (bcolors.RED," -------------------------------------------------------",	bcolors.ENDC)

def Unknownfilencryptmode ():
	banner()
	encryptloop=0
	while encryptloop <10:
		print (bcolors.RED,	" File encrypt mode ")		
		input_file = input ("  File name >> ")
		if input_file == "":
		    main()
		else:
			from cryptography.fernet import Fernet
			Algorithm_key = b'X0De9kKssMOEMmi6gK4lMskwYA_jvvK4Jsd-UgLbzrw=' 
			output_file = f"{input_file}.unknown"
			with open(input_file, 'rb') as f:
			    data = f.read()
			fernet = Fernet(Algorithm_key)
			encrypted = fernet.encrypt(data)
			with open(output_file, 'wb') as f:
		    	    f.write(encrypted)
			print (bcolors.ENDC,	bcolors.GREEN,	"Encrypted file name >>", end="")
			print(bcolors.ENDC,	bcolors.WHITE, end="")
			print( f"{output_file}",	bcolors.ENDC)
			print (bcolors.RED,	" -------------------------------------------------------",	bcolors.ENDC)

def Unknownfiledecryptmode ():	
	banner()
	encryptloop=0
	while encryptloop <10:
		print (bcolors.RED,	" File decrypt mode ")		
		input_defile = input ("  Encrypted file name >> ")
		if input_defile == "":
		    main()
		else:			
			from cryptography.fernet import Fernet
			Algorithm_key = b'X0De9kKssMOEMmi6gK4lMskwYA_jvvK4Jsd-UgLbzrw='
			output_file = f"{input_defile}.known"

			with open(input_defile, 'rb') as f:
			    data = f.read()

			fernet = Fernet(Algorithm_key)
			encrypted = fernet.decrypt(data)

			with open(output_file, 'wb') as f:
			    f.write(encrypted)
			print (bcolors.ENDC,	bcolors.GREEN,	"Decrypted file name >>", end="")
			print(bcolors.ENDC,	bcolors.WHITE, end="")
			print( f"{output_file}",	bcolors.ENDC)	
			print (bcolors.RED,	" -------------------------------------------------------",	bcolors.ENDC)
def main ():
	banner()
	print (bcolors.BLUE )
	print ("""   	        [ Press Enter to return to this menu ]

  [1] Line encryption mode  [2] File encrypt mode  [3] File decrypt mode
		""")
	
	mode = input("  Choose mode > ")
	if mode == "1": 
		Unknownlinencryption()
	elif mode == "2": 
		Unknownfilencryptmode()
	elif mode == "3":
		Unknownfiledecryptmode()
	else:
		print (bcolors.RED )
		print ("  ERROR : Invalid entry ! " )
		print (bcolors.ENDC)
		time.sleep(2)
		main()	
main()
