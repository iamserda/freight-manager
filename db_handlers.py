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
        CREATE TABLE IF NOT EXISTS Boxes(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        weight REAL NOT NULL,
        width REAL NOT NULL,
        height REAL NOT NULL,
        length REAL NOT NULL,
        CONSTRAINT max_volume CHECK (width * length * height <= 50));
        """,
        
        "freights": """
        CREATE TABLE IF NOT EXISTS Freights (
            id INTEGER PRIMARY KEY,
            container_id INTEGER NOT NULL DEFAULT 1,
            box_id INTEGER NOT NULL,
            FOREIGN KEY(box_id) REFERENCES Boxes(id) ON DELETE CASCADE
        );
        """,
        
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
    except Exception as err:
        print(err)


def insert_box(box:Box, db_connector: sqlite3.Connection) -> None:
    """Given a box as a dictionary, it adds a new box to the db.
    Prints any error to the console."""
    try:
        db_cursor = db_connector.cursor()
        statement = """INSERT INTO Boxes VALUES(:id, :name, :weight, :width, :length, :height);"""
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
        statement = """INSERT INTO Boxes VALUES(:id,:name, :weight, :width, :length, :height);"""
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
        statement = """INSERT INTO Freights(container_id, box_id) VALUES(:container_id, :box_id);"""
        relevant_box_data = box["container_id"],box["id"]
        db_cursor.execute(statement, relevant_box_data)
        db_connector.commit()
        db_cursor.close()
        return 1
    except sqlite3.OperationalError as err:
        raise err
    except sqlite3.IntegrityError as err:
        raise err


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


def seed_freights_table(freights:list, db_conn)->None:
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

def show_box_by_name(name, db_conn:sqlite3.Connection)->tuple | None:
    """Getter: Returns a specific box from the database given a name as a tuple. If none is found, logs error, return None"""
    try:
        my_cursor = db_conn.cursor()
        sql_statement = """SELECT * FROM boxes WHERE(name=:name)"""
        box_data:tuple = my_cursor.execute(sql_statement,(name,)).fetchone()
        my_cursor.close()
        if box_data is None:
            raise LookupError(f"An item with name{box_data} was not found in our database.\n \
        #                     Please check the name and try agains")
        return box_data
    except sqlite3.Error as sql_err:
        print(sql_err) # fake logging
    except LookupError as err:
        print(err) # fake logging


def get_container(container_id, db_conn:sqlite3.Connection)->tuple | None:
    """Getter: Given a container ID, query the database for the specified container, returns related data. Returns None if not found."""
    try:
        db_cursor = db_conn.cursor()
        sql_statement = "SELECT * FROM containers WHERE(container_id=:container_id)"
        container:tuple = db_cursor.execute(sql_statement, (container_id,)).fetchone()
        db_cursor.close()
        if container is None:
            raise LookupError(f"A container with the following ID: '{container_id}' was NOT found in the database.")
        return container
    except Exception as err:
        raise err
