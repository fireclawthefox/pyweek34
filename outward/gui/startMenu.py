#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectButton import DirectButton
from direct.gui.DirectFrame import DirectFrame
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):

        self.btnStart = DirectButton(
            relief = 1,
            frameColor = (0.8, 0.8, 0.8, 0.0),
            pos = LPoint3f(0, 0, -0.25),
            scale = LVecBase3f(0.1, 0.1, 0.1),
            text = ['Start'],
            image0_image = 'assets/Button.png',
            image0_pos = LPoint3f(0, 0, 0),
            image0_hpr = LVecBase3f(0, 0, 0),
            image0_scale = LVecBase3f(1, 1, 1),
            image0_color = LVecBase4f(1, 1, 1, 1),
            image1_image = 'assets/Button.png',
            image1_pos = LPoint3f(0, 0, 0),
            image1_hpr = LVecBase3f(0, 0, 0),
            image1_scale = LVecBase3f(1, 1, 1),
            image1_color = LVecBase4f(1, 1, 1, 1),
            image2_image = 'assets/Button.png',
            image2_pos = LPoint3f(0, 0, 0),
            image2_hpr = LVecBase3f(0, 0, 0),
            image2_scale = LVecBase3f(1, 1, 1),
            image2_color = LVecBase4f(1, 1, 1, 1),
            image3_image = 'assets/Button.png',
            image3_pos = LPoint3f(0, 0, 0),
            image3_hpr = LVecBase3f(0, 0, 0),
            image3_scale = LVecBase3f(1, 1, 1),
            image3_color = LVecBase4f(1, 1, 1, 1),
            text0_text = 'Start',
            text0_align = 2,
            parent=base.a2dTopLeft,
            pressEffect=0,
            command=base.messenger.send,
            extraArgs=["game_start"],
            image='assets/Button.png',
        )
        self.btnStart.setTransparency(1)

        self.btnExit = DirectButton(
            relief = 1,
            frameColor = (0.8, 0.8, 0.8, 0.0),
            pos = LPoint3f(0, 0, -0.5),
            scale = LVecBase3f(0.1, 0.1, 0.1),
            text = 'button',
            parent=base.a2dTopLeft,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["game_quit"],
            image='assets/Button.png',
        )
        self.btnExit.setTransparency(1)

        self.frmBackground = DirectFrame(
            frameSize = (-1.777, 1.77777, -1.0, 1.0),
            frameColor = (0.0, 0.0, 0.0, 1.0),
            pos = LPoint3f(0, 0, 1),
            parent=base.a2dBottomCenter,
            image='assets/sky.png',
        )
        self.frmBackground.setTransparency(0)


    def show(self):
        self.btnStart.show()
        self.btnExit.show()
        self.frmBackground.show()

    def hide(self):
        self.btnStart.hide()
        self.btnExit.hide()
        self.frmBackground.hide()

    def destroy(self):
        self.btnStart.destroy()
        self.btnExit.destroy()
        self.frmBackground.destroy()
