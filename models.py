from typing import Any


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
    
    def add_to_container(self, container_id:int):
        self.container_id = container_id

# class Freight:
#     """ Freight class, Freights contain Container Objects"""
#     def __init__(self):
#         self. freight_id = None,
#         self.containers_id = set()
#         self.box_id = set(),
#         # self.from_location = None
#         # self.to_location = None
        
#     def __setattr__(self, name: str, value: Any) -> None:
#         pass
    
#     def set_freight_id(self, freight_id):
#         self.freight_id = freight_id
#         return True
    
#     def get_freight_id(self):
#         return self.freight_id
    
#     def set_containers_id(self, container_id):
#         if container_id not in self.containers_id:
#             self.containers_id.add(container_id)
#             return True
#         else:
#             print(f"ContainerID: {container_id} is already on this frieght.")
    
#     def remove_container(self, container_id):
#         if container_id not in self.containers_id:
#             print(f"ContainerID: {container_id} is already on this frieght.")
#         else:
#             self.containers_id.remove(container_id)
#             return True
    
#     def get_containers(self):
#         return tuple(self.containers_id)


# class Container:
#     """ Container class, containers contain boxes"""
#     def __init__(self,):
#         self.id = id
#         self.storage = []
#         self.full = False
    
#     def __str__(self) -> str:
#         return f"ContainerID: {self.id}."
    
#     def load_box(self, box:Box):
#         if self.is_full:
#             print("This container is full!")
#         else:
#             self.storage.append(box)
    
#     def unload(self):
#         self.storage = []
        
#     def is_full(self):
#         return self.full
