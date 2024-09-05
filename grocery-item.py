budget = float(input("Enter your budget for the months: "))
total_spent = 0
grocery_list = []
while True:
  print("\nMenu")
  print("1. Add item")
  print("2. Exit")

  choice = input("choice option: ")

  if choice == '1':
    item_name = input("Enter the item name: ")
    item_quantity = int(input("Enter the quantity of the item: "))
    item_price = float(input("Enter the price of the item: "))

    item_total_price = item_quantity * item_price

    if total_spent + item_total_price > budget:
       print(f"Can't add {item_name}. it exceeds the budget by {item_total_price + total_spent - budget}!")
    else:
      grocery_list.append([item_name, item_quantity, item_price,item_total_price])
      total_spent += item_total_price
      print(f"{item_name} added to the list. ")

  elif choice == '2':
    print("\nFinal Grocery list: ")
    for item in grocery_list:
        print(f"{item[0]}- Quality: {item[1]}, Price: {item[2]}, Total:{item[3]}")
    print(f"\nTotal spent: {total_spent}")
    print(f"Remaining budget: {budget - total_spent}")
    break
  else:
    print("Invalid option. please choose 1 or 2.!")