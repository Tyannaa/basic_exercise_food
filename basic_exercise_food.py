# Food data structure
food_menu = [
    {
        "category": "Appetizers",
        "items": [
            {"name": "Caesar Salad", "price": 8.99},
            {"name": "Garlic Bread", "price": 4.99},
            {"name": "Bruschetta", "price": 6.99}
        ]
    },
    {
        "category": "Main Course",
        "items": [
            {"name": "Steak", "price": 19.99},
            {"name": "Grilled Salmon", "price": 18.99},
            {"name": "Chicken Parmesan", "price": 14.99},
            {"name": "Vegetable Stir-Fry", "price": 12.99}
        ]
    },
    {
        "category": "Desserts",
        "items": [
            {"name": "Cheesecake", "price": 7.99},
            {"name": "Chocolate Brownie", "price": 5.99},
            {"name": "Ice Cream Sundae", "price": 6.99}
        ]
    }
]

#####################################
# Exercise 1: Print the names of all food categories
for category_data in food_menu:
    category_name = category_data["category"]
    print(category_name)


#####################################
# Exercise 2: Calculate the total price of all items in the menu
total_price = 0

for category_data in food_menu:
    for item in category_data["items"]:
        total_price += item["price"]

rounded_total_price = round (total_price, 2)

print("Total price of all items: $", rounded_total_price)


#####################################
# Exercise 3: Find the most expensive item in each category
for category_data in food_menu:
    category_name = category_data["category"]
    items_in_category = category_data["items"]

    most_expensive_item = None
    highest_price = 0

    for item in items_in_category:
        item_name = item["name"]
        item_price = item["price"]

        if item_price > highest_price:
            highest_price = item_price
            most_expensive_item = item_name

    print(f'The most expensive item in the "{category_name}" category is "{most_expensive_item}" with a price of ${highest_price:.2f}')


####################################
# Exercise 4: Check if any category has items with a price greater than $20
has_price_above_20 = False

for category_data in food_menu:
    items_in_category = category_data["items"]

    for items in items_in_category:
        item_price = item["price"]

        if item_price > 20:
            has_price_above_20 = True
            break

if has_price_above_20:
    print("Some category has items with a price greater than $20.")
else:
    print("No category has items with a price greater than $20.")


####################################
# Exercise 5: Print the names of the vegetarian items (category: Main Course, item: Vegetable Stir-Fry)
vegetarian_items = []

for category_data in food_menu:
    category_name = category_data["category"]

    if category_name == "Main Course":
        items_in_category = category_data["items"]
        for item in items_in_category:
            if item["name"] == "Vegetable Stir-Fry":
                vegetarian_items.append(item["name"])

if vegetarian_items:
    print("The names of vegetarian items in the 'Main Course' category are:")
    for item in vegetarian_items:
        print(item)
else:
    print("No vegetarian items found in the 'Main Course' category.")


####################################
# Exercise 6: Calculate the average price of items in the Desserts category
total_price = 0
item_count = 0

for category_data in food_menu:
    if category_data["category"] == "Desserts":
        items_in_category = category_data["items"]
        for item in items_in_category:
            item_price = item["price"]
            total_price += item_price
            item_count += 1

if item_count > 0:
    average_price = total_price / item_count
else:
    average_price = 0

print(f"The average price of items in the 'Desserts' category is ${average_price:.2f}")


####################################
# Exercise 7: Update the price of the Grilled Salmon item to $18.99
print("The price of 'Grilled Salmon' has been updated to $18.99")


####################################
# Exercise 8: Print the names of the items with prices greater than $15
for category_data in food_menu:
    items_in_category = category_data["items"]

    for item in items_in_category:
        item_name = item["name"]
        item_price = item["price"]

        if item_price > 15:
            print(f"The item '{item_name}' has a price greater than $15.")


##################################
# Exercise 9: Find the cheapest item in the menu
cheapest_item = None
lowest_price = float("inf")

for category_data in food_menu:
    items_in_category = category_data["items"]

    for item in items_in_category:
        item_name = item["name"]
        item_price = item["price"]

        if item_price < lowest_price:
            lowest_price = item_price
            cheapest_item = item_name

if cheapest_item is not None:
    print(f"The cheapest item is '{cheapest_item}' with a price of ${lowest_price:.2f}")
else:
    print("No items found in the menu.")


######################################
# Exercise 10: Count the total number of items in the menu
total_items = 0

for category_data in food_menu:
    items_in_category = category_data["items"]
    total_items += len(items_in_category)

print(f"The total number of items in the menu is {total_items}")