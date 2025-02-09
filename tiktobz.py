import requests
import random
import string
from colorama import init, Fore, Style
import signal
import sys

init(autoreset=True)

print(Fore.YELLOW + r"""
 _______ _ _    _        _
|__   __(_) |  | |      | |
   | |   _| | _| |_ ___ | |__ ____
   | |  | | |/ / __/ _ \| '_ \_  /
   | |  | |   <| || (_) | |_) / /
   |_|  |_|_|\_\__\___/|_.__/___|
                                    
""")
print(Fore.CYAN + "Find a rare name on TikTok🫰️ ")
print(Fore.MAGENTA + "Made by BOYARB❤️ \n")

def check_username(session, username):
    username = username.lstrip('@')
    url = f"https://www.tiktok.com/@{username}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Connection": "keep-alive",  
    }

    try:
        response = session.get(url, headers=headers, timeout=5)  
        if response.status_code == 200:  
            return True
        elif response.status_code == 404:  
            return False
        else:
            return None  
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error while checking username: {e}")
        return None  

def generate_username(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "._"
    return ''.join(random.choices(characters, k=length))  

def signal_handler(sig, frame):
    print()  
    print("\033[97mStopped")  
    sys.exit(0)

def exit_handler(sig, frame):
    sys.exit(0)  

signal.signal(signal.SIGTSTP, signal_handler)  
signal.signal(signal.SIGINT, exit_handler)  

def main():
    print(Fore.GREEN + "Select username type:")
    
    while True:
        choice = input(Fore.YELLOW + "Do you want a 3-character or 4-character username? (3/4): ")

        if choice == '3':
            length = 3
            break
        elif choice == '4':
            length = 4
            break
        else:
            print(Fore.RED + "Invalid choice. Please choose 3 or 4.")

    print(Fore.CYAN + f"Searching for an available {length}-character username...\n")

    with requests.Session() as session:
        while True:
            username = generate_username(length)
            print(Fore.YELLOW + f"Generated username: {username}")
            
            available = check_username(session, username)  
            
            if available:  
                print(Fore.RED + f"Username @{username} is taken. Trying a new one...")
            elif available is False:  
                print(Fore.GREEN + f"Username @{username} is available for use!")
                print(Fore.CYAN + "Search completed! Username found that is not in use.")
                break  
            else:
                print(Fore.RED + "There was an issue checking the username. Retrying...")
                continue  

if __name__ == "__main__":
    main() 
