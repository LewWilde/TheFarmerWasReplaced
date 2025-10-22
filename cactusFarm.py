from __builtins__ import *

import drone

def farm(xy,xy2):

	
	x1, y1 = xy
	x2, y2 = xy2

	def loop():
		drone.go_to(xy)
		plant_phase()

		for i in range(x2 - x1): 
			sorting_phase()

		drone.go_to(xy2)
		harvest()

		loop()
	
	def plant_phase():

		planting = True

		while planting:
			
			while get_pos_y() <= y2:
				
				while get_pos_x() <= x2:
					
					if can_harvest():
						harvest()

					if(get_ground_type() != Grounds.Soil):
						till()

					plant(Entities.Cactus)

					if(get_pos_x() < x2):
						move(East)
					else:
						break
				if(get_pos_x() == x2):
					drone.go_to((x1, get_pos_y()))

				if(get_pos_y() == y2):
						drone.go_to(xy)
						planting = False
						break
				else:
					move(North)


	def sorting_phase():

		sorting = True

		while sorting:
			
			while get_pos_y() <= y2:
				
				while get_pos_x() <= x2:

					current = measure()
					right = measure(East)
					top = measure(North)

					if(top != None and current > top):
						swap(North)
						current = top

					if(right != None and current > right):
						swap(East)
						current = right
						
					

					if(get_pos_x() < x2):
						move(East)
					else:
						break
				if(get_pos_x() == x2):
					drone.go_to((x1, get_pos_y()))

				if(get_pos_y() == y2):
						drone.go_to(xy)
						sorting = False
						break
				else:
					move(North)

	loop()





