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



cook_book = {}
key = ['ingredient_name', 'quantity', 'measure']
with open(full_path, encoding="utf-8") as f:
    while True:
        # ingredients.clear()
        ingredients = []
        name = f.readline().rstrip()
        if not name:
            break
        ingredient_count = f.readline().rstrip()
        for i in range(int(ingredient_count)):
            ing = f.readline().rstrip()
            ing_list = ing.split("|")
            ingredient = dict(zip(key, ing_list))
            ingredient['quantity'] = int(ingredient['quantity'])
            ingredients.append(ingredient)
        cook_book[name] = ingredients
        f.readline().rstrip()
    # print(cook_book)
    print(f"Cook_book =", cook_book)