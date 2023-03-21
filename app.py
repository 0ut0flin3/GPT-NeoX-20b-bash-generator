import requests
import os
import socket
import platform
import sys


global ACCESS_TOKEN

# replace <YOUR_ACCESS_TOKEN> with your Huggingface's access token
ACCESS_TOKEN = '<YOUR_ACCESS_TOKEN>'

if os.name=='nt':
   print("Not supported on Windows")
   sys.exit()
   
os.system("clear")



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
print(f"{bcolors.OKBLUE}This is an experimental testing app that uses the gpt-neox-20b model to generate Bash code from requests given in natural language. Have fun and good testing!{bcolors.ENDC}\n\n")


class Device():
    info = {'USER':os.getlogin(),'WORKINGDIR':os.getcwd(),'PLATFORM':platform.uname()._asdict()}
class Network():
    name=socket.gethostname()
    host=socket.gethostbyname(name)




API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neox-20b"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()





global PRE;PRE=f'''the info of my computer: {Device.info} 
the info of my network: {Network.name}, {Network.host}

'''


global contx;contx='the following is the Bash code, only the Bash code (without description) needed to '
while True:
      
      q=input(f'{bcolors.WARNING}Print the Bash code needed to {bcolors.ENDC}')  
      output = query([f"{PRE}{contx}{q}: "])
      output=output[0]["generated_text"].replace(contx,"")
      output=output.replace(q+":","")
      output=output.replace(f"{PRE}","")
      print("\n")
      print(f"{bcolors.OKCYAN}{output}{bcolors.ENDC}")
      print("\n\n")

      
     
           



