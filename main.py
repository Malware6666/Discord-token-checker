import requests
import concurrent.futures
import yaml
import random
import time
import datetime
import os
import ctypes
from colorama import Fore, Style

ctypes.windll.kernel32.SetConsoleTitleW(f"Token Checker")
config = yaml.safe_load(open('config.yml'))

def get_type(token):
    try:
        now = datetime.datetime.now(datetime.timezone.utc)
        directory = f'output/{now.strftime("%d-%m-%Y")}'
        os.makedirs(directory, exist_ok=True)
        token_type = ''
        session = requests.Session()
        if config['proxies']:
            proxylist = open('proxies.txt', 'r').read().splitlines()
            session.proxies = 'http://' + random.choice(proxylist)
        
        response = session.get(f'https://discord.com/api/v9/users/@me', headers={'Authorization': token.split(':')[-1]})
        
        if response.status_code == 429:
            print(f'{Fore.RED}Rate limited, use proxies or try again in a few days after Cloudflare clears your IP.{Style.RESET_ALL}')
            session.close()
            return token_type
        
        if response.status_code == 200:
            user = response.json()
            if user['email']:
                if user['verified']:
                    if user['phone']:
                        token_type = 'FV'
                        with open(f"{directory}/FV.txt", "a") as f:
                            f.write(f"{token}\n")
                    else:
                        token_type = 'EV'
                        with open(f"{directory}/EV.txt", "a") as f:
                            f.write(f"{token}\n")
                else:
                    if user['phone']:
                        token_type = 'PV'
                        with open(f"{directory}/PV.txt", "a") as f:
                            f.write(f"{token}\n")
                    else:
                        token_type = 'UV'
                        with open(f"{directory}/UV.txt", "a") as f:
                            f.write(f"{token}\n")
            else:
                token_type = 'UC'
                with open(f"{directory}/UC.txt", "a") as f:
                    f.write(f"{token}\n")
        elif response.status_code == 401:
            token_type = 'IV'
            with open(f"{directory}/IV.txt", "a") as f:
                f.write(f"{token}\n")

        token_type_color = ''

        if token_type == 'EV':
            token_type_color = Fore.LIGHTGREEN_EX
        elif token_type == 'UC':
            token_type_color = Fore.MAGENTA
        elif token_type == 'FV':
            token_type_color = Fore.BLUE
        elif token_type == 'UV':
            token_type_color = Fore.CYAN
        elif token_type == 'PV':
            token_type_color = Fore.LIGHTBLUE_EX
        elif token_type == 'IV':
            token_type_color = Fore.RED

        print(f'Token: {token_type_color}{token}{Style.RESET_ALL} - Type: {token_type_color}{token_type}{Style.RESET_ALL}')

        session.close()
        return token_type
    
    except Exception as e:
        print(e)
        get_type(token)

token_count = 0

with concurrent.futures.ThreadPoolExecutor(max_workers=config['max_threads']) as executor:
    tokens = open('tokens.txt', 'r').read().splitlines()
    futures = []
    start = time.time()
    session = requests.Session()
    for token in tokens:
        token_count += 1
        futures.append(executor.submit(get_type, token))

concurrent.futures.wait(futures)

end = time.time()
elapsed_time = end - start
print(f"Checked {token_count} tokens in {elapsed_time:.2f} seconds")
input("Press Enter to exit...")
