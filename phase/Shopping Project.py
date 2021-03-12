# 商品购物系统

def initial():
    print('*' * 42)
    print(' ' * 11 + '** Main Menu **')
    print(' ' * 11 + '1 -- Item Management')
    print(' ' * 11 + '2 -- Shopping Cart')
    print(' ' * 11 + '0 -- Quit')
    print('*' * 42)

    global system
    system = int(input('Please Enter A Number to Operate: '))


def initial_mag():
    print('*' * 42)
    print(' ' * 11 + '** Item Management **')
    print(' ' * 11 + '1 -- Item Info Import')
    print(' ' * 11 + '2 -- Show All Item Info')
    print(' ' * 11 + '9 -- Back to Main Menu')
    print('*' * 42)

    global system_mag
    system_mag = int(input('Please Enter a Number to Manage Items: '))
    
def initial_cart():
    print('*' * 42)
    print(' ' * 11 + '** Shopping Cart **')
    print(' ' * 11 + '1 -- Add Items to Your Cart')
    print(' ' * 11 + '2 -- Edit the Number of Items in Your Cart')
    print(' ' * 11 + '3 -- Show All Items\'s Info in Your Cart')
    print(' ' * 11 + '4 -- Check Out')
    print(' ' * 11 + '9 -- Back to Main Menu')
    print('*' * 42)

    global system_cart
    system_cart = int(input('Please Enter a Number to Edit your Cart: '))

def importItem():
    print('ItemInfo importing...\nImport Success!')

def showAllItem():
    
    print('Show All Items\' Info')
    print('Items\' Info: ')

    for i in stock:
        print(i)

def showInitialCart():

    print('Add Item to Your Cart')
    print('Items\' Info: ')

    for i in stock:
        print(i)

def showAfterCart():
    print('Show All Items in Your Cart')
    if len(cart) != 0:
        for i in cart.keys():
            print('Item: '+ cart[i][0] + ', '+ 'Price: '+str(cart[i][1])+', Description: '+cart[i][2] + ', Number: ' + str(cart[i][3]))
    else:
        print('Your Cart is Empty , Go Shopping!')



# Above Are defined Functions
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Below Are Codes



class Item:
    def __init__(self, ID, name, price, desp):
        self.id = ID
        self.name = name
        self.price = price
        self.desp = desp

    def __str__(self):
        msg = 'ItemInfo[ID: ' + str(self.id) + ', Name: ' + self.name + ', Price: ' +str(self.price) + ', Description: ' + self.desp + ']'
        return(msg)
    
phone = Item('i004', 'Telephone', 2300.0, 'andoid phone')
wdispenser = Item('i002', 'Water Dispenser', 299.0, 'water dispenser with purifying function')
laptop = Item('i003', 'Laptop', 4999.0, '15-inch laptop')
cup = Item('i001', 'Cup', 56.0, 'stainless-steel cup')

stock = []
stock.append(phone)
stock.append(wdispenser)
stock.append(laptop)
stock.append(cup)

cart = {}

while True:
    initial()  ### 主菜单
    
    if system == 1:  ### 1.商品管理

        while True:
            initial_mag()

            if system_mag == 1:   ## 1.1 商品信息导入
                importItem()
                continue
            
            elif system_mag == 2: ## 1.2 显示所有商品信息
                showAllItem()
                continue

            else:                 ## 1.9 返回上一级菜单
                break
        continue 
            
    if system == 2:  ### 2. 购物车

        while True:

            initial_cart()

            if system_cart == 1:  ## 2.1 添加商品到购物车

                showInitialCart()

                ID = input('Please Enter the Item ID of Your Interest: ')
                num = int(input('Please Enter the Number of Items: '))

                for i in stock:

                    if i.id == ID:

                        cartlist = []
                        cartlist.append(i.name)
                        cartlist.append(i.price)
                        cartlist.append(i.desp)
                        cartlist.append(num)
        
                        cart[ID] = cartlist
                        print(cart)
                continue

            elif system_cart == 2:  ## 2.2 修改购物车中的商品数量

                newID = input('Edit the Item Number in Your Cart\nPlease Enter the Item ID you want to Edit: ')
                newNum= int(input('Please a New Number: '))

                if newNum != 0:   # 修改数量

                    for i in cart.keys():
                        if i == newID:
                            cart[i][3] = newNum      
        
                else:             # 输入0 删除该商品
                    del cart[newID]
                    print('Since the Item Number you entered is 0, this Item has been REMOVED !')
                continue
        
            elif system_cart == 3:  ## 2.3 显示购物车中的所有商品信息

                showAfterCart()
                continue

            elif system_cart == 4:  ## 2.4 结算

                print('Check Out')
   
                sum = float(0)   # 商品总价
                for i in cart.keys():
                    sum += cart[i][3] * cart[i][1]

                print('Your Balance Due: ' + str(sum))

                for i in cart.keys():
                    print('Item: '+ cart[i][0] + ', '+ 'Price: '+str(cart[i][1])+', Description: '+cart[i][2] + ', Number: ' + str(cart[i][3]))
      
                cart.clear() # 清空购物车
                continue

            else:                    ## 2.9 返回上一级菜单
                break

            continue
        
    if system == 0:  ### 0. 退出
        break




























    
