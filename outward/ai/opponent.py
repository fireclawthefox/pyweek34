import random
from economyStats.economyStats import EconomyStats
from buildings.buildingsManager import BuildingsManager

class Opponent(EconomyStats):
    def __init__(self):
        EconomyStats.__init__(self)
        self.build_speed = random.uniform(0.5, 1.1)
        self.wait_build_time = 0
        # opponents will built every minute multiplied by build_speed
        self.will_build_time = (1 * 60) * self.build_speed
        self.buildingsManager = BuildingsManager()

        self.max_building_numbers = {
            "livingQuarters":5,
            "foodProduction":3,
            "waterProduction":3,
            "mining":2,
            "genGoodFactory":2,
            "defenseTower":2,
            "defenseShield":1,
            "defenseArmy":1
            }

    def do_tick(self):
        dt = globalClock.get_dt()
        self.wait_build_time += dt

        for i in range(random.randint(1, 5)):
            building_id = random.choice(list(self.buildingsManager.buildings.keys()))

            building_counts = self.get_building_counts()
            max_buildings_reached = []
            for building_id, count in building_counts.items():
                if self.max_building_numbers[building_id] <= count:
                    max_buildings_reached.append(building_id)

            if self.buildingsManager.can_build_building(building_id, self, max_buildings_reached) \
            and self.will_build_time <= self.wait_build_time:
                self.buildingsManager.build_building_ai(building_id)
                self.ores -= self.buildingsManager.get_required_resources(building_id)
                self.wait_build_time = 0

            buildings = self.buildingsManager.update_building_time_ai()
            if buildings and len(buildings) > 0:
                for building in buildings:
                    self.add_building(building)

