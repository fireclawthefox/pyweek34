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

        self.attack_time = 0
        self.attack_delay = 2*60

        self.general_action_time = 0
        self.action_delay = 3*60

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

    def try_build(self, building_id):
        building_counts = self.get_building_counts()
        max_buildings_reached = []
        for building_id, count in building_counts.items():
            if self.max_building_numbers[building_id] <= count:
                max_buildings_reached.append(building_id)

        if self.buildingsManager.can_build_building(building_id, self, max_buildings_reached):
            self.buildingsManager.build_building_ai(building_id)
            self.ores -= self.buildingsManager.get_required_resources(building_id)

    def do_tick(self):
        dt = globalClock.get_dt()
        self.wait_build_time += dt
        self.attack_time += dt
        self.general_action_time += dt

        if self.wait_build_time >= self.will_build_time:
            if self.food_production < self.population:
                self.try_build("foodProduction")
            if self.water_production < self.population:
                self.try_build("waterProduction")
            if self.ore_production <= 0:
                self.try_build("mining")
            if self.general_goods_production < self.population:
                self.try_build("genGoodFactory")

            # after the important buildings, try to build up to 4 random other buildings
            for i in range(random.randint(1, 4)):
                # build 1-5 buildings
                building_id = random.choice(list(self.buildingsManager.buildings.keys()))

                self.try_build(building_id)
            self.wait_build_time = 0

        # check currently built buildings
        buildings = self.buildingsManager.update_building_time_ai()
        if buildings and len(buildings) > 0:
            for building in buildings:
                self.add_building(building)

        if self.attack_time >= self.attack_delay and self.defense_strength > 5:
            # attack player
            if random.randint(1,6) >= 5:
                base.messenger.send("attack_player", [self])
                self.attack_time = 0
            else:
                # wait another half minute
                self.attack_time = 1*30

        if self.general_action_time >= self.action_delay:
            # scouting
            factor = random.uniform(0.5, 2)
            self.water -= 10
            self.water -= 10
            if bool(random.getrandbits(1)):
                # found water
                self.water += round(10*factor)
            if bool(random.getrandbits(1)):
                # found food
                self.food += round(10*factor)
            if bool(random.getrandbits(1)):
                # found ore
                self.ores += round(10*factor)

            # did trading
            factor = random.uniform(0.5, 2)
            self.water -= round(10*factor)
            self.food -= round(10*factor)
            self.ores += round(30*factor)

            self.general_action_time = 0

            self.evaluate()
