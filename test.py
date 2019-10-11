import unittest
from service.mapper.BasicMap import BasicMap

class BasicMapTestCase(unittest.TestCase):
    
    def setUp(self):
        self.map = "[{\"Fname\":\"FirstName\"}, {\"Lname\": \"LastName\"}]"
        self.input_object = {'Fname':'Cody','Lname':'Zimmerman'}


    def test_validatemapkey(self):
        BasicMap()._validatemapkey(self.map)

if __name__ == '__main__':
    unittest.main()