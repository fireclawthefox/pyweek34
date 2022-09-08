import csv
import os
from buildings.buildingBase import BuildingBase
from gui.btnBuilding import GUI as BtnBuilding
from direct.gui import DirectGuiGlobals as DGG
from DirectGuiExtension.DirectTooltip import DirectTooltip

class BuildingsManager:
    def __init__(self):
        self.buildings = {}
        self.building_buttons = {}
        self.currently_built_buildings_elapsed_time_s = 0
        self.currently_built_buildings = {}

        self.tooltip = DirectTooltip(
            scale=0.2,
            text_scale=0.2,
            frameColor=(0.7, 0.9, 1, 0.8),
            pad=(.1,.1))

        csv_file = os.path.join(base.main_dir, "buildings", "buildings.csv")
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            z_pos = -0.15
            for row in reader:
                building = BuildingBase(row)
                self.buildings[building.building_id] = building

    def destroy(self):
        for building_id, button in self.building_buttons.items():
            button.destroy()

    def create_building_buttons(self, button_holder_frame):
        self.button_holder_frame = button_holder_frame
        z_pos = -0.15
        for building_id, building in self.buildings.items():
            self.building_buttons[building_id] = self.create_building_button(
                building_id,
                building.name,
                building.image,
                building.tooltip.format(building.build_time_m),
                z_pos)
            z_pos -= 0.25
        z_pos += 0.1
        cs = self.button_holder_frame["canvasSize"]
        self.button_holder_frame["canvasSize"] = [
            cs[0], cs[1],
            z_pos, cs[3]]

    def can_build_building(self, building_id, economy_stats, max_buildings_reached):
        return self.buildings[building_id].required_ore <= economy_stats.ores \
            and building_id not in max_buildings_reached \
            and building_id not in self.currently_built_buildings.keys()

    def get_required_resources(self, building_id):
        return self.buildings[building_id].required_ore

    def build_building(self, building_id):
        btn = self.building_buttons[building_id]
        btn.wbBuildingTime.show()
        btn.btnBuilding["state"] = DGG.DISABLED
        btn.wbBuildingTime["value"] = 0
        btn.wbBuildingTime["text"] = ""
        self.currently_built_buildings[building_id] = 0

    def build_building_ai(self, building_id):
        self.currently_built_buildings[building_id] = 0

    def update_building_time(self):
        finished_buildings = []
        dt = globalClock.get_dt()
        for building_id in self.currently_built_buildings.keys():
            self.currently_built_buildings[building_id] += dt

            et = self.currently_built_buildings[building_id]

            btn = self.building_buttons[building_id]
            building = self.buildings[building_id]
            value = (et / (building.build_time_m * 60)) * 100
            btn.wbBuildingTime["value"] = value

            if et >= building.build_time_m * 60:
                # this building is done:
                btn.wbBuildingTime["value"] = 100
                btn.wbBuildingTime.hide()
                finished_buildings.append(self.buildings[building_id])

        for b in finished_buildings:
            print(f"removing {b.building_id} from built buildings")
            del self.currently_built_buildings[b.building_id]

        if len(finished_buildings) > 0:
            for b in finished_buildings:
                print(b.building_id)
        return finished_buildings

    def update_building_time_ai(self):
        finished_buildings = []
        for building_id, elapsed_time in self.currently_built_buildings.items():
            self.currently_built_buildings[building_id] += globalClock.get_dt()
            building = self.buildings[building_id]
            if elapsed_time >= building.build_time_m * 60:
                # this building is done:
                finished_buildings.append(self.buildings[building_id])
        for building in finished_buildings:
            del self.currently_built_buildings[building.building_id]
        return finished_buildings

    def update_building_buttons(self, economy_stats, max_buildings_reached):
        for building_id, button in self.building_buttons.items():
            if self.can_build_building(building_id, economy_stats, max_buildings_reached):
                button.btnBuilding["state"] = DGG.NORMAL
            else:
                button.btnBuilding["state"] = DGG.DISABLED

    def get_building_info(self, building_id):
        return self.buildings[building_id]

    def create_building_button(
            self,
            building_id,
            building_name,
            building_image,
            tooltip_text,
            z_pos):
        btn = BtnBuilding(self.button_holder_frame.canvas)
        btn.btnBuilding.setPos(0, 0, z_pos)
        btn.btnBuilding["frameColor"] = [
            (.8,.8,.8,0),
            (.8,.8,.9,0),
            (.9,.9,.9,0),
            (.2,.2,.2,0)]
        btn.btnBuilding["text"] = building_name
        btn.btnBuilding["text_scale"] = 0.35
        btn.btnBuilding["text_pos"] = (0,-0.8,0)
        btn.btnBuilding["text_fg"] = (1,1,1,1)
        btn.btnBuilding["text_shadow"] = (0, 0, 0, 1)
        btn.btnBuilding["image"] = (
            f"assets/icons/{building_image}_n.png",
            f"assets/icons/{building_image}_c.png",
            f"assets/icons/{building_image}_h.png",
            f"assets/icons/{building_image}_d.png")
        btn.btnBuilding["extraArgs"] = ["build_building", [building_id]]
        btn.btnBuilding.setTransparency(1)
        btn.wbBuildingTime.hide()

        btn.btnBuilding.bind(DGG.ENTER, self.tooltip.show, [tooltip_text])
        btn.btnBuilding.bind(DGG.EXIT, self.tooltip.hide)

        return btn
