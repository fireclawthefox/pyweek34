# Panda3D imoprts
from direct.fsm.FSM import FSM
from gui.startMenu import GUI as StartMenuHandler
from core.coreGame import CoreGame
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectDialog import OkDialog
from panda3d.core import TextNode
from story import STORY_TEXT
import sys

class CoreFSM(FSM):
    def __init__(self, fsm_name):
        FSM.__init__(self, fsm_name)
        self.titleFont = loader.loadFont("assets/Warszawa.otf")
        self.titleFont.setPixelsPerUnit(100)

    def enterStartMenu(self):
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
        self.startMenu.destroy()
        self.startMenu = None
        self.background.destroy()

    def ok(self, value, next_state):
        self.request(next_state)

    def enterStory(self):
        self.story = OkDialog(
            text=STORY_TEXT,
            frameColor=(0.2, 0.8, 1, 1),
            command=self.ok,
            extraArgs=["Main"])

    def exitStory(self):
        self.story.destroy()

    def enterMain(self):
        # main application logic should be started here
        self.coreGame = CoreGame()
        self.coreGame.game_start()
        self.accept("quit_game", self.request, ["StartMenu"])

    def exitMain(self):
        # cleanup for application code
        self.coreGame.destroy()
