# dic = {
#     "Prionti": "Human Being",
#     "Spoon": "object"
# }


# print(dic["Prionti"])

# dic = {
#     344: "Harry",
#     56: "prionti",
#     678: "Zakir",
#     567: "Diganta"
# }

# print(dic[567])


info = {'name': 'Harry', 'age': 19, 'eligiable': True}
# print(info)
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")
