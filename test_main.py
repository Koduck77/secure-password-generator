import unittest
from main import generate_password


class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = generate_password(12, True, True, True)
        self.assertEqual(len(password), 12)

    def test_lowercase_password(self):
        password = generate_password(10, False, False, False)
        self.assertTrue(password.islower())


if __name__ == "__main__":
    unittest.main()
