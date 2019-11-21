
class Car:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.position = {'x' : 0, 'y' : 0}
		self.time = 0

	def left(self, speed, time):
		self.speed = abs(speed)
		self.position['x'] = self.position['x'] - speed * time
		self.time = self.time + abs(time)
		print(f"Уou have been moving for {time} h at a speed of {speed} km/h and you are in position: {self.position}")
		return self.position

	def up(self, speed, time):
		self.speed = abs(speed)
		self.position['y'] = self.position['y'] + speed * time
		self.time = self.time + abs(time)
		print(f"Уou have been moving for {time} h at a speed of {speed} km/h and you are in position: {self.position}")
		return self.position

	def right(self, speed, time):
		self.speed = abs(speed)
		self.position['x'] = self.position['x'] + speed * time
		self.time = self.time + abs(time)
		print(f"Уou have been moving for {time} h at a speed of {speed} km/h and you are in position: {self.position}")
		return self.position

	def down(self, speed, time):
		self.speed = abs(speed)
		self.position['y'] = self.position['y'] - speed * time
		self.time = self.time + abs(time)
		print(f"Уou have been moving for {time} h at a speed of {speed} km/h and you are in position: {self.position}")
		return self.position



# car1 = Car("Audi", "white")
# print(car1.position)
# print(car1.left(20, 25))
# car1.up(10, 10)
# print(car1.position)
# print(car1.time)
# car1.down(10, 20)
# print(car1.position)
# print(car1.time)
# print(car1.speed)

