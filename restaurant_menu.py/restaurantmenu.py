menu = {
        'Pizza':150,
        'Burger':60, 
        'Pasta':120,
        'Soup':100,
        'Noodles':100,
        'Spring Roll':80,
        'Fried Rice':90,
        'Salad':70
}

print("Welcome to the Genz Cafe")

print('Pizza: 150\nBurger: 60\nPasta: 120\nSoup: 100\nNoodles: 100\nSpring Roll: 80\nFried Rice: 90\nSalad: 70')

total_order = 0

while True:
  item = input("Enter  the name of the item you want to order= ")
  
  if item in  menu:
     total_order += menu[item]
     print(f"your item {item} had been added to you order")
     
  else:
     print("Sorry, we don't have that item on the menu.") 
  
  another_item = input("Do you want to add another item? (Yes/No)")

  if another_item.lower() == 'no':
     break
 
print(f"Your total order amount is: {total_order}")