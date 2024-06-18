import os
from dotenv import load_env
from models import Box
from display_menu import show_app_menu
from db.handlers import create_db,create_table
from db.handlers import insert_box, insert_boxes, seed_boxes_table
from db.handlers import insert_freight, insert_freights, seed_freights_table
from boxes_functions import get_box_info, show_box_types
from db.data import boxes_records as records

load_env()

def insert_new_box(db_connection):
    new_box = get_box_info()
    try:
        insert_box(new_box,db_connection)
    except Exception as err:
        print(f"An error occurred while inserting new_box into the database!\nError: {err}.")

def show_boxes(db_connection):
    for box in show_box_types(db_connection):
        print(box)

def load_container(db_connection):
    print("in load containers")

def show_containers(db_connection):
    print("in show containers")

def show_summary_report(db_connection):
    print("in show summary reports")


def handle_choice(num, db_connection):
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

if __name__ == "__main__":
    # creates db, returns connection obj.
    db_connection = create_db()
    # create_table(db_connector=db_conn, sql_="boxes")
    # create_table(db_connector=db_conn, sql_="freights")
    # boxes = [Box(**record) for record in records]
    # boxes = [{**box.__dict__, "container_id": 1}for box in boxes]
    # seed_boxes_table(boxes, db_conn)
    # seed_boxes_table()
    flag = True
    while flag:
        flag = show_app_menu()
        if str(flag) == "True":
            continue
        elif flag in {1,2,3,4,5}:
            handle_choice(flag, db_connection)
    
    db_connection.close()
