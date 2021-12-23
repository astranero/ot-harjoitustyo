class Calculator:
    """Luokka, jonka avulla lasketaan kalorimäärät

        Attributes:
                self.__protein_calorie_per_gram:
                alustettu arvo yhden proteiinigramman kalorimäärästä.

                self.__carbohydrates_calorie_per_gram:
                alustettu arvo yhden hiilihydraattigramman kalorimäärästä.

                self.__fat_calorie_per_gram: alustettu arvo yhden rasvagramman kalorimäärästä.
    """

    def __init__(self):
        """ Luokan konstruktori, joka luo uuden laskimen.

            Args:
                self.self.__protein_calorie_per_gram: yhden gramman proteiinin kalorimäärä
                self.self.__carbohydrates_calorie_per_gram: yhden gramman hiilihydraatin kalorimäärä
                self.self.__fat_calorie_per_gram: yhden gramman rasvan kalorimäärä
        """

        self._protein_calorie_per_gram = 4
        self._carbohydrates_calorie_per_gram = 4
        self._fat_calorie_per_gram = 9

    def protein_calorie_count(self, protein_grams: int):
        """Laskee proteiinin kalorimäärän

            Args:
                protein_grams: Laskettavan proteiinin määrä grammoina.

            Returns:
                Kokonaislukuarvoisen proteiinin kalorimäärän.
        """

        protein_calories = self._protein_calorie_per_gram * \
            int(protein_grams)
        return protein_calories

    def carbohydrates_calorie_count(self, carbohydrates_grams: int):
        carbohydrates_calories = self._carbohydrates_calorie_per_gram * \
            int(carbohydrates_grams)
        return carbohydrates_calories

    def fat_calorie_count(self, fat_grams: int):
        fat_calories = self._fat_calorie_per_gram * int(fat_grams)
        return fat_calories

    def lean_body_mass_estimate(self, weight_kg=None, height_cm=None, gender=None):
        """Laskee arvion käyttäjän lihasmassasta painon, pituuden ja sukupuolen perusteella.

            Returns:
                liukuluvun, joka kertoo lihasmassan kilogrammoina.
        """
        if gender == "male":
            lean_body_mass_kg = 0.407 * weight_kg + 0.267 * height_cm - 19.2
        elif gender == "female":
            lean_body_mass_kg = 0.252 * weight_kg + 0.473 * height_cm - 48.3
        return lean_body_mass_kg

    def count_lean_body_mass_with_fatpercent(self, body_fat_percent, weight_kg):
        """Laskee lihasmassan käyttäjän rasvaprosentti osuuden ja painon perusteella.

            Returns:
                liukuluvun, joka kertoo lihasmassan kilogrammoina.
        """

        lean_body_mass_kg = weight_kg * ((100 - body_fat_percent)/100)
        return lean_body_mass_kg

    def bmr_count(self, lean_body_mass: float):
        """ Laskee päivittäisen lepoaikaisen energian kulutuksen lihasmassan perusteella.
            Returns:
                liukuluvun, joka kertoo päivittäisen lihaskulutuksen kilokaloreina.
                Mutta virhetilanteessa palauttaa virheen.
        """

        try:
            basal_metabolic_rate = 370 + (21.6*lean_body_mass)
            return basal_metabolic_rate
        except ValueError as error:
            return error

    def total_daily_energy_expenditure(self, bmr, activity_level):
        try:
            if activity_level == "Inactive":
                activity_multiplier = 1.2
            elif activity_level == "Low":
                activity_multiplier = 1.375
            elif activity_level == "Medium":
                activity_multiplier = 1.55
            elif activity_level == "Medium-high":
                activity_multiplier = 1.65
            elif activity_level == "High":
                activity_multiplier = 1.725
            elif activity_level == "Intense":
                activity_multiplier = 1.9
            elif activity_level == "None":
                activity_multiplier = 0
            total_daily_energy_expenditure = bmr * activity_multiplier
            return round(total_daily_energy_expenditure, 3)
        except ValueError as error:
            return error
