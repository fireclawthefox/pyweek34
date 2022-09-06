#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectButton import DirectButton
from direct.gui.DirectWaitBar import DirectWaitBar
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):
        
        self.btnBuilding = DirectButton(
            relief = 1,
            frameSize = (-1.0, 1.0, -1.0, 1.0),
            pos = LPoint3f(0, 0, 0),
            hpr = LVecBase3f(0, 0, 0),
            scale = LVecBase3f(0.1, 0.1, 0.1),
            text = 'button',
            parent=rootParent,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=[],
        )
        self.btnBuilding.setTransparency(0)

        self.wbBuildingTime = DirectWaitBar(
            state = 'normal',
            frameColor = (0.0, 0.5, 1.0, 0.8),
            pos = LPoint3f(0, 0, 0),
            barColor = (0.0, 0.0, 1.0, 1.0),
            text = '0%',
            text0_scale = (0.1, 0.1),
            parent=self.btnBuilding,
        )
        self.wbBuildingTime.setTransparency(0)


    def show(self):
        self.btnBuilding.show()

    def hide(self):
        self.btnBuilding.hide()

    def destroy(self):
        self.btnBuilding.destroy()
