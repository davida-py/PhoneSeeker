import os
import requests
from colorama import Style, Fore
import json
import platform

os_ = platform.system()

def init_logo():
    logo = f"""{Fore.LIGHTMAGENTA_EX}
 _____  _                         _____           _             
|  __ \| |                       / ____|         | |            
| |__) | |__   ___  _ __   ___  | (___   ___  ___| | _____ _ __ 
|  ___/| '_ \ / _ \| '_ \ / _ \  \___ \ / _ \/ _ \ |/ / _ \ '__|
| |    | | | | (_) | | | |  __/  ____) |  __/  __/   <  __/ |   
|_|    |_| |_|\___/|_| |_|\___| |_____/ \___|\___|_|\_\___|_|  

{Fore.BLUE}Script by: Alicc. \nUsing Numverify API.{Style.RESET_ALL}\n"""
    clear(os_)
    
    print(logo)

def clear(os_):
    if os_ == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def cd(path):
    os.chdir(path)

def write_file(file_name, content, type_write):
    if type_write != "r":
        with open(file_name, type_write) as file:
            file.write(f"{content}\n") 
    else:
        print(f"{Fore.RED}Error: Invalid method.{Style.RESET_ALL}")
        
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            
        return lines
    except Exception as Error:
        print(f"{Fore.RED}Non-existent file. {Style.RESET_ALL}")
        
        return None 

def get_arg(line):
    arg = line.split(": ")

    if len(arg) > 0:
        arg = arg[1].strip()

        return arg
    else:
        return arg[0]

def get_phone_info(api_key, country_code, phone_number):
    agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}
    
    query = requests.get(
        f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code={country_code}&format=1", 
        headers=agent
    )
    
    data_response = json.loads(query.text)
    
    for data in data_response:
        print(f"{Fore.GREEN}[+] {Fore.BLUE}{data}: {data_response[data]}")
    
    return json.loads(query.text)

# INIT

init_logo()

config_file = read_file("Config.txt")

country_code = get_arg(config_file[0])
api_key = get_arg(config_file[1])
folder_saves = get_arg(config_file[2])

phone_number = input(f"Phone Number (Without +000): {Fore.GREEN}")

print("\n", end="")

data_response = get_phone_info(api_key, country_code, phone_number)

cd(folder_saves)

for data in data_response:
    write_file(f"{phone_number}.txt" , f"[+] {data}: {data_response[data]}", "a")