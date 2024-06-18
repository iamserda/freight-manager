""" User Interface: prints menu full options to end user. """
def show_app_menu():
    """menu: a menu to be displayed"""
    menu = """MENU:
    1. Add box type
    2. Show box types
    3. Load box into a given container
    4. Show Containers
    5. Summary Report
    x. Close Menu\n
    $: """
    
    valid_option = range(1, 6)
    choice = input(menu).strip()
    if choice.casefold() == "x":
        print("Terminating application at user's request...")
        return False
    if int(choice) not in valid_option:
        print(f"Selection-Error: {choice} is NOT a valid option. Please see the menu and try again!")
        return True
    return int(choice)
