# general concept definitions
DEFINE_CONCEPT = '[define {concept}]\n{concept} is a kind of {kind}.\n'
DEFINE_CONCEPT_PROPERTY = '{concept} has a {kind} called {var}.\n'
DEFINE_CONCEPT_ABLE = '{concept} can be {ability}.\n'
DEFINE_CONCEPT_ALWAYS_ABLE = '{concept} is always {ability}.\n'

# create instance of concepts
DEFINE_INSTANCE = '[create {instance}]\n{instance} is a {concept}. "{description}".\n'
DEFINE_INSTANCE_PROPERTY = 'the {property} of the {instance} is {value}.\n'

# define relationships
DEFINE_DIRECTION_AREAS = '{relation} of {area1} is {rev_relation} of {area2}.\n'
DEFINE_DIRECTION_AREAS_DOORS = '{door} is {relation} of {area1} and {rev_relation} of {area2}.\n'

# understand
UNDERSTAND_AS = 'Understand "{text}" as {variable}.\n'

# in area
SET_IN_AREA = 'the {thing} is in {area}.\n'


# quest definition
QUESTI_DEFINITION = 'nInteraction is a number that varies.\n\
nInteraction is 0.\n\
Every turn:\n\
	now nInteraction is nInteraction + 1;\n\
	if the player is in {win_area}:\n\
		say "Yayyyyyyyyy!!!!!";\n\
		end the story finally saying "You have won!";\n\
	otherwise:\n\
		if nInteraction is {max_interaction}:\n\
			say "It\'s too late to go further I am sorry to inform you that you are dead!!!";\n\
			end the story saying "You have died!";\n\
		otherwise:\n\
			say "[nInteraction] minutes has passed, decide well in your future actions, you have limited time' \
                    ' [{max_interaction} - nInteraction] minutes".'


# fixed definitions
FIXED_VIABLE_DIRECTIONS = "Definition: a direction (called thatway) is viable if the room \
thatway from the location is not nowhere.\n"

# fixed actions
FIXED_ACTIONS = 'nLooking is a number that varies. nLooking is 0. \n\
dirNumber is a number that varies.\n\
dirNumber is 0. \n\
relDirDesc is a text that varies. \n\
\n\
[describe areas and rooms]\n\
After looking:\n\
	now nLooking is 1; \n\
	let accessibleRooms be a list of rooms;\n\
	let accessibleAreas be a list of areas;\n\
	let pDirections be list of viable directions;\n\
	let parentSource be the parent of the location of player;\n\
	let relDirs be a list of number;\n\
	repeat with dirToLookAt running through pDirections:\n\
		try silently going dirToLookAt;\n\
		if rule succeeded:\n\
			now dirNumber is 0;\n\
			if "[dirToLookAt]" is "south":\n\
				now dirNumber is 4;\n\
			if "[dirToLookAt]" is "east":\n\
				now dirNumber is 6;\n\
			if "[dirToLookAt]" is "west":\n\
				now dirNumber is 2;\n\
			if "[dirToLookAt]" is "northwest":\n\
				now dirNumber is 1;\n\
			if "[dirToLookAt]" is "southwest":\n\
				now dirNumber is 3;\n\
			if "[dirToLookAt]" is "southeast":\n\
				now dirNumber is 5;\n\
			if "[dirToLookAt]" is "northeast":\n\
				now dirNumber is 7;\n\
			let relDir be the remainder after dividing the orientation of the player - dirNumber + 80 by 8;\n\
			add relDir to relDirs;\n\
			if relDir is 0:\n\
				now relDirDesc is "at the front";\n\
			if relDir is 1:\n\
				now relDirDesc is "at the slight right";\n\
			if relDir is 2:\n\
				now relDirDesc is "at the right";\n\
			if relDir is 3:\n\
				now relDirDesc is "at the sharp right";\n\
			if relDir is 4:\n\
				now relDirDesc is "at the back";\n\
			if relDir is 5:\n\
				now relDirDesc is "at the sharp left";\n\
			if relDir is 6:\n\
				now relDirDesc is "at the left";\n\
			if relDir is 7:\n\
				now relDirDesc is "at the slight left";\n\
			let destinationParent be the parent of the location of the player;\n\
			if "[parentSource]" is "[destinationParent]":\n\
				say "You can continue in the [parentSource] by going [dirToLookAt] ([relDirDesc])[line break]";\n\
				add the location of the player to accessibleAreas;\n\
			otherwise:\n\
				say "You can enter the [destinationParent] by going [dirToLookAt] ([relDirDesc])[line break]";\n\
				add the destinationParent to accessibleRooms;\n\
			try silently going the opposite of dirToLookAt;\n\
	repeat with vO running through the visible_objects of the location:\n\
		say "[vO] is visible from here, but too far! You can move in this room to examine or access [it]";\n\
	now nLooking is 0.\n\
Before going through a locked door when nLooking is 1:\n\
	stop the action.'

FIXED_DIRECTION_DEFINITION = 'Going front is an action applying to nothing. Understand "go front" as going front.\n\
\n\
Check going front:\n\
	if the orientation of the player is:\n\
		-- 0: try the player going north;\n\
		-- 1: try the player going northwest;\n\
		-- 2: try the player going west;\n\
		-- 3: try the player going southwest;\n\
		-- 4: try the player going south;\n\
		-- 5: try the player going southeast;\n\
		-- 6: try the player going east;\n\
		-- 7: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
\n\
Going back is an action applying to nothing. Understand "go back" as going back.\n\
\n\
Check going back:\n\
	if the orientation of the player is:\n\
		-- 4: try the player going north;\n\
		-- 5: try the player going northwest;\n\
		-- 6: try the player going west;\n\
		-- 7: try the player going southwest;\n\
		-- 0: try the player going south;\n\
		-- 1: try the player going southeast;\n\
		-- 2: try the player going east;\n\
		-- 3: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
\n\
\n\
Going left is an action applying to nothing. Understand "go left" as going left.\n\
\n\
Check going left:\n\
	if the orientation of the player is:\n\
		-- 6: try the player going north;\n\
		-- 7: try the player going northwest;\n\
		-- 0: try the player going west;\n\
		-- 1: try the player going southwest;\n\
		-- 2: try the player going south;\n\
		-- 3: try the player going southeast;\n\
		-- 4: try the player going east;\n\
		-- 5: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
\n\
Going right is an action applying to nothing. Understand "go right" as going right.\n\
\n\
Check going right:\n\
	if the orientation of the player is:\n\
		-- 2: try the player going north;\n\
		-- 3: try the player going northwest;\n\
		-- 4: try the player going west;\n\
		-- 5: try the player going southwest;\n\
		-- 6: try the player going south;\n\
		-- 7: try the player going southeast;\n\
		-- 0: try the player going east;\n\
		-- 1: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
Going sharp right is an action applying to nothing. Understand "go sharp right" as going sharp right.\n\
Going slight right is an action applying to nothing. Understand "go slight right" as going slight right.\n\
Going sharp left is an action applying to nothing. Understand "go sharp left" as going sharp left.\n\
Going slight left is an action applying to nothing. Understand "go slight left" as going slight left.\n\
\n\
Check going sharp right:\n\
	if the orientation of the player is:\n\
		-- 3: try the player going north;\n\
		-- 4: try the player going northwest;\n\
		-- 5: try the player going west;\n\
		-- 6: try the player going southwest;\n\
		-- 7: try the player going south;\n\
		-- 0: try the player going southeast;\n\
		-- 1: try the player going east;\n\
		-- 2: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
Check going slight right:\n\
	if the orientation of the player is:\n\
		-- 1: try the player going north;\n\
		-- 2: try the player going northwest;\n\
		-- 3: try the player going west;\n\
		-- 4: try the player going southwest;\n\
		-- 5: try the player going south;\n\
		-- 6: try the player going southeast;\n\
		-- 7: try the player going east;\n\
		-- 0: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
Check going sharp left:\n\
	if the orientation of the player is:\n\
		-- 5: try the player going north;\n\
		-- 6: try the player going northwest;\n\
		-- 7: try the player going west;\n\
		-- 0: try the player going southwest;\n\
		-- 1: try the player going south;\n\
		-- 2: try the player going southeast;\n\
		-- 3: try the player going east;\n\
		-- 4: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
Check going slight left:\n\
	if the orientation of the player is:\n\
		-- 7: try the player going north;\n\
		-- 0: try the player going northwest;\n\
		-- 1: try the player going west;\n\
		-- 2: try the player going southwest;\n\
		-- 3: try the player going south;\n\
		-- 4: try the player going southeast;\n\
		-- 5: try the player going east;\n\
		-- 6: try the player going northeast;\n\
		-- otherwise: say "Yaaaaaa Babaaaaam!!!".\n\
\n\
\n\
Instead of going north:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 0;\n\
	continue the action.\n\
\n\
Instead of going south:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 4;\n\
	continue the action.\n\
\n\
Instead of going east:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 6;\n\
	continue the action.\n\
\n\
Instead of going west:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 2;\n\
	continue the action.\n\
\n\
Instead of going northwest:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 1;\n\
	continue the action.\n\
\n\
Instead of going southwest:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 3;\n\
	continue the action.\n\
\n\
Instead of going northeast:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 7;\n\
	continue the action.\n\
\n\
Instead of going southeast:\n\
	if nLooking is 0:\n\
		now the orientation of the player is 5;\n\
	continue the action.\n'

FIXED_ALTERNATIVE_NAMES = 'Understand "veer left" as going slight left.\n\
Understand "veer right" as going slight right.\n\
Understand "turn left" as going left.\n\
Understand "turn right" as going right.\n\
Understand "turn sharp left" as going sharp left.\n\
Understand "turn sharp right" as going sharp right.'

if __name__ == "__main__":
    print(FIXED_ACTIONS)