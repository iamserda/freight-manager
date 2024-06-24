
import json
import sqlite3
from dotenv import load_dotenv
from display_menu import show_app_menu
from db_handlers import create_db,create_table, seed_boxes_table, seed_freights_table
from db_handlers import insert_box, insert_boxes, insert_freight, insert_freights, get_container, show_box_by_name
from boxes_functions import get_box_info, get_all_boxes


load_dotenv()

def insert_new_box(db_connection:sqlite3.Connection):
    """ to-do: """
    new_box = get_box_info()
    try:
        insert_box(new_box,db_connection)
    except Exception as err:
        print(f"An error occurred while inserting new_box into the database!\nError: {err}.")

def show_boxes(db_connection:sqlite3.Connection):
    """ to-do: """
    for box in get_all_boxes(db_connection):
        print(box)

def load_container(db_connection:sqlite3.Connection):
    """ to-do: """
    # ask user for box name
    try:
        box_name = input("Please enter the name of the box:\n$: ")
        # confirm box's name exist in boxes table
        box:tuple = show_box_by_name(box_name, db_connection)
        # ask user for container_id
        container_id = int(input("Enter Container ID: "))
        # verify that container has enough space, max limit is 50
        my_container:tuple = get_container(container_id, db_connection)
        # assign container_id to the specified box
        if my_container[0][1] <= 50:
            insert_freight(box, db_connection)
        # reduce the container's volume by the box's volume
        #if any of the above fails, print the specific error
        # return to the menu.
    except LookupError as err:
        print(err)


def show_containers(db_connection):
    """ to-do: """
    print("in show containers")

def show_summary_report(db_connection):
    """ to-do: """
    print("in show summary reports")


def handle_choice(num:int, db_connection:sqlite3.Connection):
    """ App's main menu"""
    match num:
        case 1:
            return insert_new_box(db_connection)
        case 2:
            return show_boxes(db_connection)
        case 3:
            return load_container(db_connection)
        case 4:
            return show_containers(db_connection)
        case 5:
            return show_summary_report(db_connection)
        case 98:
            with open("./db/boxes.json", "r") as file:
                data = json.load(file)
                for each_row in data:
                    each_row["id"] = None
                    each_row["container_id"] = 0
                try:
                    seed_boxes_table(data, db_connection)
                    print("Success!")
                except Exception as err:
                    raise err
            return True
        case 99:
            with open("./db/freights.json", "r") as file:
                data = json.load(file)
                try:
                    seed_freights_table(data, db_connection)
                    print("Success!")
                except Exception as err:
                    raise err
            return True
        case _:
            return False

if __name__ == "__main__":
    # seed_table:
    
    # creates db, returns connection obj.
    db_connection = create_db()
    create_table(db_connector=db_connection, sql_="boxes")
    create_table(db_connector=db_connection, sql_="freights")
    create_table(db_connector=db_connection, sql_="container_view")
    user_selection = True
    while user_selection:
        user_selection = show_app_menu()
        handle_choice(num=user_selection, db_connection=db_connection)

    db_connection.close()
