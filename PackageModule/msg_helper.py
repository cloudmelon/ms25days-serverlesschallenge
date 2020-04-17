from pip._vendor.colorama import init, Fore

def display(message, is_waring=False):
    if is_waring: 
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)