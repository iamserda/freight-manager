import sqlite3
import json
from display_menu import show_app_menu
from db_handlers import create_db,create_boxes_table
from models import Box







# # class container
# try:
    # db_cursor.execute(
    #     "CREATE TABLE containers"
    # )
    # # class order
    # db_cursor.execute(
    #     "CREATE TABLE orders"
    # )
# except sqlite3.OperationalError as err:
    # print(f"Error: {err} creating Boxes table!")
    # pass 


# # class freight
# try:
#     db_cursor.execute(
#         "CREATE TABLE freights"
#     )
# except sqlite3.OperationalError as err:
#     print(f"Error: {err} creating Boxes table!")
#     pass


# - load box into containers
# - see revenue, expense, projected profit

# MENU
# FLAG = True

# while FLAG:
#     FLAG = show_app_menu()


def add_box_to_db(box:Box, db_connector:sqlite3.Connection)->None:
    try:
        db_cursor = db_connector.cursor()
        statement = """
        INSERT INTO boxes 
        VALUES(:id, :name, :weight, :width, :length, :height, :container_id);
        """
        new_box = box.__dict__
        db_cursor.execute(statement, new_box)
        db_connector.commit()
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(err)
    except sqlite3.IntegrityError as err:
        print(err)

def add_boxes_to_db(boxes:list,db_connector:sqlite3.Connection)->None:
    try:
        db_cursor = db_connector.cursor()
        statement = """
        INSERT INTO boxes 
        VALUES(:id, :name, :weight, :width, :length, :height, :container_id);
        """
        db_cursor.executemany(statement, boxes)
        db_connector.commit()
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(err)
    except sqlite3.IntegrityError as err:
        print(err)

def seed_db(records, db_conn):
    for record in records:
        del record["id"]
        del record["container_id"]
    boxes = [box.__dict__ for box in [Box(**record) for record in records]]
    add_boxes_to_db(boxes=boxes, db_connector=db_conn)

if __name__ == "__main__":
    
    # creates db, returns connection obj.
    db_conn = create_db()

    #using connection obj
    create_boxes_table(db_connector=db_conn)
    # create_freights_table(db_connector=db_conn)
    # create_containers_table(db_connector=db_conn)
    # seed_db(records, db_conn)
    # create
    # run menu
    show_app_menu()

    db_conn.close()