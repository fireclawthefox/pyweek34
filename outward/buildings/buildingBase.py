
class BuildingBase:
    def __init__(self, csv_data_dict):
        self.csv_data_dict = csv_data_dict

        # building general details
        self.building_id = self.csv_data_dict["id"]
        self.name = self.csv_data_dict["name"].replace("\\n", "\n")
        self.tooltip = self.csv_data_dict["tooltip"].replace("\\n", "\n")
        self.required_ore = self.get_csv_value_int("required_ore")
        self.image = self.csv_data_dict["image"]
        self.build_time_m = self.get_csv_value_float("build_time_m")

        # affected economy stats
        self.food_production = self.get_csv_value_int("food_production")
        self.water_production = self.get_csv_value_int("water_production")
        self.general_goods_production = self.get_csv_value_int("general_goods_production")
        self.ore_production = self.get_csv_value_int("ore_production")
        self.population = self.get_csv_value_int("population")
        self.defense_strength = self.get_csv_value_int("defense_strength")

    def get_csv_value_float(self, value):
        return float(self.csv_data_dict[value])

    def get_csv_value_int(self, value):
        return int(self.csv_data_dict[value])
