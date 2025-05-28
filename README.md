[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y49tTL6w)

# ☀️𝒮𝒰𝑀𝑀𝐸𝑅𝒯𝐼𝑀𝐸 𝐵𝐸𝒜𝒞𝐻 𝒫𝒜𝒞𝒦𝐸𝑅! 🏖️

## 𝘞𝘩𝘰 𝘪𝘴 𝘵𝘩𝘦 𝘱𝘳𝘰𝘨𝘳𝘢𝘮 𝘧𝘰𝘳?
This program is useful to anyone looking to go to the beach this summer! Especially if you are a forgetful person or need help packing items for your trip. 

## 𝘞𝘩𝘢𝘵 𝘥𝘰𝘦𝘴 𝘵𝘩𝘦 𝘱𝘳𝘰𝘨𝘳𝘢𝘮 𝘥𝘰?
This program is an assistant to help you pack for you next beach trip. It gives you a list of items you might need to pack like sunscreen or water and you check off the item as you pack it. At the end, when you're done packing, based on what you've entered, it gives you a list of the items you've packed and the items you haven't.

## SS of code
![image](https://github.com/user-attachments/assets/e8fdae50-969e-4b17-bcd0-82bc7f5e11e2)

## Program running
![image](https://github.com/user-attachments/assets/59dd496a-5607-42e5-bd0a-f1f44f2ec033)


## Lists
- "packing_list" gives original items to pack and "packed_items" is initially an empty list and items are added as the user enters them.
```
packing_list = ["Sunscreen", "Towel", "Sunglasses", "Swimsuit", "Hat","Water bottle", "Flip-flops", "Beach snacks", "Book", "Umbrella"]
packed_items = []
```

## Loops
- Used a "while True" loop to check user_input.
```
while True:
        user_input = input("Packed item #")
        if user_input == "done":
            break
```

## Functions
- Incorporated functions by defining the program itself in the beginning and putting all the code under the function, and at the end to run the code.
```
def beach_program(): #at the beginning, before all the code
beach_program() #at the end, after all the code
```
  
