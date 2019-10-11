from service.mapper.BasicMap import BasicMap

map = "[{\"Fname\":\"FirstName\"}, {\"Lname\": \"LastName\"}]"
input_object = {'Fname':'Cody','Lname':'Zimmerman'}
BasicMap.Map(input_object, map)