from direct.gui.DirectLabel import DirectLabel
from panda3d.core import TextNode

class EconomyDisplay:
    def __init__(self, economyStats, economyFrame):

        self.header_size = 0.06
        self.stats_size = 0.045

        z = 0
        z_move = self.stats_size*2 + 0.01
        z_move_header = self.header_size + 0.01
        z_move_pre_header = 0.08

        z -= z_move_header
        self.create_stats_header(economyFrame, "Resources", z)
        z -= z_move_header

        self.lbl_population = self.create_stats_label(
            economyFrame,
            f"Population:\n{economyStats.population}",
            z)
        z -= z_move
        self.lbl_food = self.create_stats_label(
            economyFrame,
            f"Food:\n{economyStats.food}",
            z)
        z -= z_move
        self.lbl_water = self.create_stats_label(
            economyFrame,
            f"Water:\n{economyStats.water}",
            z)
        z -= z_move
        self.lbl_general_goods = self.create_stats_label(
            economyFrame,
            f"General Goods:\n{economyStats.general_goods}",
            z)
        z -= z_move
        self.lbl_ores = self.create_stats_label(
            economyFrame,
            f"Ore:\n{economyStats.ores}",
            z)
        z -= z_move

        z -= z_move_pre_header
        self.create_stats_header(economyFrame, "Military Strength", z)
        z -= z_move_header

        self.lbl_defense_strength = self.create_stats_label(
            economyFrame,
            f"Defense:\n{economyStats.defense_strength}",
            z)
        z -= z_move

        z -= z_move_pre_header
        self.create_stats_header(economyFrame, "Production", z)
        z -= z_move_header

        # production
        self.lbl_food_production = self.create_stats_label(
            economyFrame,
            f"Food Production:\n{economyStats.food_production}",
            z)
        z -= z_move
        self.lbl_water_production = self.create_stats_label(
            economyFrame,
            f"Water Production:\n{economyStats.water_production}",
            z)
        z -= z_move
        self.lbl_general_goods_production = self.create_stats_label(
            economyFrame,
            f"Gen. Goods Production:\n{economyStats.general_goods_production}",
            z)
        z -= z_move
        self.lbl_ore_production = self.create_stats_label(
            economyFrame,
            f"Ore Production:\n{economyStats.ore_production}",
            z)
        z -= z_move

        cs = economyFrame["canvasSize"]
        economyFrame["canvasSize"] = [cs[0], cs[1], z, cs[3]]

    def create_stats_header(self, economyFrame, text, z):
        return DirectLabel(
            parent=economyFrame.canvas,
            frameColor=(0,0,0,1),
            text=text,
            text_fg=(1,1,1,1),
            text_align=TextNode.ALeft,
            scale=self.header_size,
            pos=(0.01, 0, z)
        )

    def create_stats_label(self, economyFrame, text, z):
        return DirectLabel(
            parent=economyFrame.canvas,
            frameColor=(0,0,0,0),
            text=text,
            text_fg=(1,1,1,1),
            text_align=TextNode.ALeft,
            scale=self.stats_size,
            pos=(0.025, 0, z)
        )

    def destroy(self):
        self.lbl_population.destroy()
        self.lbl_food.destroy()
        self.lbl_water.destroy()
        self.lbl_general_goods.destroy()
        self.lbl_ores.destroy()
        self.lbl_defense_strength.destroy()
        self.lbl_food_production.destroy()
        self.lbl_water_production.destroy()
        self.lbl_general_goods_production.destroy()
        self.lbl_ore_production.destroy()

    def update_economy_stats(self, economyStats):
        self.lbl_population["text"] = f"Population:\n{economyStats.population}"
        self.lbl_food["text"] = f"Food:\n{economyStats.food}"
        self.lbl_water["text"] = f"Water:\n{economyStats.water}"
        self.lbl_general_goods["text"] = f"General Goods:\n{economyStats.general_goods}"
        self.lbl_ores["text"] = f"Ore:\n{economyStats.ores}"
        self.lbl_defense_strength["text"] = f"Defense:\n{economyStats.defense_strength}"
        self.lbl_food_production["text"] = f"Food Production:\n{economyStats.food_production}"
        self.lbl_water_production["text"] = f"Water Production:\n{economyStats.water_production}"
        self.lbl_general_goods_production["text"] = f"Gen. Goods Production:\n{economyStats.general_goods_production}"
        self.lbl_ore_production["text"] = f"Ore Production:\n{economyStats.ore_production}"
