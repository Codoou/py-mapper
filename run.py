from service.mapper.BasicMap import BasicMap

map = "[{\"Fname\":\"FirstName\"}, {\"Lname\": \"LastName\"}]"
input_object = {'Fname':'Cody','Lname':'Zimmerman'}
input_list = [{'Fname':'Cody','Lname':'Zimmerman'},
              {'Fname':'Jeremy','Lname':'Leininger'}]

print(BasicMap.MapList(input_list, map))
