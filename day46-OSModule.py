DATA:# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")


# import os
# folders = os.listdir("data")

# print (folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))



import os
folders = os.listdir("data")

print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))