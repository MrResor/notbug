from os import remove
import sqlite3

class Database ():
    """ Simple class holding sqlite3 database connection.\n

        Arguments:\n
        db_name - Holds database filename.\n
        con     - Connection to the database.\n
        cur     - Holds cursor used to execute the commands.\n

        Methods:\n
        __setup - Creates connection and cursor for the class.\n
        add     - Adds new task to the database.\n
        delete  - Deletes a task from the database.\n
        mock    - Restores the database to it's initial state.\n
        show    - Shows either one or all tasks, depends on the value of parameter it receives.\n
        update  - Updates a task in the database.s
    """
    
    def __init__(self):
        self.db_name = 'todo.db'
        self.__setup()

    def __setup(self):
        """ Creates sqlite3 connection and cursor, exists because the functionallity is needed twice in the
            program.
        """
        self.con = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def add(self, msg: str, done: bool):
        """ Add new task.
        """
        self.cur.execute('INSERT INTO tasks VALUES(NULL, ?, ?)', (msg, done))
        self.con.commit()

        return self.cur.lastrowid


    def delete(self, id: int):
        """ Delete a task.
        """
        self.cur.execute('DELETE FROM tasks WHERE rowid=?', (id, ))
        self.con.commit()
        if self.cur.rowcount:
            return 0
        else:
            return -1

    def mock(self):
        """ Function that is meant to reset the database to the initial state.
        """
        self.con.close()

        try:
            remove("todo.db")
        except OSError:
            pass

        self.__setup()

        self.cur.execute('CREATE TABLE tasks(id INTEGER PRIMARY KEY, msg TEXT, done INTEGER)')
        self.con.commit()

        # mock data values
        data = [
            ("Laundry", 0),
            ("Shopping", 1),
            ("Workout", 0),
            ("Vacuming", 1),
            ("Doctor's appointment", 0)
        ]

        self.cur.executemany('INSERT INTO tasks VALUES(NULL, ?, ?)', data)
        self.con.commit() 

    def show(self, id: int | None):
        """ Based on the presence of id, returns list of all tasks or a particular task.
        """
        if id is not None:
            res = self.cur.execute('SELECT * FROM tasks WHERE id = ?', (id, ))
            res = [res.fetchone()]
        else:
            res = self.cur.execute('SELECT * FROM tasks')
            res = res.fetchall()
        return res

    def update(self, id: int, data: dict):
        """ Tries to update the task in the database. If the "task" and "done" keys in the dict are both
            equal to None, it means no data to update was passed. 
        """
        # if both are None, it means that no needed data was sent in request
        if data.task is None and data.done is None:
            return -2
        query = 'UPDATE tasks SET'
        args = ()
        # if parameter was passed add it to the query and update args
        if data.task is not None:
            query += ' msg = ?'
            args = (*args, data.task)
        if data.done is not None:
            query += ',' * (1 if data.task else 0) + ' done = ?'
            args = (*args, data.done)
        query += ' WHERE id = ?'
        args = (*args, id)
        self.cur.execute(query, args)
        self.con.commit()
        if self.cur.rowcount:
            return 0
        else:
            return -1

db = Database()