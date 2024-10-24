
import math

EARTH_RADIUS = 6371.01

lat1 = math.radians(float(input("Enter latitude of point 1 (degrees): ")))
lon1 = math.radians(float(input("Enter longitude of point 1 (degrees): ")))
lat2 = math.radians(float(input("Enter latitude of point 2 (degrees): ")))
lon2 = math.radians(float(input("Enter longitude of point 2 (degrees): ")))

dlon = lon2 - lon1
dlat = lat2 - lat1
a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance = EARTH_RADIUS * c
print(f"Distance between points: {distance:.2f} kilometers")

