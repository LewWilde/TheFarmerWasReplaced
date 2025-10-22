def go_to(xy = (0,0)):

	x , y = xy
	w = get_world_size()
	halfW = w /2

	cx = get_pos_x() 
	cy = get_pos_y()

	xDistance =  x - cx
	yDistance =  y - cy

	xDir = East
	yDir = North

	if((xDistance < 0 and xDistance > 0-halfW) or (xDistance > halfW and xDistance < w) ):
		xDir = West

	if((yDistance < 0 and yDistance > 0-halfW) or (yDistance > halfW and yDistance < w) ):
		yDir = South

	#print(yDir)
	#print(xDir)

	while(get_pos_x() != x):
		move(xDir)

	while(get_pos_y() != y):
		move(yDir)