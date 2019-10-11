import unittest
from service.mapper.BasicMap import BasicMap

class BasicMapTestCase(unittest.TestCase):
    
    def setUp(self):
        self.map = "[{\"Fname\":\"FirstName\"}, {\"Lname\": \"LastName\"}]"
        self.input_object = {'Fname':'Cody','Lname':'Zimmerman'}

        self.mapped_object = {'FirstName': 'Cody', 'LastName': 'Zimmerman'}


    def test_validatemapkey(self):
        BasicMap()._validatemapkey(self.map)

    def test_mapdata(self):
        mapped = BasicMap().Map(self.input_object, self.map)
        self.assertEqual(mapped, self.mapped_object)

if __name__ == '__main__':
    unittest.main()