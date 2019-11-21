import unittest

from car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.my_car = Car("Audi", "white")
    def test_left_with_speed20_time25(self):
        result = self.my_car.left(20,25)
        expected_result = {'x': -500, 'y': 0}
        self.assertEqual(result, expected_result)
    def test_up_with_speed20_time25(self):
        result = self.my_car.up(10,10)
        expected_result = {'x': 0, 'y': 100}
        self.assertEqual(result, expected_result)
    def test_right_with_speed20_time20_y(self):
        result = self.my_car.right(20,20)
        self.assertEqual(result['x'], 400)
    def test_down_with_speed15_abs(self):
        self.my_car.down(-15,15)
        speed_my_car = self.my_car.speed
        self.assertEqual(speed_my_car, 15)

if __name__ == "__main__":
    unittest.main()
