import sqlite3
from models import Box
from db.data_import import records



def create_db():
    db_connector = sqlite3.connect("./db/base1.db")
    # class box:
    return db_connector


def create_boxes_table(db_connector:sqlite3.Connection):
    try:
        db_cursor = db_connector.cursor()
        db_cursor.execute(
            """CREATE TABLE Boxes(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                weight REAL NOT NULL,
                width REAL NOT NULL,
                height REAL NOT NULL,
                length REAL NOT NULL,
                container_id INTEGER DEFAULT NULL,
                CONSTRAINT max_volume CHECK (width * length * height <= 50),
                CONSTRAINT max_weight CHECK (weight <= 50));"""
        )
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(f"Error: {err} creating Boxes table!")
        pass


# def create_containers_table(db_connector:sqlite3.Connection):
#     """creates the Freights Table"""
#     try:
#         db_cursor = db_connector.cursor()
#         db_cursor.execute(
#             """CREATE TABLE Containers(
#                 id INT PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 weight REAL,
#                 width REAL,
#                 height REAL,
#                 length REAL,
#                 container_id INT DEFAULT NULL);"""
#         )
#         db_cursor.close()
#     except sqlite3.OperationalError as err:
#         print(f"Error: {err} creating Boxes table!")
#         pass


# def create_freights_table(db_connector:sqlite3.Connection):
#     """creates the Freights Table"""
#     try:
#         db_cursor = db_connector.cursor()
#         db_cursor.execute(
#             """CREATE TABLE Freights(
#                 id INT PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 weight REAL,
#                 width REAL,
#                 height REAL,
#                 length REAL,
#                 container_id INT DEFAULT NULL);"""
#         )
#         db_cursor.close()
#     except sqlite3.OperationalError as err:
#         print(f"Error: {err} creating Boxes table!")
#         pass

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

def seed_db(db_conn):
    
    for record in records:
        del record["id"]
        del record["container_id"]
    boxes = [box.__dict__ for box in [Box(**record) for record in records]]
    add_boxes_to_db(boxes=boxes, db_connector=db_conn)

