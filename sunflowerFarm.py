from __builtins__ import *

import drone

def farm(xy,xy2):

	
	x1, y1 = xy
	x2, y2 = xy2

	plots = {}

	def loop():
		drone.go_to(xy)
		plant_phase()
		scan_phase()

		loop()
	
	def plant_phase():

		y = get_pos_y()
		x = get_pos_x()
			
		while y <= y2:
			
			y = get_pos_y()

			while x <= x2:
				x = get_pos_x()
				
				if(can_harvest() and get_entity_type() != Entities.Sunflower):
					harvest()

				if(get_ground_type() != Grounds.Soil):
					till()

				plant_flower((x,y))

				if(x < x2): 
					move(East)
				else:
					break
			if(x == x2):
				drone.go_to((x1, y))

			if(y == y2):
					drone.go_to(xy)
					break
			else:
				move(North)
				


	def scan_phase():

		while True:

			plot = get_biggest_flower()
			drone.go_to(plot)

			if(can_harvest()):
				harvest()
				plant_flower(plot)
			else:
				if(get_water() <= 0.75):
					use_item(Items.Water)
		
	def plant_flower(xy):
		plant(Entities.Sunflower)
		petals = measure()
		plots[xy]= petals
		
	def get_biggest_flower():
		biggest = False
		for key in plots:
			if(biggest == False):
				biggest = key
				continue

			if plots[key] > plots[biggest]:
				biggest = key

		return biggest

	loop()





	