from __builtins__ import *

import drone
from plantList import *

global size

def farm():
	
	size = 0

	def init():
		change_hat(Hats.Straw_Hat)
		drone.go_to((0,0))
		if(can_harvest()):
			harvest()
		change_hat(Hats.Dinosaur_Hat)
		loop()


	def loop():

		dir = East
		

		while True:
				x = get_pos_x()
				y = get_pos_y()
				w = get_world_size() - 1

				checkForApples()
				if(x == 0 and y == w):
					drone.go_to((0,0),False,checkForApples)

				if(x == 1 and y > 0 and y != w):
					move(North)
					dir = East

				moved = move(dir)
				if(moved == False):
					move(North)
					if(dir == East):
						dir = West
					else:
						dir = East

	def checkForApples():
		if(get_entity_type() == Entities.Apple):
			global size
			size += 1
			w = get_world_size() ** 2
			if(size > (w -1)):
				change_hat(Hats.Straw_Hat)
				change_hat(Hats.Dinosaur_Hat)
				size = 0
	
	init()




	