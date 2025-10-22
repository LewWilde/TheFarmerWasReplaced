headings = [North, East, South, West]
check = [1,0,-1,2]

while True:

	plant(Entities.Bush)
	use_item(Items.Weird_Substance, 8)
	has_treasure = False
	heading = 1

	while not has_treasure:

		if (get_entity_type() == Entities.Treasure):
			harvest()
			has_treasure = True
			break
		for i in check:
			
			h = (heading + i) % 4
			if(can_move(headings[h])):
				heading = h
				break
		move(headings[heading])

	