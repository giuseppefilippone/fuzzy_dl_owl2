import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestRelated(unittest.TestCase):

    def test_query(self):
        p = ParserInterface("examples/TestSuite/related.txt")
        self.assertEqual(0.5, p.solve(), "TestRelated")


if __name__ == "__main__":
    unittest.main()
