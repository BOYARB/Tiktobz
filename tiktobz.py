import requests
import random
import string
from colorama import init, Fore, Style
import signal
import sys

# Initialize colorama
init(autoreset=True)

# Print a stylish header
print(Fore.YELLOW + """
 _______ _ _    _        _        
|__   __(_) |  | |      | |       
   | |   _| | _| |_ ___ | |__ ____
   | |  | | |/ / __/ _ \| '_ \_  /
   | |  | |   <| || (_) | |_) / / 
   |_|  |_|_|\_\\__\___/|_.__/___|
                                    
""")
print(Fore.CYAN + "Find a rare name on TikTok🫰️  ")
print(Fore.MAGENTA + "Made by BOYARB❤️ \n")

# Function to check if a username exists
def check_username(session, username):
    # Remove @ if it exists
    username = username.lstrip('@')
    
    url = f"https://www.tiktok.com/@{username}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Connection": "keep-alive",  # Keep connection open for faster future requests
    }

    try:
        response = session.get(url, headers=headers, timeout=5)  # 5 seconds timeout for fast failure
        if response.status_code == 200:  # Username exists
            return True
        elif response.status_code == 404:  # Username does not exist
            return False
        else:
            return None  # Other HTTP statuses
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error while checking username: {e}")
        return None  # Handle network errors

# Function to generate a random username of 3 or 4 characters with upper, lower, and digits
def generate_username(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits  # Including uppercase, lowercase, and digits
    return ''.join(random.choices(characters, k=length))

# Handle Ctrl+Z press to stop the program
def signal_handler(sig, frame):
    print()  # Add a blank line before "Stopped"
    print("\033[97mStopped")  # Display "Stopped" in white
    sys.exit(0)

# Handle Ctrl+C press to exit silently
def exit_handler(sig, frame):
    sys.exit(0)  # Exit silently without any message

# Register the signal handlers
signal.signal(signal.SIGTSTP, signal_handler)  # For Ctrl+Z
signal.signal(signal.SIGINT, exit_handler)  # For Ctrl+C

def main():
    print(Fore.GREEN + "Select username type:")
    choice = input(Fore.YELLOW + "Do you want a 3-character or 4-character username? (3/4): ")

    if choice == '3':
        length = 3
    elif choice == '4':
        length = 4
    else:
        print(Fore.RED + "Invalid choice. Please choose 3 or 4.")
        return

    print(Fore.CYAN + f"Searching for an available {length}-character username...\n")

    # Create a session to optimize connection
    with requests.Session() as session:
        while True:
            username = generate_username(length)
            print(Fore.YELLOW + f"Generated username: {username}")
            
            # Wait for the server response before proceeding
            available = check_username(session, username)  # Wait for the server to respond
            
            if available:  # If the username is taken
                print(Fore.RED + f"Username @{username} is taken. Trying a new one...")
            elif available is False:  # If the username is available
                print(Fore.GREEN + f"Username @{username} is available for use!")
                print(Fore.CYAN + "Search completed! Username found that is not in use.")
                break  # Stop after finding an available username
            else:
                print(Fore.RED + "There was an issue checking the username. Retrying...")
                continue  # Retry if there's an issue (like network errors)

if __name__ == "__main__":
    main() 
    