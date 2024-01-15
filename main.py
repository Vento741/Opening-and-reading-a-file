import os

# Открываем файл "recipes.txt" для чтения
with open('recipes.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    content = file.readlines()

cook_book = {}

i = 0
while i < len(content):
    name_of_dish = content[i].strip()  # Получаем название блюда
    i += 1  # Переходим к следующей строке (количеству ингредиентов)

    ingredients = []

    # Проходимсаемся по всем ингредиентам в этом блюде
    for j in range(i, i + int(content[i])):
        ingredient_info = content[j + 1].strip().split(' | ')  # Получаем информацию о каждом ингредиенте

        ingredient_name = ingredient_info[0]  # Получаем название ингредиента
        quantity = int(ingredient_info[1]) if len(ingredient_info) > 1 else 0  # Получаем количество ингредиента или 0, если информация отсутствует
        measure = ingredient_info[2].strip() if len(ingredient_info) > 2 else ''  # Получаем единицу измерения или пустую строку, если информация отсутствует

        ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
        ingredients.append(ingredient)  # Добавляем информацию о каждом ингредиенте в список

    cook_book[name_of_dish] = ingredients  # Добавляем информацию о блюде в словарь
    i += int(content[i]) + 2  # Переходим к следующему блюду, учитывая разделительную строку

# Печатаем готовый словарь на экран
print("cook_book = {")
for dish, ingredients in cook_book.items():
    print(f"  '{dish}': [")
    for ingredient in ingredients:
        print(f"    {ingredient},")
    print("  ],")
print("}")   


def get_shop_list_by_dishes(dishes, person_count):
    list_of_dishes = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in list_of_dishes:
                    list_of_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    list_of_dishes[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count

    return list_of_dishes

# Получаем список покупок
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#Выводим список покупок
print("{")
for ingredients, details in shop_list.items():
    print(f" '{ingredients}': {details}")
print("}")


# Получаем список файлов в папке пути sorted
folder_path = 'sorted'
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Создаем словарь для хранения данных
file_contents = {}

# Читаем содержимое файлов и подсчитываем количество строк
for file_name in file_names:
    with open(os.path.join(folder_path + '/' + file_name), 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents[file_name] = {
            'num_lines': len(lines),
            'content': lines
        }

#Сортировка словаря по количеству строк
sorted_files = sorted(file_contents.items(), key=lambda x: x[1]['num_lines'])

# Записываем отсортированное содержимое в файл
with open(os.path.join(folder_path, 'result.txt'), 'w', encoding='utf-8') as result_file:
    for file_name, content in sorted_files:
        result_file.write(f'{file_name}\n{content["num_lines"]}\n')
        result_file.writelines(content["content"])