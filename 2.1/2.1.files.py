def cook_books():
    cook_book = {}
    with open('recipe_book.txt') as f:
        for line in f:
            name = line.strip()
            number = f.readline().strip()
            ingredients = []
            for ing in range(int(number)):
                ing = f.readline().strip()
                ing_list = []
                ing_list.append(ing.split(' | '))
                ing_dict = {'ingridient_name': ing_list[0][0], 'quantity': int(ing_list[0][1]), 'measure': ing_list[0][2]}
                ingredients.append(ing_dict)
            cook_book[name] = ingredients
            f.readline()
    return cook_book
print(cook_books(), '\n\n')


def get_shop_list_by_dishes(dishes, person_count):
    dish_user = {}
    for dish in dishes:
        if dish in cook_books():
            for i in cook_books()[dish]:
                dish_key = i['ingridient_name']
                dish_user[dish_key] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
    print(dish_user)


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)

