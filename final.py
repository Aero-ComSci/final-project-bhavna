def beach_program():
    packing_list = ["Sunscreen", "Towel", "Sunglasses", "Swimsuit", "Hat","Water bottle", "Flip-flops", "Beach snacks", "Book", "Umbrella"]
    packed_items = []

    print("\nBeach packing list:")
    for each in packing_list:
        print(each)

    print("\nWhat items have you packed? Enter number from packing_list or 'done' when you're finished (enter each item one by one)")
    while True:
        user_input = input("Packed item #")
        if user_input == "done":
            break
        if user_input.isdigit():
            number = int(user_input)
            if number>=1 and number<=len(packing_list):
                item = packing_list[number-1]
                if item not in packed_items: #used google to help with this line because I was unsure how to check whether it was already packed. Now I know you can use "not in" just like you use "in" to check if it's in the list.
                    packed_items.append(item)
                    print("Packed item:", (item))
                else: print("Already packed that")
            else: print("Number not in list")
        else: print("Please enter number from list or 'done'")

    print("\nReady for the beach!")
    print("\nItems packed:")
    for each in packed_items:
        print(each)
    print("\nItems not packed:")
    for each in packing_list:
        if each not in packed_items:
            print(each)

beach_program()
