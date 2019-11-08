# This module is comprised of 3 classes. The point, robot and path class. 
# The point class makes a x1 y1 point. 
# The robot class creates a robot with a (x1, y1) coordinate
# The robot class contatins the moveRobot() function which allows 
# the user to move the robot "N" (North)"S"(South) "E"(East) "W"(West) position on the coodinate plane.
# The path class has both the robot and treasure coordinates and will keep track of all of the unique shortest paths 
# from the robot to the treasure. The unique shortest paths will be stored in a list
##***************************************************************************************************

#craetes a x y point sets and gets x and y 
class point:
	def __init__(self, x1 = 0, y1 = 0):
		self._x = x
		self._y = y

	def getX(self):
		return self._x

	def setX(self, x):
		self._x = x

	def getY(self):
		return self._y

	def setY(self, y2):
		self._y = y

	def __str__(self):
		return "({0},{1})".format(self._x,self._y)

	# creates a location of a robot and has a moveRobot fucntion thate will move the
	#  robot North, South, East, or West
class robot(point):
	def __init__(self, x1, y1):
		point.__init__(self, x1, y1 )
		
	def moveRobot(self, move):	
		if move == "N" or move == "n":
			self._y1 += 1 
			
		elif move == "S" or move == "s":
			self._y1 -= 1 
			
		elif move == "E" or move == "e":
			self._x1 += 1
			
		else: 
			move == "W" or move == "w"
			self._x1 -= 1
			
	def __str__(self):
		return "({0},{1})".format(self._x1,self._y1)


	#___ This class has methods that produces the unique path from the robot to the treasure

class path(robot):
		def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
			#robot coodinates 
			self._x1 = x1	
			self._y1 = y1

			#treasure coodinates 
			self._x2 = x2
			self._y2 = y2
			self.shortestPath = -1   #shortest path found (shorest number of moves)
			self.pathList = []         # a list to store paths
			

		def moveRobot(self, move):
			return super().moveRobot(move)

		#initial path: no pathFound = 0, empty list 
		def setPaths(self): 
				self.path(self._x1, self._y1, 0, [])

		#parameter are robotX robotY 
		def path(self, robotX, robotY, pathFound, path):
				# if shortest path < path found: if the a path found takes more steps then the shorest path return none 
				if self.shortestPath > 0 and self.shortestPath < pathFound:
					return None

				# if the robot and treasure have the same coordinates
				if robotX == self._x2 and robotY == self._y2:
					if len(path) == 0:
					  return

					# list to a string to be displayed
					pathString = ''.join(path)
					

					# Initial path 
					if self.shortestPath < 0:
						self.shortestPath = pathFound
						self.pathList.append(pathString)
						

					# new found path is as short as the shorest path 
					elif self.shortestPath == pathFound:

						# if path not in list add to the list
						if pathString not in self.pathList:
							self.pathList.append(pathString)

					# if the new found path is shorter than the shortest path
					elif self.shortestPath > pathFound:

						# Set shortest path to equal to the new shortest path
						self.shortestPath = pathFound
						self.pathList = [pathString] 

				else:
					
					# Move one step to the up ("N") 
					if robotY < self._y2:
						self.path(robotX, robotY + 1, pathFound + 1, list(path) + ['N'])
	
					# Move one step to the down ("S") 
					if robotY > self._y2:
						self.path(robotX, robotY - 1, pathFound + 1, list(path) + ['S'])

					# Move one step to the right ("E")
					if robotX < self._x2:
						self.path(robotX + 1, robotY, pathFound + 1, list(path) + ['E'])

					# Move one step to the left ("W")
					if robotX > self._x2:
						self.path(robotX - 1, robotY, pathFound + 1, list(path) + ['W'])

			# Prints number of unique paths 
		def numUniquePaths(self):
				for path in self.pathList:					
					print(path)
				print("Number of paths: ", len(self.pathList))

			# Overloaded to string

		def __str__(self):
			return "robot ({0},{1}) and treasure ({2},{3})".format(self._x1, self._y1, self._x2, self._y2)
