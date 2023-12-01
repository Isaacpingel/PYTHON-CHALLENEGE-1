# I can use commands from the terminal in here
import os

# Make empty order list
order = []
#resteraunt name
r_name = "Isaac's Taco Truck"

# Menu items dictionary
menu_items = {
    1: {"Item name": "Tacos", "Price": 1.99},
    2: {"Item name": "Burritos", "Price": 5.99},
    3: {"Item name": "Quesadillas", "Price": 4.99},
    4: {"Item name": "Nachos", "Price": 3.99},
    5: {"Item name": "Churros", "Price": 1.99},
    6: {"Item name": "Mexican Coke", "Price": 1.99}
}

# Function to display the menu
def display_menu():
    print(f"{r_name}'s Menu")
    for item_num, item in menu_items.items():
        print(f"{item_num}. {item['Item name']} - ${item['Price']:.2f}") # Will round to nearest penny 

# Print the initial menu
display_menu()

place_order = True  # Bool. for if they are still ordering

while place_order:
    # Get menu selection
    menu_selection = input("Please enter your menu selection (item number): ")

    # Validate input as a number
    if not menu_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    menu_selection = int(menu_selection)

    # Validate menu selection
    if menu_selection not in menu_items:
        print("Invalid menu selection!")
        continue

    # Get item details
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]

    # Get quantity
    quantity = input(f"How many {item_name} would you like? (Default: 1): ")
    if not quantity.isdigit():
        quantity = 1
    else:
        quantity = int(quantity)

    # Add to order
    order.append({"Item name": item_name, "Price": price, "Quantity": quantity})

    # Print current order
    print("Current Order:")
    total = 0
    for item in order:
        print(f"{item['Item name']}  ${item['Price']} x {item['Quantity']}")
        total += item['Price'] * item['Quantity']
    print(f"Total: ${total:.2f}")

    # Check if the customer wants to order more
    response = input("Would you like to order another item? (Default: N/y) ").lower() # Will default to yes

    if response != 'y'.lower():
        place_order = False
    else:
        # Reprint the menu and show the total so far
        display_menu()
        print(f"Current Total: ${total:.2f}") # Running total

# Print receipt
print(f"\n{r_name}")
print("Order Receipt:")
print("-----------------------------")
print(f"Item\t\tPrice/Quantity")
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]


# Calculate the final total
final_total = sum([item["Price"] * item["Quantity"] for item in order])
print(f"\nTotal: ${final_total:.2f}")

print("\nThank you for your order!")

#All code original to user