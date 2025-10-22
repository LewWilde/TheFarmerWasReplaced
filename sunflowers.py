def plant_sunflower():
	if get_ground_type() != Grounds.Soil:
		till()
		
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
		
	return