from os import remove
import sqlite3

class database ():
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
        if data.task is None and data.done is None:
            return -2
        query = 'UPDATE tasks SET'
        args = ()
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

db = database()