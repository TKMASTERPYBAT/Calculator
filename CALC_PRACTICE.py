import os
from colorama import Fore, init
import time

def banner():
    os.system('cls')
    print(Fore.GREEN + '''
1) ADD
2) TIMES
3) DEVIDE
4) SUBTRACT
5) EXIT       
''')
    
def add():
    os.system('cls')
    number1 = int(input(Fore.GREEN + "Enter Fisrt Number: "))
    number2 = int(input(Fore.GREEN + "Enter Second Number: "))

    if number1 == number1 and number2 == number2:
        os.system('cls')
        print(Fore.BLUE + "[+] YOUR ANSWER IS:")
        print(f"{number1 + number2}")
        print("")
        input(Fore.GREEN + "[+] Press Enter To Continue...")

def times():
    os.system('cls')
    number1 = int(input(Fore.GREEN + "Enter Fisrt Number: "))
    number2 = int(input(Fore.GREEN + "Enter Second Number: "))

    if number1 == number1 and number2 == number2:
        os.system('cls')
        print(Fore.BLUE + "[+] YOUR ANSWER IS:")
        print(f"{number1 * number2}")
        print("")
        input(Fore.GREEN + "[+] Press Enter To Continue...")

def devide():
    os.system('cls')
    number1 = int(input(Fore.GREEN + "Enter Fisrt Number: "))
    number2 = int(input(Fore.GREEN + "Enter Second Number: "))

    if number1 == number1 and number2 == number2:
        os.system('cls')
        print(Fore.BLUE + "[+] YOUR ANSWER IS:")
        print(f"{number1 / number2}")
        print("")
        input(Fore.GREEN + "[+] Press Enter To Continue...")

def sub():
    os.system('cls')
    number1 = int(input(Fore.GREEN + "Enter Fisrt Number: "))
    number2 = int(input(Fore.GREEN + "Enter Second Number: "))

    if number1 == number1 and number2 == number2:
        os.system('cls')
        print(Fore.BLUE + "[+] YOUR ANSWER IS:")
        print(f"{number1 - number2}")
        print("")
        input(Fore.GREEN + "[+] Press Enter To Continue...")

def option():
    while True:
        banner()
        choice = input(Fore.BLUE + "Enter Choice -> ")

        if choice == "1":
            add()
        elif choice == "2":
            times()
        elif choice == "3":
            devide()
        elif choice == "4":
            sub()
        elif choice == "5":
            break
        else:
            print(Fore.RED + "[-] INVALID OPTION!")
            time.sleep(1)

if __name__ == "__main__":
    option()