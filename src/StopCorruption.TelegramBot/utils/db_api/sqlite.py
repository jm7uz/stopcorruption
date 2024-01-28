import sqlite3
class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        with self.connection as connection:
            cursor = connection.cursor()
            data = None
            cursor.execute(sql, parameters)

            if commit:
                connection.commit()
            if fetchall:
                data = cursor.fetchall()
            if fetchone:
                data = cursor.fetchone()

        return data

    # Create Users table
    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            fullname VARCHAR(255),
            telegram_id VARCHAR(30) UNIQUE,
            lang VARCHAR(3)
        );
        """
        self.execute(sql, commit=True)

    def create_table_complaints(self):
        sql = """
        CREATE TABLE Complaints (
            id INTEGER PRIMARY KEY,
            post_id INTEGER,
            user_id INTEGER,
            region VARCHAR(255),
            district VARCHAR(255),
            description TEXT,
            latitude long,
            longitude long,
            phone VARCHAR(30),
            status VARCHAR(20)
        );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self,fullname: str, telegram_id: str = None, lang: str = 'uz'):
        sql = """
        INSERT INTO Users(fullname,telegram_id, lang) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(fullname, telegram_id, lang), commit=True)

    def add_complaint(self, post_id, user_id, region, district, description, latitude, longitude, phone, status):
        sql = """
        INSERT INTO Complaints(post_id, user_id, region, district, description, latitude, longitude,  phone, status) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(post_id, user_id, region, district, description, latitude, longitude, phone, status), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)
    
    def select_all_complaints(self):
        sql = """
        SELECT * FROM Complaints
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    
    def select_complaint(self, **kwargs):
        sql = "SELECT * FROM Complaints WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
    
    def count_complaints(self):
        return self.execute("SELECT COUNT(*) FROM Complaints;", fetchone=True)
    
    def update_user_lang(self, lang, telegram_id):
        sql = f"""
        UPDATE Users SET lang=? WHERE telegram_id=?
        """
        return self.execute(sql, parameters=(lang, telegram_id), commit=True)
    
    def update_complaint_status(self, status, post_id):
        sql = f"""
        UPDATE Complaints SET status=? WHERE post_id=?
        """
        return self.execute(sql, parameters=(status, post_id), commit=True)
    
    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


