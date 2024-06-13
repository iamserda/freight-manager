import sqlite3
from models import Box


def create_db():
    db_connector = sqlite3.connect("./db/base1.db")
    # class box:
    return db_connector


def create_table(db_connector: sqlite3.Connection, sql_: str):
    sql_statements = {
        "boxes": """CREATE TABLE Boxes(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            width REAL NOT NULL,
            height REAL NOT NULL,
            length REAL NOT NULL,
            container_id INTEGER NOT NULL REFERENCES Containers(id) ON DELETE CASCADE,
            CONSTRAINT max_volume CHECK (width * length * height <= 50),
            CONSTRAINT max_weight CHECK (weight <= 50));""",
        "freights": """CREATE TABLE Freights(
            id INTEGER PRIMARY KEY,
            container_id INTEGER NOT NULL,
            box_id INTEGER NOT NULL REFERENCES Boxes(id) On DELETE CASCADE);""",
        "containers": """CREATE TABLE Containers(
            id INTEGER PRIMARY KEY,
            container_id INTEGER NOT NULL,
            box_id INTEGER NOT NULL REFERENCES Boxes(id) On DELETE CASCADE);""",
        }

    try:
        print(sql_statements[sql_][:19])
        # db_cursor = db_connector.cursor()
        # db_cursor.execute(sql_statements[sql_])
        # db_cursor.close()
    except sqlite3.OperationalError as err:
        print(f"Error: {err} creating Boxes table!")

def add_box(box: Box.__dict__, db_connector: sqlite3.Connection) -> None:
    """Given a box as a dictionary, it adds a new box to the db.
    Prints any error to the console."""
    try:
        db_cursor = db_connector.cursor()
        statement = """INSERT INTO boxes VALUES(:id, :name, :weight, :width, :length, :height, :container_id);"""
        db_cursor.execute(statement, box)
        db_connector.commit()
        db_cursor.close()
    except sqlite3.OperationalError as err:
        print(err)
    except sqlite3.IntegrityError as err:
        print(err)


def add_boxes(boxes: list, db_connector: sqlite3.Connection) -> None:
    """Given an list of boxes, adds all these boxes to the table.
    If a box already exist, it prints out an error!"""
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


def seed_db(records:list, db_conn):
    """Creates a list of dictionaries representing boxes, creates a list of Boxes objects, converts them to a dictionary, and add them to db."""
    try:
        for record in records:
            del record["id"]
            del record["container_id"]
        boxes = [box.__dict__ for box in [Box(**record) for record in records]]
        add_boxes(boxes=boxes, db_connector=db_conn)
    except Exception as err:
        print(f"Error: Attempt to seed db failed...\n{err}")
        raise err
