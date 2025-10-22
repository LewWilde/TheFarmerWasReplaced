
def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
		
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
		
	return