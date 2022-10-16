from ctypes import create_string_buffer
import json

# python data that is to be serilized
 
data = {
    "user_details":{
        "name":"Gopika",
        "Gender":"F"
    }
}

# serialization using file method

with open("Create_file.json","w") as file:
    json.dump(data,file, indent=4)


# serialization using string method
Create_str=json.dumps(data,indent=4)
print(Create_str)