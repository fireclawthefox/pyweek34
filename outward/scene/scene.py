#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file was created using the Scene Editor

from panda3d.core import (
    LPoint3f,
    LVector3f,
    LVecBase3f,
    LVecBase2f,
    LVector2f,
    LPlane,
    NodePath,
    CollisionNode,
    CollisionSphere,
    CollisionCapsule,
    CollisionInvSphere,
    CollisionPlane,
    CollisionRay,
    CollisionLine,
    CollisionSegment,
    CollisionParabola,
    CollisionBox,
    PointLight,
    DirectionalLight,
    AmbientLight,
    Spotlight,
    Camera,
    PerspectiveLens,
)
from panda3d.physics import ActorNode

class Scene:
    def __init__(self, rootParent=None):
        if rootParent is None:
            rootParent = base.render

        self.ground = loader.load_model('assets/Ground.bam')
        self.ground.set_pos(LPoint3f(0, 0, -28.9166))
        self.ground.set_hpr(LVecBase3f(0, 0, 0))
        self.ground.set_scale(LVecBase3f(1, 1, 1))
        self.ground.reparent_to(rootParent)

        self.farm1 = loader.load_model('assets/Farm.bam')
        self.farm1.set_pos(LPoint3f(36.5471, -107.427, -37.268))
        self.farm1.set_hpr(LVecBase3f(-0.980231, -3.32869, -5.8968))
        self.farm1.set_scale(LVecBase3f(0.20291, 0.20291, 0.20291))
        self.farm1.reparent_to(rootParent)

        self.farm2 = loader.load_model('assets/Farm.bam')
        self.farm2.set_pos(LPoint3f(50.247, -102.531, -36.377))
        self.farm2.set_hpr(LVecBase3f(-0.980231, -3.32869, -5.8968))
        self.farm2.set_scale(LVecBase3f(0.24569, 0.24569, 0.24569))
        self.farm2.reparent_to(rootParent)

        self.farm3 = loader.load_model('assets/Farm.bam')
        self.farm3.set_pos(LPoint3f(45.9533, -89.2577, -37.3652))
        self.farm3.set_hpr(LVecBase3f(-0.980231, -3.32869, -5.8968))
        self.farm3.set_scale(LVecBase3f(0.20291, 0.20291, 0.20291))
        self.farm3.reparent_to(rootParent)

        self.PerspectiveLens_camera_1_lens = PerspectiveLens()
        self.PerspectiveLens_camera_1_lens.aspect_ratio = 1.0
        self.PerspectiveLens_camera_1_lens.fov = LVecBase2f(70, 70)
        self.PerspectiveLens_camera_1_lens.film_size = LVecBase2f(1, 1)
        self.PerspectiveLens_camera_1_lens.film_offset = LVector2f(0, 0)
        self.PerspectiveLens_camera_1_lens.near = 1.0
        self.PerspectiveLens_camera_1_lens.far = 100000.0
        self.PerspectiveLens_camera_1_lens.focal_length = 0.7140740156173706
        self.PerspectiveLens_camera_1_lens.min_fov = 0.0
        self.PerspectiveLens_camera_1_lens.view_hpr = LVecBase3f(0, 0, 0)
        self.PerspectiveLens_camera_1_lens.keystone = LVecBase2f(0, 0)
        self.PerspectiveLens_camera_1_lens.convergence_distance = 25.0
        self.PerspectiveLens_camera_1_lens.interocular_distance = 0.20000000298023224
        self.PerspectiveLens_camera_1 = Camera('PerspectiveLens_camera_1', self.PerspectiveLens_camera_1_lens)
        self.PerspectiveLens_camera_1_np = rootParent.attachNewNode(self.PerspectiveLens_camera_1)
        self.PerspectiveLens_camera_1_np.set_pos(LPoint3f(-0.707939, -242.976, 16.4994))
        self.PerspectiveLens_camera_1_np.set_hpr(LVecBase3f(0, -16.3497, 0))
        self.PerspectiveLens_camera_1_np.set_scale(LVecBase3f(1, 1, 1))

        self.WaterRefinary1 = loader.load_model('assets/WaterRefinery.bam')
        self.WaterRefinary1.set_pos(LPoint3f(-34.2752, -105.393, -41.515))
        self.WaterRefinary1.set_hpr(LVecBase3f(0, 1.79922, -4.36619))
        self.WaterRefinary1.set_scale(LVecBase3f(0.151845, 0.151845, 0.151845))
        self.WaterRefinary1.reparent_to(rootParent)

        self.WaterRefinary2 = loader.load_model('assets/WaterRefinery.bam')
        self.WaterRefinary2.set_pos(LPoint3f(-37.2477, -114.962, -41.5149))
        self.WaterRefinary2.set_hpr(LVecBase3f(0, 1.79922, -4.36619))
        self.WaterRefinary2.set_scale(LVecBase3f(0.151845, 0.151845, 0.151845))
        self.WaterRefinary2.reparent_to(rootParent)

        self.WaterRefinary3 = loader.load_model('assets/WaterRefinery.bam')
        self.WaterRefinary3.set_pos(LPoint3f(-42.6968, -99.6699, -41.5149))
        self.WaterRefinary3.set_hpr(LVecBase3f(0, 1.79922, -4.36619))
        self.WaterRefinary3.set_scale(LVecBase3f(0.151845, 0.151845, 0.151845))
        self.WaterRefinary3.reparent_to(rootParent)

        self.Army = loader.load_model('assets/Army.bam')
        self.Army.set_pos(LPoint3f(-30.5898, -78.6266, -39.5378))
        self.Army.set_hpr(LVecBase3f(-0.469384, 6.85884, -0.257784))
        self.Army.set_scale(LVecBase3f(1.5423, 1.5423, 1.5423))
        self.Army.reparent_to(rootParent)

        self.factory1 = loader.load_model('assets/Factory.bam')
        self.factory1.set_pos(LPoint3f(31.3696, -68.9401, -38.6658))
        self.factory1.set_hpr(LVecBase3f(-34.6019, 0, 0))
        self.factory1.set_scale(LVecBase3f(2.14742, 2.14742, 2.14742))
        self.factory1.reparent_to(rootParent)

        self.factory2 = loader.load_model('assets/Factory.bam')
        self.factory2.set_pos(LPoint3f(29.524, -59.899, -38.366))
        self.factory2.set_hpr(LVecBase3f(-34.6019, 0, 0))
        self.factory2.set_scale(LVecBase3f(2.14742, 2.14742, 2.14742))
        self.factory2.reparent_to(rootParent)

        self.livingQuarters1 = loader.load_model('assets/LivingQuarters.bam')
        self.livingQuarters1.set_pos(LPoint3f(0.626662, -99.9173, -39.7591))
        self.livingQuarters1.set_hpr(LVecBase3f(0, 0, 0))
        self.livingQuarters1.set_scale(LVecBase3f(0.193179, 0.193179, 0.193179))
        self.livingQuarters1.reparent_to(rootParent)

        self.livingQuarters2 = loader.load_model('assets/LivingQuarters.bam')
        self.livingQuarters2.set_pos(LPoint3f(11.2904, -107.06, -39.1815))
        self.livingQuarters2.set_hpr(LVecBase3f(0, 0, 0))
        self.livingQuarters2.set_scale(LVecBase3f(0.193179, 0.193179, 0.193179))
        self.livingQuarters2.reparent_to(rootParent)

        self.livingQuarters5 = loader.load_model('assets/LivingQuarters.bam')
        self.livingQuarters5.set_pos(LPoint3f(11.173, -92.773, -39.576))
        self.livingQuarters5.set_hpr(LVecBase3f(0, 0, 0))
        self.livingQuarters5.set_scale(LVecBase3f(0.193179, 0.193179, 0.193179))
        self.livingQuarters5.reparent_to(rootParent)

        self.livingQuarters4 = loader.load_model('assets/LivingQuarters.bam')
        self.livingQuarters4.set_pos(LPoint3f(-9.8066, -92.2132, -40.0718))
        self.livingQuarters4.set_hpr(LVecBase3f(0, 0, 0))
        self.livingQuarters4.set_scale(LVecBase3f(0.193179, 0.193179, 0.193179))
        self.livingQuarters4.reparent_to(rootParent)

        self.livingQuarters3 = loader.load_model('assets/LivingQuarters.bam')
        self.livingQuarters3.set_pos(LPoint3f(-9.68948, -107.9, -40.0771))
        self.livingQuarters3.set_hpr(LVecBase3f(0, 0, 0))
        self.livingQuarters3.set_scale(LVecBase3f(0.193179, 0.193179, 0.193179))
        self.livingQuarters3.reparent_to(rootParent)

        self.mine1 = loader.load_model('assets/Mine.bam')
        self.mine1.set_pos(LPoint3f(-66.3686, 23.8428, -16.7237))
        self.mine1.set_hpr(LVecBase3f(0, 0, 0))
        self.mine1.set_scale(LVecBase3f(1.60912, 1.60912, 1.60912))
        self.mine1.reparent_to(rootParent)

        self.mine2 = loader.load_model('assets/Mine.bam')
        self.mine2.set_pos(LPoint3f(-126.138, -3.834, -19.254))
        self.mine2.set_hpr(LVecBase3f(88.4176, 0, 0))
        self.mine2.set_scale(LVecBase3f(1.60912, 1.60912, 1.60912))
        self.mine2.reparent_to(rootParent)

        self.tower1 = loader.load_model('assets/Tower.bam')
        self.tower1.set_pos(LPoint3f(101.947, 112.412, -11.3307))
        self.tower1.set_hpr(LVecBase3f(0, 0, 0))
        self.tower1.set_scale(LVecBase3f(2.03685, 2.03685, 2.03685))
        self.tower1.reparent_to(rootParent)

        self.tower2 = loader.load_model('assets/Tower.bam')
        self.tower2.set_pos(LPoint3f(-62.7124, 58.8314, 1.80379))
        self.tower2.set_hpr(LVecBase3f(0, 0, 0))
        self.tower2.set_scale(LVecBase3f(2.03685, 2.03685, 2.03685))
        self.tower2.reparent_to(rootParent)

        self.shield = loader.load_model('assets/Shield.bam')
        self.shield.set_pos(LPoint3f(0.111017, -17.618, -30.6882))
        self.shield.set_hpr(LVecBase3f(0, 0, 0))
        self.shield.set_scale(LVecBase3f(4.40348, 4.40348, 4.40348))
        self.shield.reparent_to(rootParent)


    def show(self):
        self.ground.show()
        self.farm1.show()
        self.farm2.show()
        self.farm3.show()
        self.WaterRefinary1.show()
        self.WaterRefinary2.show()
        self.WaterRefinary3.show()
        self.Army.show()
        self.factory1.show()
        self.factory2.show()
        self.livingQuarters1.show()
        self.livingQuarters2.show()
        self.livingQuarters5.show()
        self.livingQuarters4.show()
        self.livingQuarters3.show()
        self.mine1.show()
        self.mine2.show()
        self.tower1.show()
        self.tower2.show()
        self.shield.show()

    def hide(self):
        self.ground.hide()
        self.farm1.hide()
        self.farm2.hide()
        self.farm3.hide()
        self.WaterRefinary1.hide()
        self.WaterRefinary2.hide()
        self.WaterRefinary3.hide()
        self.Army.hide()
        self.factory1.hide()
        self.factory2.hide()
        self.livingQuarters1.hide()
        self.livingQuarters2.hide()
        self.livingQuarters5.hide()
        self.livingQuarters4.hide()
        self.livingQuarters3.hide()
        self.mine1.hide()
        self.mine2.hide()
        self.tower1.hide()
        self.tower2.hide()
        self.shield.hide()

    def remove_node(self):
        self.ground.remove_node()
        self.farm1.remove_node()
        self.farm2.remove_node()
        self.farm3.remove_node()
        self.WaterRefinary1.remove_node()
        self.WaterRefinary2.remove_node()
        self.WaterRefinary3.remove_node()
        self.Army.remove_node()
        self.factory1.remove_node()
        self.factory2.remove_node()
        self.livingQuarters1.remove_node()
        self.livingQuarters2.remove_node()
        self.livingQuarters5.remove_node()
        self.livingQuarters4.remove_node()
        self.livingQuarters3.remove_node()
        self.mine1.remove_node()
        self.mine2.remove_node()
        self.tower1.remove_node()
        self.tower2.remove_node()
        self.shield.remove_node()
