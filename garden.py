import drone
from plantList import plantList

plots = {}

def init():
	clear()
	w = get_world_size()
	x = 0
	while x < w:
		y = 0
		while y < w:
			plots[(x,y)] = create_plot()
			y +=1
		x +=1

def create_plot(entity = Entities.Grass, ground = Grounds.Grassland, time = get_time()):

	plot = {
		'entity':entity, 
		'ground':ground, 
		'time':time
	}

	return plot

def update_plot(xy, entity):
	
	if(can_harvest()):
		harvest()
	
	plot = plots[xy]

	plot['entity'] = entity
	plot['time'] = get_time()
	
	ground = plantList[entity]

	if(ground != 'any'):
		plot['ground'] = ground
		till()
		
	plant(entity)
