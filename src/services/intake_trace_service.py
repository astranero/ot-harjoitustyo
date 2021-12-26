import services.calculator_service as calculator


class IntakeTrace:
    """Luokka, joka käsittelee käyttäjän päivän aikana syömää proteiini-
    , hiilihydraatti- ja rasvamäärää sekä
    palauttaa niiden perusteella lasketun kalorimäärän.
    """

    def __init__(self):
        """Luokan konstruktori, jolla alustetaan Intake-olio.
        """
        self._protein = 0
        self._carbohydrates = 0
        self._fat = 0
        self.counter = calculator.Calculator()

    def set_protein(self, protein_gram):
        """Metodi, jonka avulla muutetaan proteiinin arvo.

        Args:
            protein_gram (liukuluku): Muutettava proteiinin määrä grammoina.
        """
        self._protein += protein_gram
        self._protein = max(self._protein, 0)

    def get_protein(self):
        """Metodi, joka palauttaa proteiinimäärän

        Returns:
            Liukulukuarvo: Palauttaa proteiinimäärän grammoina.
        """
        return self._protein

    def set_carbohydrates(self, carbohydrates_gram):
        self._carbohydrates += carbohydrates_gram
        self._carbohydrates = max(self._carbohydrates, 0)

    def get_carbohydrates(self):
        return self._carbohydrates

    def set_fat(self, fat_gram):
        self._fat += fat_gram
        self._fat = max(self._fat, 0)

    def get_fat(self):
        return self._fat

    def _total_calorie_intake(self):
        """Laskee käyttäjän syöttämien ravinto-aineiden kalorimäärän.

        Returns:
            Liukuluku: Palauttaa kalorimäärän.
        """
        protein_calories = self.counter.protein_calorie_count(self._protein)
        carbohydrate_calories = self.counter.carbohydrates_calorie_count(
            self._carbohydrates)
        fat_calories = self.counter.fat_calorie_count(self._fat)
        return protein_calories + carbohydrate_calories + fat_calories

    def __str__(self):
        return f"""Protein: {self._protein}g
        | Carbohydrates: {self._carbohydrates}g
        | Fat: {self._fat}g
        | Total Calories: {self._total_calorie_intake()}"""
