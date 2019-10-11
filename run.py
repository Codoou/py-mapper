from service.mapper.BasicMap import BasicMap

#BasicMap._validatemapkey("{\"hello\":\"world\"}")
#BasicMap._validatemapkey("\"hello\":\"world\"}")

#BasicMap._validatemapkey("[{\"hello\":\"world\"}]")
map = "[{\"Fname\":\"FirstName\"}, {\"Lname\": \"LastName\"}]"
input_object = {'Fname':'Cody','Lname':'Zimmerman'}
BasicMap.Map(input_object, map)