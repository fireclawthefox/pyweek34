from dataclasses import dataclass, field

@dataclass
class EconomyStats:
    is_player_stats:bool = False

    population:int = 100
    food:int = 1000
    water:int = 1000
    general_goods:int = 1000
    ores:int = 50
    defense_strength:int = 20

    # production
    food_production:int = 0
    water_production:int = 0
    general_goods_production:int = 0
    ore_production:int = 0

    buildings:list[int] = field(default_factory=list)

    def get_strength(self) -> float:
        strength = self.population
        strength += self.food - self.population
        strength += self.water - self.population
        strength += self.defense_strength
        strength += self.general_goods - self.population
        strength += self.ores

        return strength

    def tick_stats_calculate(self):
        self.food += self.food_production
        self.water += self.water_production
        self.general_goods += self.general_goods_production
        self.ores += self.ore_production

        self.food -= self.population
        self.water -= self.population
        self.general_goods -= self.population

        if self.water < 0:
            self.population += self.water

        if self.food < 0:
            self.population += self.food

        if self.population < 0:
            self.population = 0

        self.evaluate()

    def evaluate(self):
        self.food = self.food if self.food >= 0 else 0
        self.water = self.water if self.water >= 0 else 0
        self.general_goods = self.general_goods if self.general_goods >= 0 else 0
        self.ores = self.ores if self.ores >= 0 else 0
        self.population = self.population if self.population >= 0 else 0
        self.defense_strength = self.defense_strength if self.defense_strength >= 0 else 0

    def get_building_counts(self):
        building_counts = {}
        for building in self.buildings:
            if building.building_id in building_counts:
                building_counts[building.building_id] += 1
            else:
                building_counts[building.building_id] = 1
        return building_counts

    def add_building(self, building):
        self.buildings.append(building)

        self.food_production += building.food_production
        self.water_production += building.water_production
        self.general_goods_production += building.general_goods_production
        self.ore_production += building.ore_production
        self.population += building.population
        self.defense_strength += building.defense_strength

    def remove_building(self, building):
        self.buildings.remove(building)

        self.food_production -= building.food_production
        self.water_production -= building.water_production
        self.general_goods_production -= building.general_goods_production
        self.ore_production -= building.ore_production
        self.population -= building.population
        self.defense_strength -= building.defense_strength

        if self.is_player_stats:
            base.messenger.send("remove_building_event", [building])
