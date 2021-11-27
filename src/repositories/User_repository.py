import database_connection as conn


class DatabaseTools:
    def __init__(self):
        self.cur = conn.return_connection().cursor()
        self.connection = conn.return_connection()

    def check_Email(self, email, password):
        return self.cur.execute("SELECT email FROM Users WHERE email=? AND password=?", (email, password)).fetchone()

    def check_Password(self, email, password):
        return self.cur.execute("SELECT password FROM Users WHERE email=? AND password=?", (email, password)).fetchone()

    def check_email_available(self, email):
        return self.cur.execute("SELECT email FROM Users Where email=?", (email,)).fetchone()

    def update_password(self, email, password, newPassword):
        self.cur.execute(
            "UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password))
        self.connection.commit()

    def update_height(self, email, height):
        self.cur.execute(
            "UPDATE Users SET height=? WHERE email=?", (height, email))
        self.connection.commit()

    def delete_user(self, email, password):
        self.cur.execute(
            "DELETE FROM Users WHERE email=? AND password=?", (email, password))
        self.connection.commit()

    def create_user(self, firstName, surname, email, password, dateOfBirth, sex=None, height=None):
        self.cur.execute("""INSERT INTO Users (firstName, surname, email, password, dateOfBirth, sex, height) 
                         VALUES (?, ?, ?, ?, ?, ?,?)""", (firstName, surname, email, password, dateOfBirth, sex, height))
        self.connection.commit()
