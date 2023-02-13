#___________________________________________SUPERMARKET MANAGEMENT APP______________________________________________________



items = []  # list of dictionaries representing the inventory
while True:
    print('---------------------WELCOME TO YUUKI SUPERMARKET-------------------')
    print('! Choose one of the following:\n1.View items\n2.Add items \n3.Purchase items \n4.Search items \n5.Edit items \n6.Exit the application.')
    choice = int(input('Enter your choice: '))
    
    
    if choice == 1:
        print('----------VIEW ITEMS----------')
        inventory_length = len(items)
        print(f'The number of items in the inventory is {inventory_length}')
        if len(items) != 0:
            print('Here are all the available items in the supermarket.')
            for i in items:
                for key, value in item.items():
                    print(f'{key}: {value}')
                    
                    
                    
    elif choice == 2:
        print('-------------ADD ITEMS-------------')
        #user_name = input('What is your name? ')
        #print(f'Hello {user_name}. To add an item to your shopping list, fill in the form below.')
        item = {}
        item['name'] = input('Item name: ')
        while True:
          try:
            item['quantity'] = int(input('Item quantity(indicate kg or g): '))
            break
          except ValueError:
            print('Quantity can only be in digits or numbers')
          try:
            item['price'] = int(input('Item price: '))
          except ValueError:
            print('Price can only be in digits or numbers')
        print('Item has been successfully added.')
        items.append(item)
          
    elif choice ==3:
      print('--------------Purchase items-------------')
      print(items)
      purchase_item = input('Enter the item you want to purchase? ')
      purchase_quantity = int(input('Enter the item quantity: '))
      for item in items:  
        if purchase_item.lower() == item['name'].lower():
          if item['quantity'] != 0:
            if purchase_quantity <= item['quantity']:
              print('Your total fee is %d. Please proceed to the checkout desk.' %(item['price'] * purchase_quantity))
              item['quantity'] -= purchase_quantity
            else:
              print('Quantity required not available')
          else:
            print('Item is out of stock')
    
    
    elif choice == 4:
      print('-------------------SEARCH ITEM------------------')
      find_item = input('Enter the name of the item you want to search: ')
      for item in items:
        if item['name'].lower() == find_item.lower():
          print(f'The item {find_item} is available')
          print(item)
        else:
          print('The item is not available')
          
    elif choice == 5:
      print('-----------------------EDIT ITEMS--------------------')
      item_name = input('Enter the name of the item you want to change: ')
      for item in items:
        if item_name.lower() == item['name'].lower():
          print(f'Here are the current {item_name} details.')
          print(item)
          item['name'] = input('item name: ')
          while True:
            try:
              item['quantity'] = int(input('item quantity: '))
              break
            except ValueError:
              print('Item quantity not valid. Quantity only in numbers.')
          print(item)
        else:
          print('Item not found.')
          
    elif choice == 6:
      print('--------------EXITING THE PROGRAM----------------')
      break
    
    else:
      print('You entered an invalid options. Please choose again from the available options.')        
        
        