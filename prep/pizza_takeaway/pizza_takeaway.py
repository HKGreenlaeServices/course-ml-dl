
# coding: utf-8

# ## This Project is building a pizza takeaway ordering system. 
# ### Features of this project are:
# 
# ### 1) Customer can order pizza by selecting various options like pizza type, base type, toppings etc.
# ### 2) System should take care of invalid options.
# ### 3) System should be storing customer data to personalize.
# ### 4) At the end, the program should display the itemized order with the total price.
# 
# 

# In[91]:


pizza_type_dict = {}   #dictionary for storing pizza type data   ## e.g., piza_type_dict[P1] = ['Margherita', 3.0]
base_type_dict = {}    #dictionary for storing base type data
toppings_type_dict = {}   #dictionary to store toppings data
cust_data = {}            #dictionary to store customer orders  

### Example of customer data dictionary 

cust_data['Karam'] = { 'num_of_orders': 4
                        'order_num': [(P1, B1,[T1,T2], 3)]     
                     }
# In[92]:


## Load data into dictionaries
def load_data(data_path, type):
    data_file = open(data_path, "r")
    for line in data_file:
        splitedLine = line.split(";")
        if type == 'pizza':
            pizza_type_dict[splitedLine[0]] = [splitedLine[1], float(splitedLine[2])]
        elif type == 'base':
            base_type_dict[splitedLine[0]] = [splitedLine[1], float(splitedLine[2])]
        elif type == 'toppings':
            toppings_type_dict[splitedLine[0]] = [splitedLine[1], float(splitedLine[2])]
    data_file.close()


# In[93]:


##Print dictionary
## This function print the dictionary in the following format
"""
Code, Type, Price
P1, Margherita, 3.0
P2, Chicago, 3.5
P3, Greek, 3.0
P4, California, 3.5
P5, Farm house, 3.0

"""

def print_dict(dictionary):
    print("Code, Type, Price")
    for key in dictionary.keys():
        print(""+ key + ", " + str(dictionary[key][0]) + ", " + str(dictionary[key][1]))


# In[94]:


## Generate unique order number for the given customer
def generate_order_num(name):
    if name in cust_data.keys():             ##Check if customer already exists in cust_data dict
        ord_num = cust_data[name]['num_of_orders']
        ord_num += 1
        return ord_num
    else:
        ord_num = 0
        cust_data[name] = {}
        cust_data[name]['num_of_orders'] = ord_num
        ord_num += 1
        return ord_num


# In[95]:


#Add orders into the cust_data dictionary
def add_cust_data(order_tup, name, order_num):
    cust_data[name]['num_of_orders'] = order_num
    if order_num in cust_data[name].keys():
        l = cust_data[name][order_num]
        l.append(order_tup)
    else:
        l = []
        l.append(order_tup)
        cust_data[name][order_num] = l
    


# In[96]:


#Calculate the total bill of a customer given the order
def calculate_bill(ord_tup):
    bill = 0
    piza_type = ord_tup[0]
    base_type = ord_tup[1]
    top_list = ord_tup[2]
    qty = ord_tup[3]
    bill += pizza_type_dict[piza_type][1]
    bill += base_type_dict[base_type][1]
    bill += len(top_list)*0.5
    bill = bill * qty
    return bill


# In[97]:


def print_complete_order(name, ord_num):
    order_list = cust_data[name][ord_num]
    print("Pizza_type"+"-->"+"Base_Type"+ "-->"+ "Toppings" + "-->" + "-->" + "qty"+ "-->" +"price")
    print("-----------------------------------------------")
    for order in order_list:
        bill = calculate_bill(order)
        print(order[0]+ "-->" + order[1] + "-->" + str(order[2]) + "-->" + str(order[3]) + "-->" + str(bill)+"$")


# In[101]:


##Function to order data
def order():
    print("Welcome to the Pizza TakeAway ")
    name = input("Please enter your name :")
    total_bill = 0
    ord_num = generate_order_num(name)
    #cust_dict = create_order(name)
    print("Hello " + name + ", what type of Pizza would you like to have:")
    print_dict(pizza_type_dict)
    piza_type = input("please select from above options:")
    piza_type = piza_type.upper()    
    while piza_type != 'X': 
        if piza_type in pizza_type_dict.keys():        
            print("\n")
            print(" Here are the types of base availabe: ")
            print_dict(base_type_dict)
            base_type = input("Please enter your option")
            base_type = base_type.upper()
            
            ##Check if base code has valid entry
            base_flag = 0
            while base_flag == 0:
                base_flag = 1
                if base_type not in base_type_dict.keys():
                    base_flag =0
                    print("It is an invalid option")
                    print("\n")
                    print(" Here are the types of base availabe: ")
                    print_dict(base_type_dict)
                    base_type = input("Please enter your option")
                    base_type = base_type.upper()
                    
            print("\n")
            print("Please enter the toppings you would like to add from the following list")
            print_dict(toppings_type_dict)
            print("\n")
            toppings = input("Enter toppings in a comma separated form e.g., if you want to add Olives and mushrooms, enter: T1,T3")
            split_topings = toppings.split(",")             ##List of toppings
            split_topings = [x.upper() for x in split_topings]   #Converting all items of list into uppercase
                
               
            ##Check if all the toppings are valid
            top_flag = 0
            while top_flag == 0:
                top_flag = 1
                for item in split_topings:
                    if item not in toppings_type_dict:
                        toppings = input(item+" :" + " is an invalid entry, please re-enter all toppings with valid codes")
                        split_topings = toppings.split(",")
                        split_topings = [x.upper() for x in split_topings]
                        top_flag = 0
                        break

            qty = 2000
            while qty > 1000:
                qty = input("Please input the number of pizzas to order")
                qty = int(qty)
                if qty > 1000:
                    print("You can order maximum 1000 pizzas in one order")

            print("\n")
            print("Here is your order till now")
            print("Pizza Type: ",pizza_type_dict[piza_type][0])
            print("Pizza Base: ", base_type_dict[base_type][0])
            print("Toppings: ", str(split_topings))
            for item in split_topings:
                print(toppings_type_dict[item][0])
            print("Number of pizzas: ", qty)
            print("\n")
            cnf = input(" Press y to confirm, else to cancel press c")
            if cnf == 'y':
                ord_tup = (piza_type, base_type, split_topings, qty)
                total_bill += calculate_bill(ord_tup)
                print("Your total bill till now is: ", total_bill)
                add_cust_data(ord_tup, name, ord_num)
                piza_type = input("Press 'X' to complete your order or to continue ordering, select a pizza type code:" )
                piza_type = piza_type.upper()
            elif cnf == 'c':
                piza_type = input("To order new pizza, select a pizza type code or press X to exit")  
                piza_type = piza_type.upper()
            
        else:
            print_dict(pizza_type_dict)
            piza_type = input("Please Enter a valid option")
            piza_type = piza_type.upper()
            
    if ord_num in cust_data[name].keys():        
        print("Thank you for your order, Here is your final order")
        print_complete_order(name, ord_num)
        print("Total amount to be paid is " + str(total_bill) +"$")
    else:
        print(" Thank you for visiting")
    


# In[102]:


if __name__ == '__main__':
    pizza = "./Types_of_Pizza.txt"
    base = "./Types_of_Base.txt"
    toppings = "./Types_of_toppings.txt"
    load_data(pizza, 'pizza')
    load_data(base, 'base')
    load_data(toppings, 'toppings')
    order()
    


# In[103]:


cust_data


# In[ ]:


pizza_type_dict


# In[ ]:


s.upper()

