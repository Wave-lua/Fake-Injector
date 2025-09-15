import time
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print("Welcome user")
    time.sleep(3)

    print("Loading...")
    time.sleep(5)

    print("Mapping...")
    time.sleep(3)

    text = "LOADED!!!"
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    
    for _ in range(30): 
        for color in colors:
            print(f"{color}{text}{Style.RESET_ALL}   ", end="\r", flush=True)
            time.sleep(0.1)

   
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")  
    print("Program will close in 15 seconds...")
    
    time.sleep(15)  

if __name__ == "__main__":
    main()
