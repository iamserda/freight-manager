import sqlite3
from models import Box


def create_db():
    """
    Creates database file if it does not exits,
    creates a connection to the database.
    return the newly created connection.
    """
    db_connection = sqlite3.connect("./db/base1.db")
    return db_connection


def create_table(db_connector: sqlite3.Connection, sql_: str):
    """Creates all tables for the app."""
    sql_statements = {
        "boxes": """
        CREATE TABLE Boxes(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        weight REAL NOT NULL,
        width REAL NOT NULL,
        height REAL NOT NULL,
        length REAL NOT NULL,
        container_id INTEGER NOT NULL DEFAULT 1 REFERENCES Containers(id) ON DELETE CASCADE,
        CONSTRAINT max_volume CHECK (width * length * height <= 50),
        CONSTRAINT max_weight CHECK (weight <= 50));""",
        
        "freights": """
        CREATE TABLE Freights(
        id INTEGER PRIMARY KEY,
        container_id INTEGER NOT NULL DEFAULT 1,
        box_id INTEGER NOT NULL REFERENCES boxes(id) ON DELETE CASCADE);""",
        
        "container_view": """
        CREATE VIEW IF NOT EXISTS containers
        as 
        select container_id, round(sum(width * length * height),2) as occupied_volume 
        from Freights f 
        left join Boxes b on f.box_id = b.id 
        group by container_id;
        """
    }

    try:
        db_cursor = db_connector.cursor()
        db_cursor.execute(f"DROP TABLE IF EXISTS {sql_};")
        db_cursor.execute(sql_statements[sql_])
        
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(f"Error: {err} creating {sql_} table!")


def insert_box(box:Box, db_connector: sqlite3.Connection) -> None:
    """Given a box as a dictionary, it adds a new box to the db.
    Prints any error to the console."""
    try:
        db_cursor = db_connector.cursor()
        statement = """
        INSERT INTO Boxes 
        VALUES(:id, :name, :weight, :width, :length, :height, :container_id);"""
        db_cursor.execute(statement, box.__dict__)
        db_connector.commit()
        db_cursor.close()
    except sqlite3.OperationalError as err:
        raise err
    except sqlite3.IntegrityError as err:
        raise err


def insert_boxes(boxes: list, db_connector: sqlite3.Connection) -> None:
    """Given an list of boxes, adds all these boxes to the table.
    If a box already exist, it prints out an error!"""
    try:
        db_cursor = db_connector.cursor()
        statement = """
        INSERT INTO Boxes 
        VALUES(:id,:name, :weight, :width, :length, :height, :container_id);
        """
        db_cursor.executemany(statement, boxes)
        db_connector.commit()
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(err)
    except sqlite3.IntegrityError as err:
        print(err)


def seed_boxes_table(records, db_conn):
    """
        Creates a list of dictionaries representing boxes,
        creates a list of Boxes objects,
        converts them to a dictionary, and add them to db.
    """
    try:
        insert_boxes(boxes=records, db_connector=db_conn)
    except Exception as err:
        print(f"Error: Attempt to seed db failed...\n{err}")
        raise err

def insert_freight(box:dict, db_connector: sqlite3.Connection) -> None:
    """Given a box as a dictionary, it adds a new box to the db.
    Prints any error to the console."""
    try:
        db_cursor = db_connector.cursor()
        statement = """
        INSERT INTO Freights VALUES(:id,:container_id, :box_id);"""
        db_cursor.execute(statement, box)
        db_connector.commit()
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(err)
    except sqlite3.IntegrityError as err:
        print(err)


def insert_freights(freights: list, db_connector: sqlite3.Connection) -> None:
    """Given an list of freights records, adds all these freights to the table.
    If a freight already exist, it prints out an error!"""
    try:
        db_cursor = db_connector.cursor()
        statement = """INSERT INTO Freights VALUES(:id,:container_id, :box_id);"""
        db_cursor.executemany(statement, freights)
        db_connector.commit()
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(err)
    except sqlite3.IntegrityError as err:
        print(err)


def seed_freights_table(freights:list, db_conn):
    """
        Creates a list of dictionaries representing boxes,
        creates a list of Boxes objects,
        converts them to a dictionary, and add them to db.
    """
    try:
        insert_freights(freights, db_connector=db_conn)
    except Exception as err:
        print(f"Error: Attempt to seed db failed...\n{err}")
        raise err

def show_box_types(box_type, db_conn:sqlite3.Connection):
    sql_statement = """SELECT * FROM boxes WHERE(:name)"""
    box_types_data = db_conn.execute(sql_statement, box_type).fetchall()
    return box_types_data