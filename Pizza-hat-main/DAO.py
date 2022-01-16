from DTO import Orders,Supplier,Hats

class _Orders:
    def __init__(self,conn):
        self._conn=conn

    def insert(self,order):
        self._conn.execute("""INSERT INTO orders (id,location,hat) VALUES (?,?,?)""",[order.id,order.location,order.hat])     

    def find(self,order_id):
        c=self._conn.cursor()
        c.execute("""SELECT id, location, hat FROM orders WHERE id=?""",[order_id])
        return Orders(*c.fetchone())

    def findAll(self):
        c=self._conn.cursor()
        all=c.execute("""SELECT id, location, hat FROM orders""").fetchall()
        return [Orders(*row) for row in all]
 
 
class _Supplier:
    def __init__(self,conn):
        self._conn=conn

    def insert(self,supplier):
        self._conn.execute("""
                INSERT INTO suppliers (id,name) VALUES (?,?)
        """, [supplier.id,supplier.name])     

    def find(self,supplier_id):
        c=self._conn.cursor()
        c.execute("""
                SELECT id, name FROM suppliers WHERE id = ?
            """, [supplier_id])
        return Supplier(*c.fetchone())
    
    def printTable(self):
        c=self._conn.cursor()
        c.execute("""
                SELECT * FROM suplliers 
            """)
        row=c.fetchall()
        for line in row:
            print(line)

class _Hats:
    def __init__(self,conn):
        self._conn = conn

    def insert(self,hats):
        self._conn.execute("""
            INSERT INTO hats (id,topping,supplier,quantity) VALUES (?,?,?,?)
        """, [hats.id, hats.topping, hats.supplier, hats.quantity])  
        self.delete()

    def find(self, hats_id):
        c=self._conn.cursor()
        c.execute("""
                SELECT id, topping, supplier, quantity FROM hats WHERE id = ?
            """, [hats_id])
        return Hats(*c.fetchone())

    def findIdForOrder(self, hats_topping):
        c=self._conn.cursor()
        c.execute("""
                SELECT id FROM hats WHERE topping = ? ORDER BY supplier ASC LIMIT 1 
            """, [hats_topping])
        row=c.fetchone()[0]
        return (row)
    
    def selectHatsQuantity(self, hats_id):
        c=self._conn.cursor()
        c.execute("""
                SELECT quantity FROM hats WHERE id = ?
            """, [hats_id])
        row=c.fetchone()[0]
        return row

    def update(self, id):
        quantityToSet=int(self.selectHatsQuantity(id))-1
        self._conn.execute("""
               UPDATE hats SET quantity=(?) WHERE id = (?)
           """, [quantityToSet, id])
       # self.delete()

    def delete(self):
        self._conn.execute("""
                DELETE FROM hats WHERE quantity = (?)
            """, [0])

    def printTable(self):
        c=self._conn.cursor()
        c.execute("""
                SELECT * FROM hats 
            """)
        row=c.fetchall()
        for line in row:
            print(line)

      


        