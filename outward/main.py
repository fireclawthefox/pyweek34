#!/usr/bin/python
__author__ = "Fireclaw the Fox"
__license__ = """
Simplified BSD (BSD 2-Clause) License.
See License.txt or http://opensource.org/licenses/BSD-2-Clause for more info
"""

# Panda3D imoprts
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DGG
from panda3d.core import (
    AntialiasAttrib,
    ConfigVariableBool)
import simplepbr

# configuration handling
from core import config

# State handling
from core.coreFSM import CoreFSM

#
# MAIN GAME CLASS
#
class Main(ShowBase, CoreFSM):
    """Main function of the application
    initialise the engine (ShowBase)"""

    def __init__(self):
        """initialise the engine"""
        ShowBase.__init__(self)

        base.notify.info(f"Version {config.versionstring}")
        CoreFSM.__init__(self, "FSM-Core")

        self.setBackgroundColor(0,0,0)

        #
        # PBR SHADING
        #
        pipeline = simplepbr.init()
        pipeline.use_normals_map = False
        pipeline.enable_shadows = True

        #
        # CONFIGURATIONS
        #
        config.load_config()

        #
        # BASIC APPLICATION CONFIGURATIONS
        #
        # disable pandas default camera driver
        self.disableMouse()
        # set antialias for the complete sceen to automatic
        self.render.setAntialias(AntialiasAttrib.MAuto)
        # Enhance font readability
        DGG.setDefaultFont(loader.loadFont("assets/TheTravelingFoxText.otf"))
        DGG.getDefaultFont().setPixelsPerUnit(96)
        DGG.setDefaultClickSound(loader.loadSfx("assets/freesound_jummit_soft-ui-button-click_license_CC0.ogg"))

        #
        # CONFIGURATION LOADING
        #
        # load given variables or set defaults
        # check if particles should be enabled
        # NOTE: If you use the internal physics engine, this always has
        #       to be enabled!
        #particles = ConfigVariableBool("particles-enabled", True).getValue()
        #if particles:
        #    self.enableParticles()

        # automatically safe configuration at application exit
        base.exitFunc = config.write_config

        #
        # ENTER GAMES INITIAL FSM STATE
        #
        self.request("StartMenu")
    #
    # BASIC END
    #
# CLASS Main END

#
# START GAME
#
Game = Main()
Game.run()
