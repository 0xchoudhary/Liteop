import os 
from time import sleep
os.system("figlet -f banner NMAP AND FFUF SCANNING TOOL" )
sleep(2)
print('''
██╗░░░░░██╗████████╗███████╗░░░░░░░█████╗░░█████╗░███████╗░█████╗░
██║░░░░░██║╚══██╔══╝██╔════╝░░░░░░██╔══██╗██╔══██╗╚════██║██╔══██╗
██║░░░░░██║░░░██║░░░█████╗░░█████╗╚██████║██║░░██║░░░░██╔╝╚█████╔╝
██║░░░░░██║░░░██║░░░██╔══╝░░╚════╝░╚═══██║██║░░██║░░░██╔╝░██╔══██╗
███████╗██║░░░██║░░░███████╗░░░░░░░█████╔╝╚█████╔╝░░██╔╝░░╚█████╔╝
╚══════╝╚═╝░░░╚═╝░░░╚══════╝░░░░░░░╚════╝░░╚════╝░░░╚═╝░░░░╚════╝░
''')
os.system("figlet Enter IP:")
n=input("")
def nmap():
    op=input("Enter plugins for nmap scan (Default Plugins: -sV -T5)")

    os.system(f"nmap -T5 -sV {n} {op}")
nmap()
g=input("Extension scan or normal scan E/N?")
if g=="e" or g=="E":
    n2=list(input("Enter extentions (PLEASE USE , TO SEPREATE VALUES)"))
    
    def gobuster():
        os.system(f"gobuster dir -u http://{n} -x {n2} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
    gobuster()
else:
    n1=input("Directory Scan Medium/Comman M/C?")
    def ffuf():
        if n1=="m":
            os.system(f"ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://{n}/FUZZ")
        else:
            os.system(f"ffuf -w /usr/share/wordlists/dirb/common.txt -u http://{n}/FUZZ ")
    ffuf()

