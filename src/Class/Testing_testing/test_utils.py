import unittest

from .exception import MyCustomException
from . import utils


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Run once")

    def setUp(self) -> None:
        print("set up")

    def test_something(self):
        self.assertTrue(True)  # add assertion here

    def test_add_func(self):
        """
        GIVEN:
        WHEN:
        THEN:

        """
        x = utils.add(5, 7)
        self.assertEqual(12, x)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, 2)

    def test_that_add_throws_exception(self):
        # self.assertRaises(TypeError, utils.add, 2, "3")

        with self.assertRaises(TypeError):
            utils.add(2, "hi")

        with self.assertRaises(MyCustomException):
            utils.add(6, 2)


if __name__ == '__main__':
    unittest.main()
