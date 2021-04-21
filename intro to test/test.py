from demo import *

import unittest

# a unit test is required to be defined inside a class

class TestArea(unittest.TestCase):
    def setUp(self):
        pass
    #runs before running test used as preparation method before test

    def test_area_of_rect(self):
        self.assertEqual(area_of_rect(5,6), 30)
    #basic test method 1

    def test_area_of_square(self):
        self.assertEqual(area_of_square(8), 64)
    #basic test method 2

    def test_input_value(self):
        self.assertRaises(TypeError, area_of_square, True)

    def tearDown(self):
        pass
    # runs after all the test have been run this is used for purpose like deleting the content or closing the file ,etc.


# python -m unittest discover -> use this command is used for auto discovery for test
# it will not only search them but also attempt testing all the test file present in that directory

# python -m unittest discover -s <directory-name>

# python -m unittest -v <filename>
#the command is used run all the test in verbose mode in a file
# its not compulsory to run a unittest with verbose
