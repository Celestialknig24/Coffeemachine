
water=1000
milk=1000
coffee=100
money=0
flag=1

def transaction(cost):
    print("It would cost {} Rs ".format(cost))
    try:
        t=int(input("Enter the amount :"))
        if(t>=cost):
            if(t==cost):
                print("Transaction Successfull!!!")
                return "success"
            else:
                print("Transaction success!!!\nTake your remaining cost {}".format(t-cost))
                return 'success'
                
            
        elif(t<cost):
            print("Transaction Failed \nYou have Transacted less money you poor fellow \nHere's your money refunded {}Rs\nTry Again!!!!!!".format(t))
            return 'Failed'
        else:
            print('Invalid Entery')
            return 'failed'
    except:
        print('Invalid Entery \nTry Again!!!!!! ')
        return 'Failed'



def resources(choice):
    global water,milk,coffee,money
    if (choice=='espresso'):
        if(water>=200 and milk>=50 and coffee>=20):
            if(transaction(200)=='success'):
                water=water-200
                milk=milk-50
                coffee=coffee-20
                money=money+200
                return "Here's Your {} Enjoy!!!".format(choice)
            else:
                return "Transaction Failed"
        else:
            return "Insuffiecent Resources"
    elif (choice=='latte'):
        if ( water>=100 and milk>=150 and coffee>=15):
            if(transaction(150)=='success'):
                water=water-100
                milk=milk-150
                coffee=coffee-15
                money=money+150
                return "Here's Your {} Enjoy!!!".format(choice)
            else:
                return 'Transaction Failed'
        else:
            return "Insuffiecent Resources"

        
    elif (choice=='cappuccino'):
        if(water>=200 and milk>=50 and coffee>=20):
            if(transaction(250)=="success"):
                water=water-50
                milk=milk-250
                coffee=coffee-10
                money=money+250
                return "Here's Your {} Enjoy!!!".format(choice)
            else:
                return 'Transaction Failed'
        else:
            return "Insuffiecent Resources"
        
    
    elif (choice=='report'):
        return "Water:{}ml \nMilk:{}ml \nCoffee:{}g \nTotal Sales:{}Rs ".format(water,milk,coffee,money)
    elif choice=='off':
        global flag
        flag=0
        return "Turning Off \nTotal sales: {} Rs".format(money)

    else:
        return "enter wrong item"
            


while(flag!=0):
    Choose=input("What would you like to drink? (espresso/latte/cappuccino): ")
    print(resources(Choose))

