import sqlite3
import atexit
from DAO import _Orders,_Supplier,_Hats
import sys

class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect(sys.argv[4])
        self.order = _Orders(self._conn)
        self.supplier = _Supplier(self._conn)
        self.hat = _Hats(self._conn)

    def init(self):
        self.__init__()
 
    def _close(self):
        self._conn.commit()
        #self._conn.close()

    def _executeOrder(self,hats_topping):
        #self.supplier.printTable()
        #self.hat.printTable()
        top=str(hats_topping)
        id=self.hat.findIdForOrder(top)
        self.hat.update(id)
        return id

    def myOrder(self,orderid):
        c=self._conn.cursor()
        c.execute("""
                SELECT hats.topping, suppliers.name, b.location 
                FROM ((SELECT hat, location FROM orders WHERE id = ? ) AS b JOIN
                    hats ON hats.id=b.hat
                    ) AS a JOIN suppliers ON a.supplier=suppliers.id
            """,[orderid])
        return c.fetchone()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE hats (
            id      INT     PRIMARY KEY,
            topping TEXT    NOT NULL,
            supplier    INT,
            quantity    INT NOT NULL,
            FOREIGN KEY(supplier)  REFERENCES supplier(id)
        );

        CREATE TABLE suppliers (
            id      INT     PRIMARY KEY,
            name TEXT    NOT NULL
        );

        CREATE TABLE orders (
            id      INT     PRIMARY KEY,
            location TEXT    NOT NULL,
            hat    INT,
            FOREIGN KEY(hat)  REFERENCES hats(id)
        );
    """)
 
# the repository singleton
repo = _Repository()
atexit.register(repo._close)
