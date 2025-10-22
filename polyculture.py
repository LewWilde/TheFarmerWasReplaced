import garden
import drone

garden.init()

while True:

	#use_item(Items.Fertilizer)

	companion = get_companion()

	if(companion):
		entity, xy = companion
		drone.go_to(xy)
		garden.update_plot(xy, companion[0])

	