from __builtins__ import *

import drone

def farm(xy,xy2):

	
	x1, y1 = xy
	x2, y2 = xy2

	plots = []

	def loop():
		drone.go_to(xy)
		plant_phase()
		scan_phase()

		loop()
	
	def plant_phase():

		planting = True
		y = get_pos_y()
		x = get_pos_x()

		while planting:
			
			while y <= y2:
				
				y = get_pos_y()

				while x <= x2:
					x = get_pos_x()
					
					if(can_harvest() and get_entity_type() != Entities.Pumpkin):
						harvest()

					if(get_ground_type() != Grounds.Soil):
						till()

					plant(Entities.Pumpkin)
					
					plots.append((x,y))

					if(x < x2): 
						move(East)
					else:
						break
				if(x == x2):
					drone.go_to((x1, y))

				if(y == y2):
						drone.go_to(xy)
						planting = False
						break
				else:
					move(North)

	def scan_phase():

		while True:

			if(len(plots) < 1):
				break

			plot = plots.pop(0)
			drone.go_to(plot)

			if(can_harvest() == False):
				plots.append(plot)
				plant(Entities.Pumpkin)
				use_item(Items.Water)
		
		harvest()

	loop()





	