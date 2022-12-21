import modules.module1 as deobfuscator1
import os


class colors:
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    printTitle()
    printOption(1, "https://development-tools.net/python-obfuscator/process DEOBFUSCATOR")
    printOption(2, "Exit")
    x = input(f"[{colors.YELLOW}>{colors.RED}] ")
    handleInput(x)

def printTitle():
    os.system("cls")
    title = [
" ______   _______  _______  ______   _______          ",
"(  __  \ (  ____ \(  ___  )(  ___ \ (  ____ \|\     /|",
"| (  \  )| (    \/| (   ) || (   ) )| (    \/| )   ( |",
"| |   ) || (__    | |   | || (__/ / | (__    | |   | |",
"| |   | ||  __)   | |   | ||  __ (  |  __)   | |   | |",
"| |   ) || (      | |   | || (  \ \ | (      | |   | |",
"| (__/  )| (____/\| (___) || )___) )| )      | (___) |",
"(______/ (_______/(_______)|/ \___/ |/       (_______)",                                           
    ]
    for line in title:
        print(f"{colors.RED}", end="")
        centerText(line)

def centerText(text):
    size = text.__len__()
    consoleWidth = os.get_terminal_size().columns
    spaces = (consoleWidth - size) / 2
    for i in range(int(spaces)):
        print(" ", end="")
    print(text)

def printOption(num,option):
    print(f"{colors.RED}[{colors.YELLOW}{num}{colors.RED}] {option}")
    
    
    
def handleInput(x):
    if x == "1":
        magic = input("[*] Magic: ")
        love = input("[*] Love: ")
        god = input("[*] God: ")
        destiny = input("[*] Destiny: ")
        type1 = deobfuscator1.Deobfuscator(magic,love,god,destiny)
        type1.run()
    if x == "2":
        exit(0)
    else:
        main()
if __name__ == "__main__":
    main()
    
    
    