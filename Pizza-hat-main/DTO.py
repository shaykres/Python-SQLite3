# Data Transfer Objects:
class Orders:
    def __init__(self,id,location,hat):
        self.id = id
        self.location = location
        self.hat = hat
     
class Supplier:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Hats:
    def __init__(self,id,topping,supplier,quantity):
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity