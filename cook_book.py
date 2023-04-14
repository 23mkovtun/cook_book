import os
current = os.getcwd()
folder_name = "Открытие и чтение файла, запись в файл"
file_name = "recipes.txt"
full_path = os.path.join(current, file_name)
# print(current)
print(full_path)

with open(full_path, encoding="utf-8") as f:
    res = f.read()
  # print(res)
    

    

    