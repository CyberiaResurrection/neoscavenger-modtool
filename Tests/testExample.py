import unittest


class TestExample(unittest.TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
