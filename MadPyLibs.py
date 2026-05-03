from colorama import init, Fore, Back, Style
init(autoreset=True)

def display_menu():
    print(Back.CYAN + Fore.MAGENTA + Style.BRIGHT + "\n=== MadPyLibs Game Menu ===")
    print(Style.BRIGHT + Fore.CYAN + "1. [The Heist]")
    print(Style.BRIGHT + Fore.MAGENTA + "2. [The Dating Profile]")
    print(Style.BRIGHT + Fore.BLUE + "3. [The Wilderness Survival]")
    print(Style.BRIGHT + Fore.GREEN + "4. [Exit]")
    choice = input(Style.BRIGHT + Back.RED + Fore.WHITE + "\nEnter your choice (1-4): ")
    return choice

def get_input(prompt):
    return input(Fore.CYAN + prompt + Style.RESET_ALL)

def the_heist():
    print(Fore.YELLOW + Style.BRIGHT + "\n--- The Heist ---\n" + Style.RESET_ALL)
    
    noun = get_input("Noun: ")
    time_of_day = get_input("Time of Day: ")
    building = get_input("Building: ")
    vehicle = get_input("Vehicle: ")
    article_of_clothing = get_input("Article of Clothing: ")
    adjective1 = get_input("Adjective: ")
    food = get_input("Food: ")
    nationality = get_input("Nationality: ")
    occupation = get_input("Occupation: ")
    ridiculous_name = get_input("Ridiculous Name: ")
    exotic_city = get_input("Exotic City: ")
    day_of_week = get_input("Day of Week: ")
    animal = get_input("Animal: ")
    kitchen_utensil = get_input("Kitchen Utensil: ")
    body_part = get_input("Body Part: ")
    insult = get_input("Insult: ")
    verb = get_input("Verb: ")

    story = f"\nIt was {time_of_day} when MadPyLibs pulled up to the {building} in a stolen {vehicle} wearing nothing but a {article_of_clothing} and a {adjective1} smile. The plan was simple: steal the world's largest {food}, fence it to a {nationality} {occupation} named {ridiculous_name}, and be in {exotic_city} by {day_of_week}. Everything went perfectly until a {animal} showed up armed with a {kitchen_utensil}. MadPyLibs looked it dead in the {body_part} and said, \"Not today, {insult}.\" Then they {verb}-ed into the sunset."

    print(Style.BRIGHT + Back.YELLOW + "\nYOUR HEIST STORY \n" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + story + Style.RESET_ALL)
    input(Fore.MAGENTA + "Press Enter to continue..." + Style.RESET_ALL)  

def the_dating_profile():
    """The Dating Profile Mad Lib story"""
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n--- The Dating Profile: Helping You FindLove ---\n" + Style.RESET_ALL)
    
    username = get_input("Name: ")
    age = get_input("Age (number): ")
    height_num = get_input("Height (number): ")
    unit = get_input("Unit of Measurement (ft, cm, etc): ")
    noun = get_input("Noun: ")
    verb1 = get_input("Verb: ")
    plural_noun = get_input("Plural Noun: ")
    adjective1 = get_input("Adjective: ")
    adjective2 = get_input("Adjective: ")
    num_pets = get_input("Number: ")
    animal = get_input("Animal: ")
    celebrity = get_input("Celebrity: ")
    weird_food = get_input("Weird Food: ")
    verb2 = get_input("Verb: ")

    story = f"\nUsername: {username} \nAge: {age}\nHeight: {height_num} {unit}\n\nBio: I enjoy long walks on the {noun}, {verb1}-ing competitively, and collecting rare {plural_noun}. My friends describe me as \"{adjective1}, but in a {adjective2} way.\" Looking for someone who won't judge me for my {num_pets} pet {animal}s or my obsession with {celebrity}. Must love {weird_food}. Swipe left if you can't handle someone who {verb2}s at the dinner table. IYKYK."

    print(Style.BRIGHT + Back.MAGENTA + "YOUR DATING PROFILE" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + story + Style.RESET_ALL)
    input(Fore.MAGENTA + "Press Enter to continue..." + Style.RESET_ALL)    

def main():
    while True:
        choice = display_menu()
        
        if choice == "1":
            the_heist()
        elif choice == "2":
            the_dating_profile()
        elif choice == "3":
            the_wilderness_survival()
        elif choice == "4":
            print(Fore.CYAN + Style.BRIGHT + "\nThanks for playing! Goodbye! 👋\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Please try again." + Style.RESET_ALL)
        
        play_again = input("\nWould you like to play another story? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()