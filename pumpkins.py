def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
		
	if get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)
		
	return