import random
from gui.mainView import GUI as MainView
from panda3d.core import TextNode, DirectionalLight, CardMaker, CullBinAttrib, TexGenAttrib, TextureStage, PerspectiveLens, Spotlight
from economyStats.economyStats import EconomyStats
from economyStats.economyDisplay import EconomyDisplay
from events.eventHandler import EventHandler
from buildings.buildingsManager import BuildingsManager
from direct.showbase.DirectObject import DirectObject
from datetime import timedelta
from direct.gui.OnscreenImage import OnscreenImage
from direct.interval.IntervalGlobal import (
    Sequence,
    Parallel,
    Wait,
    Func,
    LerpColorScaleInterval)
from ai.opponent import Opponent
from scene.scene import Scene
from direct.gui import DirectGuiGlobals as DGG
from direct.gui.DirectDialog import OkDialog, YesNoDialog

class CoreGame(DirectObject):
    def __init__(self):
        # enable event handling for this class
        DirectObject.__init__(self)

        # store the elapsed time in the game
        self.game_time_s = 0
        # calculate how long the game takes, red planets year packed into 1 hour
        self.red_planet_year_s = 30 * 60 #* (687 / 12 / 60) * 60
        #print(f"YEAR in s {self.red_planet_year_s}")
        # store the time until the next tick
        self.tick_time_s = 0
        # do a tick every "week" in game time
        self.calculate_tick_time_s = (self.red_planet_year_s / (12 * 4))# * 60

        self.mainView = MainView()
        self.mainView.frmEconomy["text"] = "Economy"
        self.mainView.frmEconomy["text_align"] = TextNode.ALeft
        self.mainView.frmEconomy["text_fg"] = (1,1,1,1)
        self.mainView.frmEconomy["text_scale"] = (0.05, 0.05, 0.05)
        self.mainView.frmEconomy["text_pos"] = (-1, 0.45, 0)

        self.mainView.hide()

        self.dlg_game_over = None

        self.notification_fade_in = LerpColorScaleInterval(
            self.mainView.lblNotification,
            0.1,
            (1.0, 1.0, 1.0, 1.0))

        self.notification_fade_out = LerpColorScaleInterval(
            self.mainView.lblNotification,
            2,
            (0.0, 0.0, 0.0, 0.0))
        self.notification_fade_out.start()

        self.player_economy = EconomyStats()
        self.player_economy.is_player_stats = True

        self.opponents = [
            Opponent()
        ]

        self.eventHandler = EventHandler()

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

        self.buildingsManager = BuildingsManager()
        self.buildingsManager.create_building_buttons(self.mainView.frmBuildings)
        self.economyDisplay = EconomyDisplay(self.player_economy, self.mainView.frmStats)

        self.scene_root = render.attachNewNode("SceneRoot")
        self.scene = Scene(self.scene_root)

        #self.scene.ground.find("**/Sun").setColor(10,10,10,1)
        #sun = self.scene.ground.find("**/Sun").find("**/Sun").node()
        #sun.setShadowCaster(True, 1024, 1024)
        #lens = sun.getLens()
        #lens.setFilmSize(8, 8)
        #lens.setNearFar(1, 100000)
        #sun.setMaxDistance(10000)
        #sun.getLens()
        #self.scene.ground.setDepthOffset(100)

        #slight = Spotlight('slight')
        #slight.setColor((1, 1, 1, 1))
        #lens = PerspectiveLens()
        #lens.setFocalLength(10)
        #lens.setFar(200)
        #slight.setLens(lens)
        #slight.setShadowCaster(True, 1024, 1024)
        #sun = render.attachNewNode(slight)
        #sun.setPos(7, -8, 10)
        #sun.lookAt(self.scene.ground)
        #render.setLight(sun)

        self.scene.hide()
        self.scene.ground.show()

        cm = CardMaker("sky")
        cm.set_frame(-1.7777, 1.7777, -1, 1)
        self.sky = base.cam.attachNewNode(cm.generate())
        tex = loader.loadTexture("assets/sky.png")
        self.sky.set_texture(tex)
        self.sky.set_pos(base.cam, (0,2,1))
        self.sky.set_depth_test(False)
        self.sky.set_depth_write(False)
        self.sky.set_attrib(CullBinAttrib.make("skyBin", 1000))
        self.sky.set_shader_off()
        self.sky.set_light_off()

        base.cam.set_pos(self.scene.PerspectiveLens_camera_1_np.get_pos())
        base.cam.set_hpr(self.scene.PerspectiveLens_camera_1_np.get_hpr())
        base.camLens.setFov(70)

    def game_start(self):
        self.show_gui()
        self.start_game_loop()

        self.accept("event_happened", self.show_event)
        self.accept("build_building", self.build_building)

        self.accept("toggle_stats", self.toggle_stats)
        self.accept("toggle_economy", self.toggle_economy_panel)

        self.accept("send_scout", self.send_scout)
        self.accept("send_trader", self.send_trader)
        self.accept("decimate_population", self.decimate_population)

        self.accept("remove_building_event", self.remove_building)

        self.accept("ask_for_quit", self.ask_for_quit)

    def game_over(self):
        self.hide_gui()
        has_won = self.player_has_won()
        if has_won:
            self.dlg_game_over = OkDialog(
                text=self.get_game_over_text(has_won),
                text_fg=(1,1,1,1),
                command=self.quit,
                frameColor=(0.2,0.8,1,0.75))
        else:
            self.dlg_game_over = OkDialog(
                text=self.get_game_over_text(has_won),
                text_fg=(1,1,1,1),
                command=self.quit,
                frameColor=(0.8,0.4,0.2,0.75))

    def get_game_over_text(self, has_won):
        text = ""
        if has_won:
            text = "Congratulation!\n"
            text += f"You won with {self.player_economy.get_strength()} Points.\n"
        else:
            text = "Too bad, you lost...\n"
            text += f"You had {self.player_economy.get_strength()} Points.\n"

        text += "\n"
        text += "\n"
        text += "your Opponents had:\n"
        for i, opponent in enumerate(self.opponents):
            text += f"Opponent {i+1}: {opponent.get_strength()}\n"

        return text

    def ask_for_quit(self):
        self.dlg_game_over = YesNoDialog(
            text="Really Quit?",
            text_fg=(1,1,1,1),
            command=self.quit,
            frameColor=(0.2,0.8,1,0.75))

    def quit(self, args=None):
        if self.dlg_game_over:
            self.dlg_game_over.destroy()
        if args == 1:
            base.messenger.send("quit_game")

    def destroy(self):
        self.ignore_all()
        taskMgr.remove("NotificationFadeOut")
        taskMgr.remove("scouting_in_progress")
        taskMgr.remove("trade_in_progress")
        taskMgr.remove("world task")
        self.buildingsManager.destroy()
        self.economyDisplay.destroy()
        self.mainView.destroy()
        self.sky.remove_node()
        self.scene_root.remove_node()

    def start_game_loop(self):
        base.taskMgr.add(self.game_tick, "world task")

    def game_tick(self, task):
        self.game_time_s += globalClock.get_dt()
        self.tick_time_s += globalClock.get_dt()

        # let the player do their thing
        # Calculate building time
        buildings = self.buildingsManager.update_building_time()
        if buildings and len(buildings) > 0:
            self.show_event("Buildings finished")
            for building in buildings:
                self.player_economy.add_building(building)
                self.show_building(building)

        # let the opponents do their thing
        for opponent in self.opponents:
            opponent.do_tick()

        if self.tick_time_s >= self.calculate_tick_time_s:
            # do the calculation tick for the statistics
            self.show_event("A week has passed, stats were updated")
            self.tick_time_s = 0
            self.player_economy.tick_stats_calculate()
            for opponent in self.opponents:
                opponent.tick_stats_calculate()

        # check for event happenings
        self.eventHandler.check_events([self.player_economy] + self.opponents)

        # update the building UI
        max_buildings_reached = self.get_max_buildings_reached()
        self.buildingsManager.update_building_buttons(self.player_economy, max_buildings_reached)

        self.economyDisplay.update_economy_stats(self.player_economy)

        # update the timer
        timer_time_s = self.red_planet_year_s - self.game_time_s
        td = timedelta(seconds=timer_time_s)

        h, rem = divmod(td.seconds, 3600)
        m, s = divmod(rem, 60)

        self.mainView.lblTimer["text"] = f"Time Left: {m:02d}:{s:02d}"

        if self.game_time_s >= self.red_planet_year_s:
            # time ran out, game is over
            self.game_over()
            return task.done
        return task.cont

    def show_gui(self):
        self.mainView.show()

    def hide_gui(self):
        self.mainView.hide()

    def show_event(self, event_text):
        if taskMgr.hasTaskNamed("NotificationFadeOut"):
            taskMgr.remove("NotificationFadeOut")
        else:
            self.notification_fade_in.start()

        self.mainView.lblNotification["text"] = event_text
        self.mainView.lblNotification.resetFrameSize()

        taskMgr.doMethodLater(5, self.notification_fade_out.start, "NotificationFadeOut", extraArgs=[])

    def get_max_buildings_reached(self):
        building_counts = self.player_economy.get_building_counts()
        max_buildings_reached = []
        for building_id, count in building_counts.items():
            if self.max_building_numbers[building_id] <= count:
                max_buildings_reached.append(building_id)
        return max_buildings_reached

    def build_building(self, building_id):
        max_buildings_reached = self.get_max_buildings_reached()

        if self.buildingsManager.can_build_building(building_id, self.player_economy, max_buildings_reached):
            self.buildingsManager.build_building(building_id)
            self.player_economy.ores -= self.buildingsManager.get_required_resources(building_id)
            self.buildingsManager.update_building_buttons(self.player_economy, max_buildings_reached)

    def player_has_won(self):
        has_won = True
        player_strength = self.player_economy.get_strength()
        for opponent in self.opponents:
            has_won = player_strength >= opponent.get_strength()
        return has_won

    def show_building(self, building):
        building_id = building.building_id
        if building_id == "livingQuarters":
            if self.scene.livingQuarters1.isHidden():
                self.scene.livingQuarters1.show()
            elif self.scene.livingQuarters2.isHidden():
                self.scene.livingQuarters2.show()
            elif self.scene.livingQuarters3.isHidden():
                self.scene.livingQuarters3.show()
            elif self.scene.livingQuarters4.isHidden():
                self.scene.livingQuarters4.show()
            elif self.scene.livingQuarters5.isHidden():
                self.scene.livingQuarters5.show()
        elif building_id == "foodProduction":
            if self.scene.farm1.isHidden():
                self.scene.farm1.show()
            elif self.scene.farm2.isHidden():
                self.scene.farm2.show()
            elif self.scene.farm3.isHidden():
                self.scene.farm3.show()
        elif building_id == "waterProduction":
            if self.scene.WaterRefinary1.isHidden():
                self.scene.WaterRefinary1.show()
            elif self.scene.WaterRefinary2.isHidden():
                self.scene.WaterRefinary2.show()
            elif self.scene.WaterRefinary3.isHidden():
                self.scene.WaterRefinary3.show()
        elif building_id == "mining":
            if self.scene.mine1.isHidden():
                self.scene.mine1.show()
            elif self.scene.mine2.isHidden():
                self.scene.mine2.show()
        elif building_id == "genGoodFactory":
            if self.scene.factory1.isHidden():
                self.scene.factory1.show()
            elif self.scene.factory2.isHidden():
                self.scene.factory2.show()
        elif building_id == "defenseTower":
            if self.scene.tower1.isHidden():
                self.scene.tower1.show()
            elif self.scene.tower2.isHidden():
                self.scene.tower2.show()
        elif building_id == "defenseShield":
            if self.scene.shield.isHidden():
                self.scene.shield.show()
        elif building_id == "defenseArmy":
            if self.scene.Army.isHidden():
                self.scene.Army.show()

        self.buildingsManager.update_building_buttons(self.player_economy, self.get_max_buildings_reached())

    def remove_building(self, building):
        building_id = building.building_id
        if building_id == "livingQuarters":
            if not self.scene.livingQuarters5.isHidden():
                self.scene.livingQuarters5.hide()
            elif not self.scene.livingQuarters4.isHidden():
                self.scene.livingQuarters4.hide()
            elif not self.scene.livingQuarters3.isHidden():
                self.scene.livingQuarters3.hide()
            elif not self.scene.livingQuarters2.isHidden():
                self.scene.livingQuarters2.hide()
            elif not self.scene.livingQuarters1.isHidden():
                self.scene.livingQuarters1.hide()
        elif building_id == "foodProduction":
            if not self.scene.farm3.isHidden():
                self.scene.farm3.hide()
            elif not self.scene.farm2.isHidden():
                self.scene.farm2.hide()
            elif not self.scene.farm1.isHidden():
                self.scene.farm1.hide()
        elif building_id == "waterProduction":
            if not self.scene.WaterRefinary3.isHidden():
                self.scene.WaterRefinary3.hide()
            elif not self.scene.WaterRefinary2.isHidden():
                self.scene.WaterRefinary2.hide()
            elif not self.scene.WaterRefinary1.isHidden():
                self.scene.WaterRefinary1.hide()
        elif building_id == "mining":
            if not self.scene.mine2.isHidden():
                self.scene.mine2.hide()
            elif not self.scene.mine1.isHidden():
                self.scene.mine1.hide()
        elif building_id == "genGoodFactory":
            if not self.scene.factory2.isHidden():
                self.scene.factory2.hide()
            elif not self.scene.factory1.isHidden():
                self.scene.factory1.hide()
        elif building_id == "defenseTower":
            if not self.scene.tower2.isHidden():
                self.scene.tower2.hide()
            elif not self.scene.tower1.isHidden():
                self.scene.tower1.hide()
        elif building_id == "defenseShield":
            if not self.scene.shield.isHidden():
                self.scene.shield.hide()
        elif building_id == "defenseArmy":
            if not self.scene.Army.isHidden():
                self.scene.Army.hide()

        self.buildingsManager.update_building_buttons(self.player_economy, self.get_max_buildings_reached())

    def send_scout(self):
        if taskMgr.hasTaskNamed("scouting_in_progress"):
            return
        self.show_event(f"Scout will be back in 1 Minute")
        taskMgr.doMethodLater(1*60, self.scout_comeback, "scouting_in_progress", extraArgs=[])
        self.mainView.btnScout["state"] = DGG.DISABLED
        fc = self.mainView.btnScout["frameColor"]
        self.mainView.btnScout["frameColor"] = (fc[0] * 0.5, fc[1] * 0.5, fc[2] * 0.5, fc[3])

    def scout_comeback(self):
        factor = random.uniform(0.5, 2)

        self.player_economy.water -= 10
        self.player_economy.water -= 10

        text = "Scout come back with "

        found_anything = False

        if bool(random.getrandbits(1)):
            # found water
            water = round(10*factor)
            self.player_economy.water += water
            text += f"{water} Water "
            found_anything = True
        if bool(random.getrandbits(1)):
            # found food
            food = round(10*factor)
            self.player_economy.food += food
            text += f"{food} Food "
            found_anything = True
        if bool(random.getrandbits(1)):
            # found ore
            ore = round(10*factor)
            self.player_economy.ores += ore
            text += f"{ore} Ores"
            found_anything = True

        if not found_anything:
            text += "nothing."

        self.show_event(text)

        self.mainView.btnScout["state"] = DGG.NORMAL
        fc = self.mainView.btnScout["frameColor"]
        self.mainView.btnScout["frameColor"] = (0.2, 0.8, 1.0, 0.75)

    def send_trader(self):
        if taskMgr.hasTaskNamed("trade_in_progress"):
            return
        self.show_event(f"Trader will be back in 1 Minute")
        taskMgr.doMethodLater(1*60, self.trader_comeback, "trade_in_progress", extraArgs=[])
        self.mainView.btnTrade["state"] = DGG.DISABLED
        fc = self.mainView.btnTrade["frameColor"]
        self.mainView.btnTrade["frameColor"] = (fc[0] * 0.5, fc[1] * 0.5, fc[2] * 0.5, fc[3])

    def trader_comeback(self):
        factor = random.uniform(0.5, 2)
        self.player_economy.water -= round(10*factor)
        self.player_economy.food -= round(10*factor)
        new_ores = round(30*factor)
        self.player_economy.ores += new_ores
        self.mainView.btnTrade["state"] = DGG.NORMAL
        fc = self.mainView.btnTrade["frameColor"]
        self.mainView.btnTrade["frameColor"] = (0.2, 0.8, 1.0, 0.75)

        self.show_event(f"Trader Came back with {new_ores} ore")

    def decimate_population(self, amount):
        if self.player_economy.population > amount:
            self.player_economy.population -= amount
        else:
            self.show_event(f"Can't remove the complete population")

    def toggle_stats(self):
        frm = self.mainView.frmStats
        if frm.get_z() == 1:
            frm.posInterval(
                0.4,
                (0, 0, 0),
                (0, 0, 1)
            ).start()
        else:
            frm.posInterval(
                0.4,
                (0, 0, 1),
                (0, 0, 0)
            ).start()

    def toggle_economy_panel(self):
        frm = self.mainView.frmEconomy
        if frm.get_z() == -0.5:
            frm.posInterval(
                0.2,
                (0, 0, 0),
                (0, 0, -0.5)
            ).start()
        else:
            frm.posInterval(
                0.2,
                (0, 0, -0.5),
                (0, 0, 0)
            ).start()
