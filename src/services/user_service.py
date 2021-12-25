import string
import re
from repositories.user_repository import DatabaseTools


class UserService:
    def __init__(self):
        """Luokka instanssi, joka käsittelee käyttäjän haluamia toiminnallisuuksia, kuten salasanan vaihtamista.
        """
        self._datatools = DatabaseTools()
        self._password1 = None
        self._password2 = None
        self._email = None
        self._password = None

    def user_delete(self, email, password):
        """Metodi, joka poistaa käyttäjän.

        Args:
            email (String): Käyttäjän sähköposti
            password (String): Käyttäjän salasana
        """
        fun_email = email
        fun_password = password
        self._datatools.delete_user(fun_email, fun_password)

    def change_password(self, in_email, password, in_password1, in_password2):
        """Metodi, jonka avulla voidaan vaihtaa käyttäjän salasana"""
        self._password1 = in_password1
        self._password2 = in_password2
        email = in_email
        self._password = password

        if self._password1 == self._password2 and self._password1 not in ([None], ""):
            self._datatools.update_password(
                email,  self._password, self._password2)
            return True
        return False

    def gender_check(self, gender):
        """Tarkistaa, että käyttäjä on syöttänyt sukupuolen.

        Args:
            gender (String): käyttäjän sukupuoli

        Returns:
            Boolean: Palauttaa True, jos sukupuoli on ilmoitettu.
        """
        var = bool(gender in ("male", "female"))
        return var

    def name_check(self, name):
        """Tarkistaa, että etunimi ja sukunimi syötteet ovat oikein.

        Args:
            name (String): joko etunimi tai sukunimi

        Returns:
            Boolean: Jos nimi koostuu akkosista, niin palauttaa True.
        """
        error = True
        letters = string.ascii_letters + " "
        for i in name:
            if i not in letters:
                error = False
        if name is None or error is False or name == "":
            error = False
        return error

    def fetch_weights_to_frame(self, email):
        """Memotid, joka vastaanottaa DatabaseTools-oliolta
        käyttäjän painot, joita käsittelee ja välittää eteenpäin.

        Args:
            email (String): Käyttäjän sähköpostiosoite

        Returns:
            Tuple: Palauttaa monikkon, jonka sisällä on paino- ja päivämäärä-lista.
        """
        weight_list = []
        date_list = []
        datacontent = self._datatools.fetch_all_from_weights(email)
        for row in datacontent:
            weight_list.append(row[0])
            date_list.append(row[1])
        return (weight_list, date_list)

    def email_check(self, in_email):
        """Funktio, joka tarkistaa, että sähköpostia ei ole olemassa
        ja sähköpostiosoitteen formaatti on oikein.

        Args:
            in_email: Käyttäjän sähköpostiosoite

        Returns:
            Boolean: Palauttaa False, jos formaatti on oikein.
        """
        email = in_email
        error = False
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)) is not None:
            email_available = self._datatools.check_email_available(
                email)
            var = bool(email_available in ([None]))
            return var
        return error

    def password_check(self, password1, password2):
        if password1 == password2:
            var = bool("" not in (password1, password2))
            return var
        return None

    def check_height_digit(self, height):
        error = True
        new_height = height
        dig = string.digits + "."
        for i in height:
            if i not in (dig):
                error = False
        if error is False or new_height is None or new_height == "":
            return False
        error = self._check_value_type(new_height)
        return error

    def _check_value_type(self, height):
        new_height = height
        error = True
        try:
            new_height = float(height)
            if 0.0 > new_height < 400.0:
                error = False
        except ValueError:
            pass
        return error
