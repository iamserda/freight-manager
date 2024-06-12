""" User Interface: prints menu full options to end user. """
def show_app_menu():
    """
menu: a menue to be displayed until user terminates
-- 1. add box type
-- 2. Show box types
-- 3. Load box into a given container
-- 4. Show Containers
-- 5. Summary Report
-- x. Close Menu
"""
    menu = """
    MENU:
1. Add box type
2. Show box types
3. Load box into a given container
4. Show Containers
5. Summary Report
x. Close Menu\n
$: """

    choice = input(menu).strip()
    if choice.casefold() == "x":
        print("Terminating application at user's request...")
        return False
    if choice not in ["1","2","3","4","5"]:
        print(f"Selection-Error: {choice} is NOT a valid option. Please see the menu and try again!")
    else:
        print(f"Selected option: {choice}")
    return True
