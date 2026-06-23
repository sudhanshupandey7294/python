"""
Restaurent Management System
food_items ( fid , fname , category )
orders   ( cname , cmob , category )

1. Add Food Items
2. View Menu
3. Update Food Price/Category
4. Delete Food Item
5. Place Order
6. View Orders
0. Exit

"""
#importing libraries
import pickle

#A method to add food

def addFood():
    file=open('food.bin', 'ab')
    fid=input("\tEnter the New food ID : ")
    fname=input("\tEnter food name : ")
    category= dict()
    i=1
    ch='y'
    while ch in "yY":
        cat=input(f"\n\tEnter {i} Category : ")
        price=input("\tEnter the price : ")
        ch=input("\tDo you want to Add More(Y/n) : ")
        category.update({cat:price})
        i=i+1
    food={fid:[fname,category]}    
    pickle.dump(food,file)
    file.close()
    print("\tFood items added Successfully")



while True:
    print("\n\tRestaurent Management System")
    print('''
            1. Add Food Items
            2. View Menu
            3. Update Food Price/Category
            4. Delete Food Item
            5. Place Order
            6. View Orders
            0. Exit
    ''')
    ch=int(input("\tSelect option : "))
    if ch==0:
        
        print("\tThank you!")
        break
    elif ch==1:
        addFood()   
