cook_book = {}

with open("recipes.txt", "r", encoding="utf-8") as f:
    recipe_name = ""
    servings = 0
    ingredients = {}

    for line in f:
        line = line.strip()

        if line:
            if recipe_name == "":
                recipe_name = line
            elif servings == 0:
                servings = int(line)
            else:
                ingredient_data = line.split('|')
                ingredient_name = ingredient_data[0].strip()
                quantity = int(ingredient_data[1].strip())
                measure = ingredient_data[2].strip()
                ingredients[ingredient_name] = {"quantity": quantity, "measure": measure}
        elif recipe_name and servings and ingredients:
            cook_book[recipe_name] = {"servings": servings, "ingredients": ingredients}
            recipe_name = ""
            servings = 0
            ingredients = {}

# Print the dictionary
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]['ingredients']

            for ingredient_name, data in ingredients.items():
                quantity = data['quantity'] * person_count
                measure = data['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
        else:
            print(f"Recipe for {dish} is not found in the cookbook.")

    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


files = ['1.txt', '2.txt']
output_file = "output.txt"

file_info = []
for filename in files:
    with open(filename, 'r') as file:
        lines = file.readlines()
        file_info.append((filename, len(lines), lines))

file_info.sort(key=lambda x: x[1])

with open(output_file, 'w') as output:
    for file_data in file_info:
        output.write(file_data[0] + '\n')
        output.write(str(file_data[1]) + '\n')
        for line in file_data[2]:
            output.write(line)

print("Готово! Результат записан в файл", output_file)
