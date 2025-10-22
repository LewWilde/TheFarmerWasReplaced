
def plant_tree():   
	
	if get_ground_type() != Grounds.Grassland :
		till()

	if get_pos_x() % 2 != get_pos_y() % 2:
	
		if get_entity_type() != Entities.Tree:
			plant(Entities.Tree)