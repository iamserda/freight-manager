import sqlite3
import json
from display_menu import show_app_menu
from db_handlers import create_db,create_boxes_table,\
                        add_box_to_db, add_boxes_to_db\






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
    display_menu_flag = True
    while display_menu_flag:
        display_menu_flag = show_app_menu()
    
    # Use to seed DB first-time
    # seed_db(db_conn)
    
    db_conn.close()
    