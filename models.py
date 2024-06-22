import sqlite3

class Box:
    def __init__(self, name:str=None, width:float=0, length:float=0 , height:float=0, weight:float=0):
        self.id:int = None
        self.name:str = name
        self.weight:float = weight
        self.width:float = width
        self.length:float = length
        self.height:float = height
        self.container_id:int = None

    def __str__(self) -> str:
        return f"name: {self.name}, dimensions:{self.width} in. x {self.length} in. x {self.height} in."

    def create(self, db_connection:sqlite3.Connection):
        """Saves this box's instance data into the database"""
        sql_statement = "INSERT INTO boxes VALUES(:id, :name, :weight, :width, :length, :height, :container_id)"
        try:
            db_cursor = db_connection.cursor()
            db_cursor.execute(sql_statement, self.__dict__)
            db_connection.commit()
            db_cursor.close()
        except sqlite3.OperationalError as err:
            raise err
        except sqlite3.IntegrityError as err:
            raise err
    
    def update(self, db_connection:sqlite3.Connection):
        """Saves this box's instance data into the database"""
        sql_statement = """
        UPDATE boxes
        SET(:id, :name, :weight, :width, :length, :height, :container_id)
        WHERE(id={})"""
        try:
            db_cursor = db_connection.cursor()
            db_cursor.execute(sql_statement.format(self.id), self.__dict__)
            db_connection.commit()
            db_cursor.close()
        except sqlite3.OperationalError as err:
            raise err
        except sqlite3.IntegrityError as err:
            raise err
    
    def set_container_id(self, container_id:int):
        self.container_id = container_id
    
    def calculate_box_volume(self):
        if self.width > 0 and self.height > 0 and self.length > 0:
            return float(self.width * self.height * self.length)


class Freight:
    """ Freight class, Freights contain Container Objects"""
    def __init__(self):
        self. freight_id = None,
        self.containers_id = set()
        self.box_id = set(),
        # self.from_location = None
        # self.to_location = None
        
    def __setattr__(self, name: str, value) -> None:
        pass
    
    def set_freight_id(self, freight_id):
        self.freight_id = freight_id
        return True
    
    def get_freight_id(self):
        return self.freight_id
    
    def set_containers_id(self, container_id):
        if container_id not in self.containers_id:
            self.containers_id.add(container_id)
            return True
        else:
            print(f"ContainerID: {container_id} is already on this frieght.")
    
    def remove_container(self, container_id):
        if container_id not in self.containers_id:
            print(f"ContainerID: {container_id} is already on this frieght.")
        else:
            self.containers_id.remove(container_id)
            return True
    
    def get_containers(self):
        return tuple(self.containers_id)


class Container:
    """ Container class, containers contain boxes"""
    def __init__(self):
        self.id = id
        self.loaded_boxes_id = []
        self.max_boxes = 10
        self.available_space = 300
        self.is_full = False
    
    def __str__(self) -> str:
        return f"ContainerID: {self.id} has includes {self.loaded} boxes aboard. {self.get_status()}"
    
    def save(self, db_conn=sqlite3.Connection):
        """Save instance into database"""
        sql_statement = """
        INSERT INTO containers 
        VALUES(:id, )"""
    
    def load_box(self, box:Box, db_path:str="db/base1.db", db_connection:sqlite3.Connection=None):
        if self.is_full:
            print(self.get_status)
            return
        try:

            if db_connection is None:
                db_connection = sqlite3.Connection(db_path)
                db_connection.execute("INSERT INTO boxes VALUES(:id,:name,:weight,:length,:width,:height,:container)", box.__dict__)
                self.storage.append(box.id)
        except sqlite3.DatabaseError as db_error:
            print(f"An error occurred! See [{db_error}]")
    
    def unload(self):
        self.loaded_boxes_id = []
        self.max_boxes = 10
        self.available_space = 300
        self.is_full = False
    
    def set_full_status(self):
        self.is_full = len(self.load_box) >= 30
    
    def get_status(self):
        """Returns a string, either 'Container is full!' or 'Container has cargo space available!'"""
        return "Container is full!" if self.is_full() else "Container has cargo space available!"

