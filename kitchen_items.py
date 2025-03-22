my_kitchen = {
	"knife":3,"cooker":6,"blender":7,"spoon":8,"pot":9,
	}

kitchen_items = "knife","cooker","blender","spoon","pot",
kitchen_Sum = [3,6,7,8,9]


for key,value in zip(kitchen_items,kitchen_Sum):
 my_kitchen[key]=value
print(my_kitchen)

for key in kitchen_Sum:
 print(key)

my_kitchen = {"knife":3,"cooker":6,"blender":7,"spoon":8,"pot":9,}
new_data ={"knife":31,"cooker":78,"blender":100,"spoon":10,"pot":23,}

for key, value in new_data.items():
 my_kitchen[key]= value
print(my_kitchen)

nested_dict = {
 "person1": {"name":"Alice","age":25},
 "person2": {"name":"Bob","age":30}
}