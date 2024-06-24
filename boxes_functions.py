import random
import sqlite3
from models import Box

def get_box_weight():
    """Gets box weight from the user via the console"""
    flag = True
    print(f"IMPORTANT: Any box's weight less than 1lbs, well be set 1 lbs.")
    while flag:
        try:
            weight = input("Enter box's weight in lb: ")
            weight_num = float(weight)
            if weight_num < 0 or weight_num > 50:
                raise ValueError("Weight value cannot be less than 0lbs or more than 50lbs")
            return weight_num
        except ValueError as err:
            print(f"Error: You've enter a value that's not a number.\n{err}")
        except TypeError as err:
            raise err

def get_box_dimensions(side_name:str):
    """Gets box's dimension(width, length, height) from the user."""
    while True:
        try:
            side_measurement = float(input(f"Enter box's {side_name} in 'in': "))
            break
        except ValueError as err:
            print(err)
    return side_measurement

def get_box_info():
    """Get box name, weights, width, length, height from user via console."""
    new_box = Box()
    while True:
        new_box.name = input("Enter box's name: ")
        if len(new_box.name) >= 3:
            break
    new_box.weight = get_box_weight()
    new_box.width = get_box_dimensions("width")
    new_box.length = get_box_dimensions("length")
    new_box.height = get_box_dimensions("height")
    new_box.container_id = random.randint(1, 5)
    return new_box

def get_all_boxes(db_conn:sqlite3.Connection):
    """Getter: returns all boxes in the Boxes table."""
    sql_statement = """SELECT name, weight, width, length, height FROM boxes"""
    box_types_data = [zip(["name", "weight", "width", "length", "height"],item) for item in db_conn.execute(sql_statement).fetchall()]
    
    return [dict(item) for item in box_types_data]