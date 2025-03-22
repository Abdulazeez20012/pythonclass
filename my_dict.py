my_dict={
	"name":"Alice",
	"age":"25",
	"city":"New York"
}
print(my_dict)

if "25" in my_dict:
	print('city is in the dictionary')

print(my_dict.get("name"))

print(my_dict.get("salary","Not Available"))
for key in my_dict:
 print(key)

for values in my_dict.values():
 print(values)
for key,value in my_dict.items():
 print(f"{key}:{value}")

squared={x:x**2 for x in range(1,6)} 
print(squared)


keys =["name","age","city"]
values= ["Alice","25","New York"]

for key,values in zip(keys,values):
 my_dict[key] = value
print(my_dict)

my_dict = {"name":"Alice","age":25}
new_data ={"city":"New York","age":26}

for key, value in new_data.items():
 my_dict[key]= value
print(my_dict)

nested_dict = {
 "person1": {"name":"Alice","age":25},
 "person2": {"name":"Bob","age":30}
}

nested_dict["person1"]["city"] = "New York"
print(nested_dict)


new_data = {"city": "Los Angeles","profession":"Engineer"}
nested_dict["person2"].update(new_data)
print(nested_dict)




