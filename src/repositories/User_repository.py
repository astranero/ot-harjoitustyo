from tkinter.messagebox import showinfo
import database_connection as conn


class DatabaseTools:
    def __init__(self):
        self.cur = conn.return_connection().cursor()
        self.connection = conn.return_connection()

    def check_email(self, email, password):
        return self.cur.execute("SELECT email FROM Users WHERE email=? AND password=?", (email, password)).fetchone()

    def check_password(self, email, password):
        return self.cur.execute("SELECT password FROM Users WHERE email=? AND password=?", (email, password)).fetchone()

    def check_email_available(self, email):
        return self.cur.execute("SELECT email FROM Users Where email=?", (email,)).fetchone()

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

    def fetch_weight(self, email):
        return self.cur.execute(
            "SELECT weight FROM Users LEFT JOIN Weights ON Users.id = Weights.user_id WHERE email = ? ORDER BY weight_timestamp DESC LIMIT 1", [
                email]
        ).fetchone()[0]

    def fetch_40_from_weights(self, email):
        return self.cur.execute(
            "SELECT weight, weight_timestamp FROM Users LEFT JOIN Weights ON Users.id = Weights.user_id WHERE email = ? ORDER BY weight_timestamp ASC LIMIT 40", [
                email]
        ).fetchall()

    def update_password(self, email, password, newPassword):
        try:
            self.cur.execute(
                "UPDATE Users SET password=? WHERE email=? AND password=?", (newPassword, email, password))
            self.connection.commit()
        except Exception as e:
            showinfo(f"{e}")

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
