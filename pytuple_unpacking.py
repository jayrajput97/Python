#created a tuple
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    #print tuple
    print(item)

#able to print or access a part of tuple is called tuple unpacking
for ticker, price in stock_prices:
    print(price)


#use the same concept to make it complex
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    #using tuple unpacking to compare highest hours worked
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    #Return value as a tuple
    return (employee_of_month, current_max)

e = employee_check(work_hours)
#print tuple returned tuple
print(e)

#tuple unpacking using function call and return
name, hours = employee_check(work_hours)
print(f'Name: {name}')
print(f'Hours: {hours}')