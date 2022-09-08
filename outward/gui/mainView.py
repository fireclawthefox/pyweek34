#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file was created using the DirectGUI Designer

from direct.gui import DirectGuiGlobals as DGG

from direct.gui.DirectScrolledFrame import DirectScrolledFrame
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectFrame import DirectFrame
from panda3d.core import (
    LPoint3f,
    LVecBase3f,
    LVecBase4f,
    TextNode
)

class GUI:
    def __init__(self, rootParent=None):
        
        self.frmStats = DirectScrolledFrame(
            state = 'normal',
            frameSize = (0.0, 0.5, -1.0, 0.0),
            frameColor = (0.0, 0.0, 0.0, 0.4),
            pos = LPoint3f(0, 0, 0),
            canvasSize = (0.0, 0.4, -1.5, 0.0),
            scrollBarWidth = 0.03,
            parent=base.a2dTopLeft,
        )
        self.frmStats.setTransparency(0)

        self.collapseStats = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(0.245559, 0, -1.04433),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Show/Hide Stats'],
            parent=self.frmStats,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["toggle_stats"],
        )
        self.collapseStats.setTransparency(0)

        self.lblNotification = DirectLabel(
            frameColor = (0.8, 0.8, 0.0, 0.8),
            pad = (0.5, 0.2),
            pos = LPoint3f(0, 0, -0.22),
            scale = LVecBase3f(0.07, 0.07, 0.07),
            text = ['Event Notifications'],
            parent=base.a2dTopCenter,
        )
        self.lblNotification.setTransparency(0)

        self.lblTimer = DirectLabel(
            frameColor = (0.2, 0.8, 1.0, 0.8),
            pad = (0.2, 0.2),
            pos = LPoint3f(0, 0, -0.1),
            scale = LVecBase3f(0.1, 0.1, 0.1),
            text = ['Time Left: 00:00'],
            parent=base.a2dTopCenter,
        )
        self.lblTimer.setTransparency(0)

        self.frmEconomy = DirectFrame(
            frameSize = (-1.0, 1.0, 0.0, 0.5),
            frameColor = (0.0, 0.0, 0.0, 0.5),
            pos = LPoint3f(0, 0, 0),
            text = ['Economy'],
            parent=base.a2dBottomCenter,
        )
        self.frmEconomy.setTransparency(0)

        self.btnCollapseEconomy = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(-0.693084, 0, 0.520597),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Show/Hide Economy panel'],
            parent=self.frmEconomy,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["toggle_economy"],
        )
        self.btnCollapseEconomy.setTransparency(0)

        self.btnScout = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(-0.8, 0, 0.27),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Send scouts'],
            parent=self.frmEconomy,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["send_scout"],
        )
        self.btnScout.setTransparency(0)

        self.btnTrade = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(-0.8, 0, 0.36),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Send Trader'],
            parent=self.frmEconomy,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["send_trader"],
        )
        self.btnTrade.setTransparency(0)

        self.btnRemovePopulation10 = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(-0.65, 0, 0.17),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Decimate Population by 10'],
            parent=self.frmEconomy,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["decimate_population",[10]],
        )
        self.btnRemovePopulation10.setTransparency(0)

        self.btnRemovePopulation100 = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(-0.64, 0, 0.07),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Decimate Population by 50'],
            parent=self.frmEconomy,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["decimate_population",[50]],
        )
        self.btnRemovePopulation100.setTransparency(0)

        self.frmEventLog = DirectScrolledFrame(
            state = 'normal',
            frameSize = (-0.0, 1.0, -0.45, 0.0),
            frameColor = (0.0, 0.0, 0.0, 0.5),
            pos = LPoint3f(-0.02, 0, 0.47),
            canvasSize = (0.0, 0.8, -1.0, 0.0),
            scrollBarWidth = 0.02,
            parent=self.frmEconomy,
        )
        self.frmEventLog.setTransparency(0)

        self.btnAttackOpponent = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(-0.35, 0, 0.36),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Attack Opponent'],
            parent=self.frmEconomy,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["attack_opponent"],
        )
        self.btnAttackOpponent.setTransparency(0)

        self.frmBuildings = DirectScrolledFrame(
            state = 'normal',
            frameSize = (-0.25, 0.0, -0.6, 0.6),
            frameColor = (0.0, 0.0, 0.0, 0.4),
            pos = LPoint3f(0, 0, 0.2),
            canvasSize = (-0.11, 0.11, -1.5, 0.0),
            scrollBarWidth = 0.03,
            parent=base.a2dRightCenter,
        )
        self.frmBuildings.setTransparency(0)

        self.btnQuit = DirectButton(
            relief = 5,
            frameColor = (0.2, 0.8, 1.0, 0.75),
            pos = LPoint3f(-0.15, 0, -0.05),
            scale = LVecBase3f(0.05, 0.05, 0.05),
            text = ['Quit Game'],
            parent=base.a2dTopRight,
            pressEffect=1,
            command=base.messenger.send,
            extraArgs=["ask_for_quit"],
        )
        self.btnQuit.setTransparency(0)


    def show(self):
        self.frmStats.show()
        self.lblNotification.show()
        self.lblTimer.show()
        self.frmEconomy.show()
        self.frmBuildings.show()
        self.btnQuit.show()

    def hide(self):
        self.frmStats.hide()
        self.lblNotification.hide()
        self.lblTimer.hide()
        self.frmEconomy.hide()
        self.frmBuildings.hide()
        self.btnQuit.hide()

    def destroy(self):
        self.frmStats.destroy()
        self.lblNotification.destroy()
        self.lblTimer.destroy()
        self.frmEconomy.destroy()
        self.frmBuildings.destroy()
        self.btnQuit.destroy()
