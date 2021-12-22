import database_connection as conn


def create_user_table():
    return """CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            firstName TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            dateOfBirth NOT NULL,
            gender NOT NULL,
            height NOT NULL,
            nutrient_data TEXT DEFAULT "",
            update_timestamp DATE DEFAULT CURRENT_TIMESTAMP
            )"""


def create_weight_table():
    return """CREATE TABLE IF NOT EXISTS Weights (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            weight REAL,
            weight_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users (id) 
            )"""

class DatabaseTools:
    def __init__(self):
        self.connection = conn.return_connection()
        self.cur = self.connection.cursor()

    def check_email(self, email, password):
        return self.cur.execute("SELECT email FROM Users WHERE email=? AND password=?", (email, password)).fetchone()

    def check_password(self, email, password):
        return self.cur.execute("SELECT password FROM Users WHERE email=? AND password=?", (email, password)).fetchone()

    def check_email_available(self, email):
        return self.cur.execute("SELECT email FROM Users Where email=?", (email,)).fetchone()

    def fetch_user_info(self, email):
        return self.cur.execute("SELECT * FROM Users Where email=?", (email,)).fetchone()

    def fetch_updatedate(self, email):
        return self.cur.execute("SELECT update_timestamp FROM Users WHERE email=?", (email,)).fetchone()[0]

    def insert_weight(self, email, weight):
        self.cur.execute(
            "INSERT INTO Weights (user_id, weight) VALUES ((SELECT id FROM Users WHERE email=?), ?)", (email, weight))
        self.connection.commit()

    def delete_weight(self, email):
        self.cur.execute(
            "DELETE FROM Weights WHERE id = (SELECT id FROM Weights WHERE user_id=(SELECT id FROM Users WHERE email=?) ORDER BY weight_timestamp DESC LIMIT 1)", [
                email]
        )
        self.connection.commit()

    def update_updatadate(self, email, update_date):
        self.cur.execute(
            "UPDATE Users SET update_timestamp=? WHERE email=?", (email, update_date))
    
    def update_nutrientdata(self, email, nutrient_data):
        self.cur.execute(
            "UPDATE Users nutrient_data=? WHERE email=?", (email, nutrient_data))

    def fetch_weight(self, email):
        return self.cur.execute(
            "SELECT weight FROM Users LEFT JOIN Weights ON Users.id = Weights.user_id WHERE email = ? ORDER BY weight_timestamp DESC LIMIT 1", [
                email]
        ).fetchone()[0]

    def fetch_all_from_weights(self, email):
        return self.cur.execute(
            "SELECT weight, strftime('%d.%m.%Y ', weight_timestamp) FROM Users LEFT JOIN Weights ON Users.id = Weights.user_id WHERE email = ? ORDER BY weight_timestamp", [
                email]
        ).fetchall()

    def update_password(self, email, password, newPassword):
        self.cur.execute(
            "UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password))
        self.connection.commit()

    def delete_user(self, email, password):
        self.cur.execute(
            "DELETE FROM Users WHERE email=? AND password=?", (email, password))
        self.connection.commit()

    def create_user(self, firstName, surname, email, password, dateOfBirth, gender=None, height=None):
        self.cur.execute("""INSERT INTO Users (firstName, surname, email, password, dateOfBirth, gender, height) 
                         VALUES (?, ?, ?, ?, ?, ?,?)""", (firstName, surname, email, password, dateOfBirth, gender, height))
        self.connection.commit()

    def _database_drop_it(self):
        self.cur.execute("DROP TABLE IF EXISTS Users")
        self.cur.execute("DROP TABLE IF EXISTS Weights")
        self.connection.commit()

    def _database_create_tables(self):
        self.cur.execute(create_user_table())
        self.cur.execute(create_weight_table())
        self.connection.commit()

    def database_init(self):
        self._database_drop_it()
        self._database_create_tables()
