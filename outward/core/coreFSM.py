# Panda3D imoprts
from direct.fsm.FSM import FSM
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectDialog import OkDialog
from panda3d.core import TextNode

from gui.startMenu import GUI as StartMenuHandler
from core.coreGame import CoreGame
from story import STORY_TEXT, STORY_TEXT_END_GOOD, STORY_TEXT_END_BAD

import sys
import random

class CoreFSM(FSM):
    def __init__(self, fsm_name):
        FSM.__init__(self, fsm_name)
        self.titleFont = loader.loadFont("assets/Warszawa.otf")
        self.titleFont.setPixelsPerUnit(100)

        self.menu_music = loader.loadMusic("assets/opengameart_brandon75689_ambientmain_license_CC0.ogg")
        self.menu_music.setLoop(True)

        self.game_tracks = [
            loader.loadMusic("assets/opengameart_yd_caravan_license_CC0.ogg"),
            loader.loadMusic("assets/opengameart_yd_MyVeryOwnDeadShip_license_CC0.ogg"),
            loader.loadMusic("assets/opengameart_vitalezzz_pulsar_license_CCBY4.0.ogg"),
            loader.loadMusic("assets/opengameart_vitalezzz_solar_sail_license_CCBY4.0.ogg"),
            loader.loadMusic("assets/opengameart_vitalezzz_star_on_the_horizon_license_CCBY4.0.ogg")
        ]
        self.current_music = random.choice(self.game_tracks)

    def music_playlist_task(self, task):
        if self.current_music.status() == self.current_music.PLAYING:
            return task.cont

        last_music = self.current_music
        while self.current_music == last_music:
            self.current_music = random.choice(self.game_tracks)

        self.current_music.play()
        return task.cont

    def enterStartMenu(self):
        self.menu_music.play()
        self.startMenu = StartMenuHandler()
        self.startMenu.btnStart["text_align"] = TextNode.ALeft
        self.startMenu.btnStart["text_fg"] = (1, 1, 1, 1)
        self.startMenu.btnStart["text_pos"] = (0.2, -0.3)
        self.startMenu.btnStart["image_scale"] = (8, 1, 1)
        self.startMenu.btnStart["image_pos"] = (8, 0, 0)
        self.startMenu.btnStart["frameSize"] = [0, 16, -1, 1]
        self.startMenu.btnStart.resetFrameSize()

        self.startMenu.btnExit["text"] = "Exit"
        self.startMenu.btnExit["text_align"] = TextNode.ALeft
        self.startMenu.btnExit["text_fg"] = (1, 1, 1, 1)
        self.startMenu.btnExit["text_pos"] = (0.2, -0.3)
        self.startMenu.btnExit["image_scale"] = (8, 1, 1)
        self.startMenu.btnExit["image_pos"] = (8, 0, 0)
        self.startMenu.btnExit["frameSize"] = [0, 16, -1, 1]
        self.startMenu.btnExit.resetFrameSize()

        self.startMenu.frmBackground["image_scale"] = (1.7777, 1, 1)

        self.background = DirectLabel(
            parent = base.a2dRightCenter,
            text = "Outward",
            text_font = self.titleFont,
            text_align=TextNode.ACenter,
            text_fg=(1,1,1,1),
            frameColor = (0,0,0,0),
            hpr = (0,0,-90),
            scale = (0.3),
            pos = (0, 0, 0))


        self.accept("game_start", self.request, ["Story"])
        self.accept("game_quit", base.userExit)

    def exitStartMenu(self):
        self.menu_music.stop()
        self.startMenu.destroy()
        self.startMenu = None
        self.background.destroy()

    def ok(self, value, next_state):
        self.request(next_state)

    def enterStory(self):
        self.current_music.play()
        self.story = OkDialog(
            text=STORY_TEXT,
            frameColor=(0.2, 0.8, 1, 1),
            command=self.ok,
            extraArgs=["Main"])
        base.taskMgr.add(self.music_playlist_task, "playlist")

    def exitStory(self):
        self.story.destroy()

    def enterMain(self):
        # main application logic should be started here
        self.coreGame = CoreGame()
        self.coreGame.game_start()
        self.accept("quit_game", self.request, ["StartMenu"])
        self.accept("show_end_story_victory", self.request, ["StoryEndGood"])
        self.accept("show_end_story_defeated", self.request, ["StoryEndBad"])

    def exitMain(self):
        # cleanup for application code
        self.coreGame.destroy()
        base.taskMgr.remove("playlist")

    def enterStoryEndGood(self):
        self.current_music.play()
        self.story = OkDialog(
            text=STORY_TEXT_END_GOOD,
            frameColor=(0.2, 0.8, 1, 1),
            command=self.ok,
            extraArgs=["StartMenu"])

    def exitStoryEndGood(self):
        self.story.destroy()

    def enterStoryEndBad(self):
        self.current_music.play()
        self.story = OkDialog(
            text=STORY_TEXT_END_BAD,
            frameColor=(0.1, 0.7, 0.9, 1),
            command=self.ok,
            extraArgs=["StartMenu"])

    def exitStoryEndBad(self):
        self.story.destroy()
