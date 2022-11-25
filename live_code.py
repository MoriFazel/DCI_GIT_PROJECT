#####################
from data import warehouse1, warehouse2
user_name = (input("what is your name?"))
print(f"Hello, {user_name}")
print(f"what would you like to do?, {user_name}")
print("1.list")
print("2.search")
print("3-quit")

while True:
    user_input = input("number:")
    if user_input =="1":
        print("")
        print("********************")
        print("Items in warehouse1:")
        print("")
        for item in warehouse1:
            print("-" + item)
        print("")
        print("********************")
        print("Items in warehouse2:")
        print("")
        for item in warehouse2:
            print("-" + item)
        print("-" + item)
        print(f" thank you, {user_name}")
        break


    if user_input =="2":
        item_name = input("what to search?")
        amount_wareh1 = warehouse1.count(item_name)
        amount_wareh2 = warehouse2.count(item_name)
        if amount_wareh1 ==0 and amount_wareh2 > 0:
            print(f" Amount aval: {amount_wareh1 + amount_wareh2}")
            print("location: warehouse1")

            yes_no= input("do u wanna order this? (yes/no)")
            if yes_no.lower() == "y":
                print(f"")
            else:
                print(f"Thank you fo rur visit, {user_name}")
                break
        
        print(f" Amount aval: {amount_wareh1 + amount_wareh2}")

        if amount_wareh1 > 0 and amount_wareh2>0:
            warehouse_dict = {amount_wareh1: "warehouse1", amount_wareh2: "warehouse2"}
            sum_item = amount_wareh1 + amount_wareh2
            maximum = max(amount_wareh1, amount_wareh2) 
            print(f" Amount aval: {amount_wareh1 + amount_wareh2}")
            print("location: both wareh")
            print(f"Maximum avilable {maximum}in{warehouse_dict[maximum]}")

            yes_no= input("do u wanna order this? (yes/no)")
            if yes_no.lower() == "y":
                order_amount = input("how many?")
                if order_amount > sum_item:
                    print("*******************")
                    print(f" more than numbers we have, only in {sum_item}")
                    print("*******************")
                    order_max = input("u wanna order the max aval? (y/n)")
                    if order_max.lower()== 'y':
                        print(f"{sum_item} {item_name} have benn ordered.")
                        print(" ")
                        print( 'thanks for the visit', user_name)
                        break
                    else:
                        print("thanks for the visit", user_name)
                        print(" ")
                        break
                else:
                    print(" ")
                    print(f"Thank you fo rur visit, {user_name}")
                    break
                
        print(f" Amount aval: {amount_wareh1 + amount_wareh2}")






    if user_input =="3":
        pass
