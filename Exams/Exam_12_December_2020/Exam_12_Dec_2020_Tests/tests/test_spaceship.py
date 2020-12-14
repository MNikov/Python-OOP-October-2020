import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceship(unittest.TestCase):
    def setUp(self) -> None:
        self.ship = Spaceship('Apollo', 3)

    def test_init(self):
        self.assertEqual('Apollo', self.ship.name)
        self.assertEqual(3, self.ship.capacity)
        self.assertListEqual([], self.ship.astronauts)

    def test_add_when_full_should_raises_error(self):
        self.ship.add('Neil')
        self.ship.add('Buzz')
        self.ship.add('Momchil')
        with self.assertRaises(ValueError) as error:
            self.ship.add('test')
        # expected = "Spaceship is full"
        # self.assertEqual(expected, str(error))

    def test_add_when_name_same_should_raise_error(self):
        self.ship.add('Neil')
        self.ship.add('Buzz')
        self.ship.add('Momchil')
        with self.assertRaises(ValueError) as error:
            self.ship.add('Buzz')

    def test_successful_add_should_return_string(self):
        self.ship.add('Neil')
        self.ship.add('Buzz')
        self.assertEqual("Added astronaut test", self.ship.add('test'))
        self.assertEqual(3, len(self.ship.astronauts))

    def test_remove_non_existing_astronaut_should_raise_error(self):
        with self.assertRaises(ValueError):
            self.ship.remove('test')

    def test_remove_successfully(self):
        self.ship.add('Neil')
        self.ship.add('Buzz')
        self.assertEqual("Removed Buzz", self.ship.remove('Buzz'))