# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1, s2)

cities = {"Delhi", "Mumbai", "Pune", "Bangalore"}
cities2 = {"Seoul", "kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid", "Paris"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")    
