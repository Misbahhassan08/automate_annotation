import os
model_name = 'pills'

project_path = os.getcwd()
rootdir = f"{project_path}/data/{model_name}/JPEGImages"

list = os.listdir(rootdir)
print(len(list))
