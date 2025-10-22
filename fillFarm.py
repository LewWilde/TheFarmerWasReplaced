from __builtins__ import *

import drone
from plantList import *

def farm(xy,xy2,entityList):

	x1, y1 = xy
	x2, y2 = xy2
	w = x2 - x1
	h = y2 - y1
	entityLength = len(entityList)
	plots = []

	def loop():
		drone.go_to(xy)
		plant_phase()
		scan_phase()
		loop()
	
	def plant_phase():

		y = get_pos_y()
		ry = 0
		x = get_pos_x()
		rx = 0
			
		while y <= y2:
				
			y = get_pos_y()
			ry = y - y1

			while x <= x2:
					x = get_pos_x()
					rx = x - x1
					entity = entityList[rx % entityLength]
					ideal_ground = plantList[entity]
					
					if(can_harvest()):
						harvest()

					if(get_ground_type() != ideal_ground and ideal_ground != 'any'):
						till()

					plots.append((x,y))

					plant_entity(entity)
				
					if(x < x2): 
						move(East)
					else:
						break
			if(x == x2):
				drone.go_to((x1, y))

			if(y == y2):
				break
			else:
				move(North)
	def scan_phase():

		while True:

			plot = plots.pop(0)
			drone.go_to(plot)
			x,y = plot

			if(can_harvest()):
				harvest()
				rx = x - x1
				entity = entityList[rx % entityLength]
				plant_entity(entity)
			else:
				use_item(Items.Water)
			
			plots.append(plot)
	
	def plant_entity(entity):
		if(entity == Entities.Grass):
			return

		if(entity == Entities.Tree):
			if(get_pos_x() % 2 != get_pos_y() % 2):
				plant(entity)
			#else: 
				#plant(Entities.Bush)
		else:
			plant(entity)

	loop()




	