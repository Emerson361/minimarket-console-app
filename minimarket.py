# -*- coding: utf-8 -*-
# minimarket.py

def show_menu():
    print("\n--- Minimarket ---")
    print("1. View available products")
    print("2. Add product to cart")
    print("3. View cart")
    print("4. Remove product from cart")
    print("5. Checkout")
    print("6. Exit")

# Available products in the minimarket
products = {
    1: {"name": "Bread", "price": 1.0},
    2: {"name": "Milk", "price": 3.5},
    3: {"name": "Eggs (12 pack)", "price": 7.0},
    4: {"name": "Rice (1kg)", "price": 4.2},
    5: {"name": "Oil (1L)", "price": 6.8},
}

cart = {}

def view_products():
    print("\n--- Available Products ---")
    for code, info in products.items():
        print(f"{code}. {info['name']} - S/ {info['price']}")

def add_to_cart():
    view_products()
    try:
        code = int(input("Enter the product code: "))
        if code in products:
            quantity = int(input("Quantity: "))
            if code in cart:
                cart[code]['quantity'] += quantity
            else:
                cart[code] = {
                    "name": products[code]["name"],
                    "price": products[code]["price"],
                    "quantity": quantity
                }
            print(f"{products[code]['name']} added to cart.")
        else:
            print("Invalid code.")
    except ValueError:
        print("Invalid input.")

def view_cart():
    print("\n--- Shopping Cart ---")
    if not cart:
        print("Your cart is empty.")
        return
    total = 0
    for code, info in cart.items():
        subtotal = info["price"] * info["quantity"]
        total += subtotal
        print(f"{info['name']} x{info['quantity']} - S/ {subtotal:.2f}")
    print(f"Current total: S/ {total:.2f}")

def remove_product():
    view_cart()
    try:
        code = int(input("Enter the code of the product to remove: "))
        if code in cart:
            del cart[code]
            print("Product removed from cart.")
        else:
            print("Product is not in the cart.")
    except ValueError:
        print("Invalid input.")

def checkout():
    view_cart()
    if cart:
        confirm = input("Do you want to complete the purchase? (y/n): ").lower()
        if confirm == 'y':
            print("Thank you for your purchase!")
            cart.clear()
        else:
            print("Purchase cancelled.")
    else:
        print("No products in the cart.")

# Main program loop
while True:
    show_menu()
    option = input("Select an option: ")

    if option == "1":
        view_products()
    elif option == "2":
        add_to_cart()
    elif option == "3":
        view_cart()
    elif option == "4":
        remove_product()
    elif option == "5":
        checkout()
    elif option == "6":
        print("Thank you for using the minimarket system.")
        break
    else:
        print("Invalid option.")
