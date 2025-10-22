from __builtins__ import *

from carrots import *
from trees import *
from grass import *
from pumpkins import *
from sunflowers import *

plants = [plant_tree,plant_tree,plant_carrot,plant_carrot,plant_pumpkin,plant_pumpkin,plant_pumpkin,plant_sunflower]

while True:
	
	for iy in range(get_world_size()):
		

		move(North)

		for ix in range(get_world_size()):
			
			if can_harvest():
				harvest()

			plant_item = plants[get_pos_x()]

			plant_item()

			#if get_ground_type() == Grounds.Soil:
			#	if get_water() <= 0.75:
			#			use_item(Items.Water)

			move(East)

		

		