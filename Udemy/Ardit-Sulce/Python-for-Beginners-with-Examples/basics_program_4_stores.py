store_addresses = ["Ordular Sokak", "İleri Sokak", "Atatürk Sokak"]
pins = {"Mustafa": 1234, "Kemal": 1235, "Ahmet": 1236}



def find_in_file(user_fruit):
    with open("C:/Users/msı/Documents/GitHub/Learning-Path/Udemy/Ardit-Sulce/Python-for-Beginners-with-Examples/sample.txt", "r") as myfile:
        fruits = myfile.read()
    fruits.splitlines()
    if user_fruit in fruits:
        return "That fruit is in the list."
    else:
        return "No such fruit found!"

while True:
    store_address = input("Enter your store address(to exit write exit): ")
    if store_address in store_addresses:
        print(f"Welcome to {store_address}!")
        while True:
            pin = int(input("Enter your pin code(to exit write -1): "))
            pins_val_list = list(pins.values())
            pins_key_list = list(pins.keys())
            if pin in pins.values():
                print(f"Welcome {pins_key_list[pins_val_list.index(pin)]}!")
                fruit = input("Enter fruit:")
                print(find_in_file(fruit))

            elif pin == -1:
                print(f"{pin} exits from the program.")
                break
            
            else:
                print("Incorrect pin!")
                print("This info can be accessed only by firm personnel.")
                print("If you think there is a problem with it. Please consult with your IT support.")
    elif store_address.lower() == "exit":
        print("Program is stopped.")
        break
    else:
        print("Incorrect store address!")
        print("Please enter a valid address.")
        print("If you think there is a problem with it. Please consult with your IT support.")
        