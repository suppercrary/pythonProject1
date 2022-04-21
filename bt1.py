"""
import yaml
with open("configs.yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as error:
        print(error)
"""


# mo file bang duong dan
"""
path='C:/Users/Admin/PycharmProjects/pythonProject4/coffee.txt'
with open(path,"r") as f:
    for i in f.readlines():
        print(i)

"""
# tao va ghi data vao file yaml
"""
import yaml
f=open("test1.yaml","w+")
f.write("---# A list of blogd.net- Domain blogd- TLD net...")
f.close()
"""
"""
# mo file va doc file yaml
import  yaml
with open("test1.yaml","r+") as f:
    print(f.read())
"""
import yaml
"""
#python yaml read
with open("items.yaml") as f:
    data=yaml.load(f,Loader=yaml.FullLoader)
    print(type(data))
"""
"""
#python yaml read document
with open("test1.yaml") as f:
    docs=yaml.load_all(f,Loader=yaml.FullLoader)
    for doc in docs:
        for k,v in doc.items():
            print(k,"->",v)
"""
"""
# python yaml dump
users= [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]
print(yaml.dump(users))
"""
"""
# python yaml write
users= [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]
with open("users.yaml","w+") as f:
    data=yaml.dump(users,f)
"""
"""
# python yaml sorting keys
with open("items.yaml") as f:
    data= yaml.load(f,Loader=yaml.FullLoader)
    print(data)
    sorted=yaml.dump(data,sort_keys=True)
    print(sorted)
"""
""" 
# Tokens
with open("items.yaml") as f:
    data=yaml.scan(f,Loader=yaml.FullLoader)
    for tokens in data:
        print(tokens)
"""





