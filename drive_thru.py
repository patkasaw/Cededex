def get_item(x):
    if x == 1:
        return'🍔 Cheeseburger'
    elif x == 2:
        return'🍟 Fries'
    elif x == 3:
        return'🥤 Soda' 
    elif x == 4:
        return'🍦 Ice Cream'
    elif x == 5:
        return'🍪 Cookie'
    else:
        return'Wrong number'

def welcome():
    print('Welcom to our restaurant, please see our menue below:')
    welcome_menu = [
     '1.🍔 Cheeseburger',
     '2.🍟 Fries',
     '3.🥤 Soda',
     '4.🍦 Ice Cream',
     '5.🍪 Cookie',
    ]
    print(welcome_menu, '\n')
    
welcome()

x = int(input('Please insert youe order number:'))
print(get_item(x))