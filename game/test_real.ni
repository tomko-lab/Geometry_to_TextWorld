[define indoor_room]
indoor_room is a kind of room.
indoor_room has a text called description.
indoor_room has a text called printed name.

[define area]
area is a kind of room.
area has a text called description.
area has a text called printed name.
area has a indoor_room called parent.
area can be enterable.
area is always enterable.

player has a number called orientation.


[define landmark]
landmark is a kind of thing.
landmark has a text called description.
landmark has a text called printed name.
landmark can be examined.
area has a list of landmark called visible_objects.

[create r0]
r0 is a indoor_room. "Room 0".

[create r1]
r1 is a indoor_room. "Room 1".

[create r2]
r2 is a indoor_room. "Room 2".

[create r3]
r3 is a indoor_room. "Room 3".

[create r4]
r4 is a indoor_room. "Room 4".

[create r5]
r5 is a indoor_room. "Room 5".

[create r6]
r6 is a indoor_room. "Room 6".

[create r7]
r7 is a indoor_room. "Room 7".

[create r8]
r8 is a indoor_room. "Room 8".

[create r9]
r9 is a indoor_room. "Room 9".

[create a0r0]
a0r0 is a area. "An area (0) in [parent]".
the printed name of the a0r0 is "Room 0".
Understand "Area 0 in Room 0" as a0r0.
the parent of the a0r0 is r0.

[create a0r1]
a0r1 is a area. "An area (0) in [parent]".
the printed name of the a0r1 is "Room 1".
Understand "Area 0 in Room 1" as a0r1.
the parent of the a0r1 is r1.

[create a1r1]
a1r1 is a area. "An area (1) in [parent]".
the printed name of the a1r1 is "Room 1".
Understand "Area 1 in Room 1" as a1r1.
the parent of the a1r1 is r1.

[create a2r1]
a2r1 is a area. "An area (2) in [parent]".
the printed name of the a2r1 is "Room 1".
Understand "Area 2 in Room 1" as a2r1.
the parent of the a2r1 is r1.

[create a3r1]
a3r1 is a area. "An area (3) in [parent]".
the printed name of the a3r1 is "Room 1".
Understand "Area 3 in Room 1" as a3r1.
the parent of the a3r1 is r1.

[create a4r1]
a4r1 is a area. "An area (4) in [parent]".
the printed name of the a4r1 is "Room 1".
Understand "Area 4 in Room 1" as a4r1.
the parent of the a4r1 is r1.

[create a0r2]
a0r2 is a area. "An area (0) in [parent]".
the printed name of the a0r2 is "Room 2".
Understand "Area 0 in Room 2" as a0r2.
the parent of the a0r2 is r2.

[create a0r3]
a0r3 is a area. "An area (0) in [parent]".
the printed name of the a0r3 is "Room 3".
Understand "Area 0 in Room 3" as a0r3.
the parent of the a0r3 is r3.

[create a1r3]
a1r3 is a area. "An area (1) in [parent]".
the printed name of the a1r3 is "Room 3".
Understand "Area 1 in Room 3" as a1r3.
the parent of the a1r3 is r3.

[create a2r3]
a2r3 is a area. "An area (2) in [parent]".
the printed name of the a2r3 is "Room 3".
Understand "Area 2 in Room 3" as a2r3.
the parent of the a2r3 is r3.

[create a3r3]
a3r3 is a area. "An area (3) in [parent]".
the printed name of the a3r3 is "Room 3".
Understand "Area 3 in Room 3" as a3r3.
the parent of the a3r3 is r3.

[create a4r3]
a4r3 is a area. "An area (4) in [parent]".
the printed name of the a4r3 is "Room 3".
Understand "Area 4 in Room 3" as a4r3.
the parent of the a4r3 is r3.

[create a5r3]
a5r3 is a area. "An area (5) in [parent]".
the printed name of the a5r3 is "Room 3".
Understand "Area 5 in Room 3" as a5r3.
the parent of the a5r3 is r3.

[create a6r3]
a6r3 is a area. "An area (6) in [parent]".
the printed name of the a6r3 is "Room 3".
Understand "Area 6 in Room 3" as a6r3.
the parent of the a6r3 is r3.

[create a7r3]
a7r3 is a area. "An area (7) in [parent]".
the printed name of the a7r3 is "Room 3".
Understand "Area 7 in Room 3" as a7r3.
the parent of the a7r3 is r3.

[create a8r3]
a8r3 is a area. "An area (8) in [parent]".
the printed name of the a8r3 is "Room 3".
Understand "Area 8 in Room 3" as a8r3.
the parent of the a8r3 is r3.

[create a0r4]
a0r4 is a area. "An area (0) in [parent]".
the printed name of the a0r4 is "Room 4".
Understand "Area 0 in Room 4" as a0r4.
the parent of the a0r4 is r4.

[create a0r5]
a0r5 is a area. "An area (0) in [parent]".
the printed name of the a0r5 is "Room 5".
Understand "Area 0 in Room 5" as a0r5.
the parent of the a0r5 is r5.

[create a0r6]
a0r6 is a area. "An area (0) in [parent]".
the printed name of the a0r6 is "Room 6".
Understand "Area 0 in Room 6" as a0r6.
the parent of the a0r6 is r6.

[create a0r7]
a0r7 is a area. "An area (0) in [parent]".
the printed name of the a0r7 is "Room 7".
Understand "Area 0 in Room 7" as a0r7.
the parent of the a0r7 is r7.

[create a0r8]
a0r8 is a area. "An area (0) in [parent]".
the printed name of the a0r8 is "Room 8".
Understand "Area 0 in Room 8" as a0r8.
the parent of the a0r8 is r8.

[create a1r8]
a1r8 is a area. "An area (1) in [parent]".
the printed name of the a1r8 is "Room 8".
Understand "Area 1 in Room 8" as a1r8.
the parent of the a1r8 is r8.

[create a2r8]
a2r8 is a area. "An area (2) in [parent]".
the printed name of the a2r8 is "Room 8".
Understand "Area 2 in Room 8" as a2r8.
the parent of the a2r8 is r8.

[create a3r8]
a3r8 is a area. "An area (3) in [parent]".
the printed name of the a3r8 is "Room 8".
Understand "Area 3 in Room 8" as a3r8.
the parent of the a3r8 is r8.

[create a4r8]
a4r8 is a area. "An area (4) in [parent]".
the printed name of the a4r8 is "Room 8".
Understand "Area 4 in Room 8" as a4r8.
the parent of the a4r8 is r8.

[create a5r8]
a5r8 is a area. "An area (5) in [parent]".
the printed name of the a5r8 is "Room 8".
Understand "Area 5 in Room 8" as a5r8.
the parent of the a5r8 is r8.

[create a0r9]
a0r9 is a area. "An area (0) in [parent]".
the printed name of the a0r9 is "Room 9".
Understand "Area 0 in Room 9" as a0r9.
the parent of the a0r9 is r9.

[create a1r9]
a1r9 is a area. "An area (1) in [parent]".
the printed name of the a1r9 is "Room 9".
Understand "Area 1 in Room 9" as a1r9.
the parent of the a1r9 is r9.

[create a2r9]
a2r9 is a area. "An area (2) in [parent]".
the printed name of the a2r9 is "Room 9".
Understand "Area 2 in Room 9" as a2r9.
the parent of the a2r9 is r9.

[create a3r9]
a3r9 is a area. "An area (3) in [parent]".
the printed name of the a3r9 is "Room 9".
Understand "Area 3 in Room 9" as a3r9.
the parent of the a3r9 is r9.

[create a4r9]
a4r9 is a area. "An area (4) in [parent]".
the printed name of the a4r9 is "Room 9".
Understand "Area 4 in Room 9" as a4r9.
the parent of the a4r9 is r9.

north of a0r1 is south of a1r1.

southeast of a0r1 is northwest of a2r1.

south of a1r1 is north of a0r1.

northwest of a2r1 is southeast of a0r1.

east of a2r1 is west of a3r1.

west of a3r1 is east of a2r1.

northeast of a3r1 is southwest of a4r1.

southwest of a4r1 is northeast of a3r1.

north of a0r3 is south of a1r3.

south of a1r3 is north of a0r3.

east of a1r3 is west of a2r3.

west of a2r3 is east of a1r3.

south of a2r3 is north of a3r3.

east of a2r3 is west of a4r3.

north of a2r3 is south of a5r3.

north of a3r3 is south of a2r3.

west of a4r3 is east of a2r3.

south of a4r3 is north of a6r3.

east of a4r3 is west of a7r3.

north of a4r3 is south of a8r3.

south of a5r3 is north of a2r3.

north of a6r3 is south of a4r3.

west of a7r3 is east of a4r3.

south of a8r3 is north of a4r3.

southeast of a0r8 is northwest of a1r8.

northwest of a1r8 is southeast of a0r8.

southeast of a1r8 is northwest of a2r8.

northeast of a1r8 is southwest of a3r8.

northwest of a2r8 is southeast of a1r8.

south of a2r8 is north of a4r8.

southwest of a3r8 is northeast of a1r8.

north of a3r8 is south of a5r8.

north of a4r8 is south of a2r8.

south of a5r8 is north of a3r8.

northeast of a0r9 is southwest of a1r9.

southwest of a1r9 is northeast of a0r9.

east of a1r9 is west of a2r9.

west of a2r9 is east of a1r9.

southeast of a2r9 is northwest of a3r9.

northwest of a3r9 is southeast of a2r9.

south of a3r9 is north of a4r9.

north of a4r9 is south of a3r9.

[create d0]
d0 is a door. "Door Room 2 to Room 3".
d0 is west of a1r3 and east of a0r2.

[create d1]
d1 is a door. "Door Room 1 to Room 2".
d1 is south of a2r1 and north of a0r2.

[create d2]
d2 is a door. "Door Room 1 to Room 4".
d2 is northeast of a4r1 and southwest of a0r4.

[create d3]
d3 is a door. "Door Room 3 to Room 4".
d3 is north of a5r3 and south of a0r4.

[create d4]
d4 is a door. "Door Room 3 to Room 5".
d4 is north of a8r3 and south of a0r5.

[create d5]
d5 is a door. "Door Room 4 to Room 5".
d5 is west of a0r5 and east of a0r4.

[create d6]
d6 is a door. "Door Room 5 to Room 8".
d6 is northwest of a0r8 and southeast of a0r5.

[create d7]
d7 is a door. "Door Room 3 to Room 7".
d7 is south of a6r3 and north of a0r7.

[create d8]
d8 is a door. "Door Room 7 to Room 9".
d8 is west of a0r9 and east of a0r7.

[create d9]
d9 is a door. "Door Room 3 to Room 6".
d9 is south of a0r3 and north of a0r6.

[create d10]
d10 is a door. "Door Room 3 to Room 8".
d10 is east of a7r3 and west of a4r8.

[create d11]
d11 is a door. "Door Room 0 to Room 8".
d11 is west of a0r0 and east of a4r8.

[create d12]
d12 is a door. "Door Room 8 to Room 9".
d12 is south of a4r8 and north of a2r9.

[create landmark0]
landmark0 is a landmark. "Pear".
the printed name of the landmark0 is "Landmark 0".
Understand "Landmark 0" as landmark0.
the landmark0 is in a1r1.

[create landmark1]
landmark1 is a landmark. "Banana".
the printed name of the landmark1 is "Landmark 1".
Understand "Landmark 1" as landmark1.
the landmark1 is in a3r3.

[create landmark2]
landmark2 is a landmark. "Apple".
the printed name of the landmark2 is "Landmark 2".
Understand "Landmark 2" as landmark2.
the landmark2 is in a4r9.

[create landmark3]
landmark3 is a landmark. "Exit is in this room!".
the printed name of the landmark3 is "Landmark 3".
Understand "Landmark 3" as landmark3.
the landmark3 is in a0r8.

[create landmark4]
landmark4 is a landmark. "Move toward North or East!".
the printed name of the landmark4 is "Landmark 4".
Understand "Landmark 4" as landmark4.
the landmark4 is in a0r9.

[create landmark5]
landmark5 is a landmark. "Move toward East!".
the printed name of the landmark5 is "Landmark 5".
Understand "Landmark 5" as landmark5.
the landmark5 is in a2r3.



the visible_objects of the a1r1 is {landmark0}.







the visible_objects of the a2r3 is {landmark5}.

the visible_objects of the a3r3 is {landmark1}.










the visible_objects of the a0r8 is {landmark3}.






the visible_objects of the a0r9 is {landmark4}.




the visible_objects of the a4r9 is {landmark2}.

Definition: a direction (called thatway) is viable if the room thatway from the location is not nowhere.

nLooking is a number that varies. nLooking is 0. 
dirNumber is a number that varies.
dirNumber is 0. 
relDirDesc is a text that varies. 

[describe areas and rooms]
After looking:
	now nLooking is 1; 
	let accessibleRooms be a list of rooms;
	let accessibleAreas be a list of areas;
	let pDirections be list of viable directions;
	let parentSource be the parent of the location of player;
	let relDirs be a list of number;
	repeat with dirToLookAt running through pDirections:
		try silently going dirToLookAt;
		if rule succeeded:
			now dirNumber is 0;
			if "[dirToLookAt]" is "south":
				now dirNumber is 4;
			if "[dirToLookAt]" is "east":
				now dirNumber is 6;
			if "[dirToLookAt]" is "west":
				now dirNumber is 2;
			if "[dirToLookAt]" is "northwest":
				now dirNumber is 1;
			if "[dirToLookAt]" is "southwest":
				now dirNumber is 3;
			if "[dirToLookAt]" is "southeast":
				now dirNumber is 5;
			if "[dirToLookAt]" is "northeast":
				now dirNumber is 7;
			let relDir be the remainder after dividing the orientation of the player - dirNumber + 80 by 8;
			add relDir to relDirs;
			if relDir is 0:
				now relDirDesc is "at the front";
			if relDir is 1:
				now relDirDesc is "at the slight right";
			if relDir is 2:
				now relDirDesc is "at the right";
			if relDir is 3:
				now relDirDesc is "at the sharp right";
			if relDir is 4:
				now relDirDesc is "at the back";
			if relDir is 5:
				now relDirDesc is "at the sharp left";
			if relDir is 6:
				now relDirDesc is "at the left";
			if relDir is 7:
				now relDirDesc is "at the slight left";
			let destinationParent be the parent of the location of the player;
			if "[parentSource]" is "[destinationParent]":
				say "You can continue in the [parentSource] by going [dirToLookAt] ([relDirDesc])[line break]";
				add the location of the player to accessibleAreas;
			otherwise:
				say "You can enter the [destinationParent] by going [dirToLookAt] ([relDirDesc])[line break]";
				add the destinationParent to accessibleRooms;
			try silently going the opposite of dirToLookAt;
	repeat with vO running through the visible_objects of the location:
		say "[vO] is visible from here, but too far! You can move in this room to examine or access [it]";
	now nLooking is 0.
Before going through a locked door when nLooking is 1:
	stop the action.
Going front is an action applying to nothing. Understand "go front" as going front.

Check going front:
	if the orientation of the player is:
		-- 0: try the player going north;
		-- 1: try the player going northwest;
		-- 2: try the player going west;
		-- 3: try the player going southwest;
		-- 4: try the player going south;
		-- 5: try the player going southeast;
		-- 6: try the player going east;
		-- 7: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".


Going back is an action applying to nothing. Understand "go back" as going back.

Check going back:
	if the orientation of the player is:
		-- 4: try the player going north;
		-- 5: try the player going northwest;
		-- 6: try the player going west;
		-- 7: try the player going southwest;
		-- 0: try the player going south;
		-- 1: try the player going southeast;
		-- 2: try the player going east;
		-- 3: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".



Going left is an action applying to nothing. Understand "go left" as going left.

Check going left:
	if the orientation of the player is:
		-- 6: try the player going north;
		-- 7: try the player going northwest;
		-- 0: try the player going west;
		-- 1: try the player going southwest;
		-- 2: try the player going south;
		-- 3: try the player going southeast;
		-- 4: try the player going east;
		-- 5: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".


Going right is an action applying to nothing. Understand "go right" as going right.

Check going right:
	if the orientation of the player is:
		-- 2: try the player going north;
		-- 3: try the player going northwest;
		-- 4: try the player going west;
		-- 5: try the player going southwest;
		-- 6: try the player going south;
		-- 7: try the player going southeast;
		-- 0: try the player going east;
		-- 1: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".

Going sharp right is an action applying to nothing. Understand "go sharp right" as going sharp right.
Going slight right is an action applying to nothing. Understand "go slight right" as going slight right.
Going sharp left is an action applying to nothing. Understand "go sharp left" as going sharp left.
Going slight left is an action applying to nothing. Understand "go slight left" as going slight left.

Check going sharp right:
	if the orientation of the player is:
		-- 3: try the player going north;
		-- 4: try the player going northwest;
		-- 5: try the player going west;
		-- 6: try the player going southwest;
		-- 7: try the player going south;
		-- 0: try the player going southeast;
		-- 1: try the player going east;
		-- 2: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".

Check going slight right:
	if the orientation of the player is:
		-- 1: try the player going north;
		-- 2: try the player going northwest;
		-- 3: try the player going west;
		-- 4: try the player going southwest;
		-- 5: try the player going south;
		-- 6: try the player going southeast;
		-- 7: try the player going east;
		-- 0: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".

Check going sharp left:
	if the orientation of the player is:
		-- 5: try the player going north;
		-- 6: try the player going northwest;
		-- 7: try the player going west;
		-- 0: try the player going southwest;
		-- 1: try the player going south;
		-- 2: try the player going southeast;
		-- 3: try the player going east;
		-- 4: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".

Check going slight left:
	if the orientation of the player is:
		-- 7: try the player going north;
		-- 0: try the player going northwest;
		-- 1: try the player going west;
		-- 2: try the player going southwest;
		-- 3: try the player going south;
		-- 4: try the player going southeast;
		-- 5: try the player going east;
		-- 6: try the player going northeast;
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".


Instead of going north:
	if nLooking is 0:
		now the orientation of the player is 0;
	continue the action.

Instead of going south:
	if nLooking is 0:
		now the orientation of the player is 4;
	continue the action.

Instead of going east:
	if nLooking is 0:
		now the orientation of the player is 6;
	continue the action.

Instead of going west:
	if nLooking is 0:
		now the orientation of the player is 2;
	continue the action.

Instead of going northwest:
	if nLooking is 0:
		now the orientation of the player is 1;
	continue the action.

Instead of going southwest:
	if nLooking is 0:
		now the orientation of the player is 3;
	continue the action.

Instead of going northeast:
	if nLooking is 0:
		now the orientation of the player is 7;
	continue the action.

Instead of going southeast:
	if nLooking is 0:
		now the orientation of the player is 5;
	continue the action.

Understand "veer left" as going slight left.
Understand "veer right" as going slight right.
Understand "turn left" as going left.
Understand "turn right" as going right.
Understand "turn sharp left" as going sharp left.
Understand "turn sharp right" as going sharp right.
the player is in a1r1.

the orientation of the player is 4.

nInteraction is a number that varies.
nInteraction is 0.
Every turn:
	now nInteraction is nInteraction + 1;
	if the player is in a0r0:
		say "Yayyyyyyyyy!!!!!";
		end the story finally saying "You have won!";
	otherwise:
		if nInteraction is 15:
			say "It's too late to go further I am sorry to inform you that you are dead!!!";
			end the story saying "You have died!";
		otherwise:
			say "[nInteraction] minutes has passed, decide well in your future actions, you have limited time [15 - nInteraction] minutes".