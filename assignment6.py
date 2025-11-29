#problem 1
#determine the day with most sales
#create a list of sales amount and a list of corresponding days

def find_max_sales():
    sales_list= [50, 75, 150, 125, 100]
    week_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

    #assume the 1st sale is the max

    max_sale = sales_list[0]
    max_day= week_list[0]

    #finding the max sale and its corresponding day
    for i in range (1,len(sales_list)):
        if sales_list[i] > max_sale:
            max_sale = sales_list[i]
            max_day = week_list[i]

    #display the max sale and day using f string
    print(f"The max sales is ${max_sale}")
    print(f"The max sales day is {max_day}")

find_max_sales()









