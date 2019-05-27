import sqlite3

class Database:

    # This used to be the 'connect' method.
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        # got rid of the line below because I want the connection to the db to stay open for all future methods
        # conn.close()

    def insert(self,title,author,year,isbn):
        # deleted the connection to each method because using the __init__ one for all others instead.
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        # got rid of the line below on each method because I will close the db when I close the program.
        # self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title =? OR author =? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?" ,(title,author,year,isbn,id))
        self.conn.commit()

    # this method closes the connection to the db when closing the program.
    def __del__(self):
        self.conn.close()



# insert("Star Wars","George Lucas",1977,12649716)
# update(5,"I JUST CHANGED THE TITLE","ME",2019,62189756)
# print(view())
# print("***********")
