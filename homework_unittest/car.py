
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



car1 = Car("Audi", "white")
print(car1.position)
print(car1.left(20, 25))
car1.up(10, 10)
print(car1.position)
print(car1.time)
car1.down(10, 20)
print(car1.position)
print(car1.time)
print(car1.speed)

# class Car:
#     def __init__(self, speed: int, map: int):
#         self.speed = speed
#         self.map = 500
#         self.pos = self.map/2

#     def move(self, direction):
#         if direction == 'right':
#             self.pos += self.speed
#         elif direction == 'left':
#             self.pos -= self.speed
#         elif direction == 'up':
#             self.pos -= (self.map/5)*self.speed
#         elif direction == 'down':
#             self.pos += (self.map/5)*self.speed
#         return(self.pos)

#     def change_speed(self, speed):
#         self.speed = speed
#         return self.speed

#     def print_info(self):
#         print('Speed:', self.speed, '\nPosition:', self.pos)

#     def print_map(self):

#         for f in range(0, self.map):

#             if f == self.pos:
#                 print('+', end='')
#             else:
#                 print('-', end='')
#             if not f % (self.map/5):
#                 print()
#         print()

#     def drive(self):
#         self.print_map()
#         while True:
#             user_input = input(
#                 'Enter direction("up", "down", "left", "right"), speed(1,2,10,20), i-info, q-quit: ').lower().strip()
#             expected_values = ['up', 'down', 'left', 'right', 'i', 'q']
#             if user_input in expected_values or user_input.isnumeric():
#                 if user_input.isnumeric():
#                     self.change_speed(int(user_input))
#                 elif user_input == 'i':
#                     self.print_info()
#                 elif user_input == 'q':
#                     break
#                 else:
#                     self.move(user_input)
#                     self.print_map()


# car1 = Car(1, 500)
# car1.print_info()
# car1.drive()