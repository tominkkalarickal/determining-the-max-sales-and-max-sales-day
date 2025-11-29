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

#problem 2
#input numbers until user enters 0 then find range
#initialize an empty list to hold numbers
def find_range_of_numbers():
    numbers = []
    #Encourage the user to keep entering numbers until they enter zero
    while True:
        value= float(input("Enter a value (or 0 to end): "))
        if value == 0:
            break
        else:
            numbers.append(value)

    #display the list of numbers entered
    print(numbers)
    #Determine the range if the list isn't empty
    if len(numbers) > 0:
        max_num = numbers[0]
        min_num = numbers[0]

        #find max and min
        for num in numbers:
            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num

        #compute range
        num_range = max_num - min_num
        #display the range using f string
        print(f"Range = {num_range}")
    else:
        print("No numbers found")

find_range_of_numbers()






