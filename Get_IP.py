import socket 
import pyfiglet
from rich import print 


class gethostname :
    def __init__(self,domain):
        self.domain = domain
        
    
    def trait(self):
        try :
            ip = socket.gethostbyname(self.domain)
            print(f"[blue]IP address of {self.domain} is {ip}[blue]")
        except socket.gaierror:
            print(f"[red]Could not get IP for {self.domain}[/]")



f = pyfiglet.Figlet(font="slant" , justify="auto")

print(f.renderText("GET HOST IP"))

domain = input("Enter The Domain Name : ")

run = gethostname(domain)

run.trait()


