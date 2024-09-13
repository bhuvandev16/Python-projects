food = []
prices = []
total = 0

def display_cart():
    print('\n----- Your Cart -----')
    if len(food) == 0:
        print("Your cart is empty.")
    else:
        for i in range(len(food)):
            print(f"{i+1}. {food[i]} - ${prices[i]}")
        print(f"\nTotal: ${sum(prices)}")
    print('----------------------')

while True:
    print("\nOptions: ")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View your cart")
    print("4. Checkout and Quit")

    choice = input("\nChoose an option: ")

    if choice == '1':
        food_name = input("Enter the food item to buy: ")
        try:
            food_price = float(input(f"Enter the price of {food_name}: $"))
            food.append(food_name)
            prices.append(food_price)
            print(f"{food_name} added to the cart.")
        except ValueError:
            print("Please enter a valid price.")

    elif choice == '2':
        display_cart()
        if len(food) > 0:
            try:
                remove_index = int(input("Enter the number of the item to remove: ")) - 1
                removed_item = food.pop(remove_index)
                removed_price = prices.pop(remove_index)
                print(f"{removed_item} removed from the cart.")
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
        else:
            print("Nothing to remove.")

    elif choice == '3':
        display_cart()

    elif choice == '4':
        display_cart()
        print("Thank you for shopping!")
        break

    else:
        print("Invalid option. Please choose again.")
