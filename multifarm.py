from __builtins__ import *

import cactusFarm
import pumpkinFarm
import fillFarm
import boneFarm
import sunflowerFarm

import drone

needs = [Entities.Grass]

clear()

def drone_cactus_farm():
	
		cactusFarm.farm((8,8),(15,15))
		#fillFarm.farm((0,12),(15,15),needs)
		#sunflowerFarm.farm((8,14),(15,15))

def drone_carrot_farm():
	
		fillFarm.farm((0,8),(7,15),[Entities.Carrot])
		#fillFarm.farm((0,8),(15,11),needs)

def drone_tree_farm():
	#fillFarm.farm((8,0),(15,7),[Entities.Tree,Entities.Tree])
		#fillFarm.farm((8,0),(15,13),needs)
		sunflowerFarm.farm((10,0),(15,1))

spawn = spawn_drone(drone_cactus_farm)
spawn = spawn_drone(drone_carrot_farm)
spawn = spawn_drone(drone_tree_farm)

pumpkinFarm.farm((0,0),(7,7))
fillFarm.farm((0,0),(15,3),needs)
#boneFarm.farm()
