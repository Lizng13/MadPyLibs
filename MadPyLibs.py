from colorama import init, Fore, Back, Style
init(autoreset=True)

print (Fore.GREEN + "Testing 123")

def display_menu():
    print(Back.CYAN + Fore.MAGENTA + Style.BRIGHT + "\n=== MadPyLibs Game Menu ===")
    print(Style.BRIGHT + Fore.CYAN + "1. [The Heist]")
    print(Style.BRIGHT + Fore.MAGENTA + "2. [The Dating Profile]")
    print(Style.BRIGHT + Fore.BLUE + "3. [The Wilderness Survival]")
    choice = input(Style.BRIGHT + Back.RED + Fore.WHITE + "\nEnter your choice (1-3): ")
    return choice

def main():
    while True:
        choice = display_menu()
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Invalid choice. Please try again.")
        
        play_again = input("\nWould you like to play another story? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()