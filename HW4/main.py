import os

print("=======")


def walk_dir(dir:str,root:str,list:list):
    with os.scandir(dir) as files:

        for file in files:
            if file.name[0]=='.':
                continue
            path=f"{dir}/{file.name}"
            if file.is_dir():
                p=[]
                list.append([file.name,p])
                print(f'{root}/{file.name}/')
                walk_dir(path,dir,p)
            else:
                list.append(file.name)
                print(path)
    return

def expand_list(l:list,root_string:str):

    new_list= []
    for element in l:
        if isinstance(element,list):
            """new_list.append(f"{root_string}/{element[0]}")"""
            for a in expand_list(element[1],f"{root_string}/{element[0]}"):
                new_list.append(a)
        else:
            new_list.append(f"{root_string}/{element}")

    return new_list


example_dir = '/Users/evgenijgalusko/dbData'
files = []
walk_dir(example_dir,example_dir,files)
print("_____________")
names = expand_list(files,example_dir)
for a in names:
    print(a)