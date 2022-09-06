import random

class EventBase:
    def __init__(self, csv_data_dict):
        self.csv_data_dict = csv_data_dict

    def do(self, economy_stats_list):
        stats_list = economy_stats_list
        if self.csv_data_dict["randomAffect"] == 1:
            stats_list = [random.choice(economy_stats_list)]

        for stats in stats_list:
            if (self.get_csv_value_int("defensible")):
                if stats.defense_strength >= self.get_csv_value_int("strength"):
                    continue

            if stats.is_player_stats:
                base.messenger.send(
                    "event_happened",
                    [self.csv_data_dict["text"]])

            stats.population += self.get_csv_value_int("population")
            stats.food += self.get_csv_value_int("food")
            stats.water += self.get_csv_value_int("water")
            stats.general_goods += self.get_csv_value_int("general_goods")
            stats.defense_strength += self.get_csv_value_int("defense_strength")
            stats.ores += self.get_csv_value_int("ores")

            for i in range(self.get_csv_value_int("buildingsLost")):
                if len(stats.buildings) == 0:
                    break
                stats.remove_building(stats.buildings[-1])

            stats.evaluate()

    def get_csv_value_int(self, value):
        return int(self.csv_data_dict[value])
