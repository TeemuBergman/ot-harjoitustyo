""" db.py

    This is where all the SQLite magic happens.
    """

import sqlite3
from sqlite3 import Error


class Database(object):
    """sqlite3 database entities that holds testers jobs"""
    DB_LOCATION = r"./db/players.db"

    def __init__(self):
        """Initialize db entities variables"""
        self.connection = sqlite3.connect(Database.DB_LOCATION)
        self.cur = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def executemany(self, many_new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cur.executemany('REPLACE INTO jobs VALUES(?, ?, ?, ?)', many_new_data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS jobs(title text, \
                                                            job_id integer PRIMARY KEY, 
                                                            company text,
                                                            age integer)''')

    def commit(self):
        """commit changes to database"""
        self.connection.commit()


def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, command):
    """Execute given command on database."""
    try:
        c = conn.cursor()
        c.execute(command)
    except Error as e:
        print(e)


def build_database():
    """Create Players database and its tables."""
    database = r"./db/players.db"

    sql_create_main_table = """ CREATE TABLE IF NOT EXISTS main (
                                        account_id integer PRIMARY KEY,
                                        player_id integer NOT NULL,
                                        bank_account_id integer NOT NULL
                                    ); """

    sql_create_players_table = """ CREATE TABLE IF NOT EXISTS players (
                                        player_id integer PRIMARY KEY,
                                        player_name text NOT NULL,
                                        password text NOT NULL,
                                        FOREIGN KEY (player_id) REFERENCES main (player_id)
                                    ); """

    sql_create_bank_table = """CREATE TABLE IF NOT EXISTS bank (
                                    bank_account_id integer PRIMARY KEY,
                                    balance integer NOT NULL,
                                    FOREIGN KEY (bank_account_id) REFERENCES main (bank_account_id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_main_table)
        create_table(conn, sql_create_players_table)
        create_table(conn, sql_create_bank_table)
    else:
        print("Error! cannot create the database connection.")
