def even_check(num):
#mod method provides a boolean output
    result = num % 2 == 0
    return result

r = even_check(20)
#output will be TRUE or FALSE based on the result
print(r)



#Return TRUE if any number is even inside a list
def check_even_list(num_list):
    for number in num_list:
        if number%2 == 1:
            return True
        else:
            #pass keyword means don't do anything
            pass
    print('no numbers even')
    return False

#the output will return nothing. the first TRUE is for the previous function
check_even_list([1,3,5])


def check_return_even_number(list1):
    #return all the even numbers in a list

    #placeholder variables
    even_numbers = []

    for number in list1:
        if number % 2 == 0:
            even_numbers.append(number)

        else:
            pass

    return even_numbers

output = check_return_even_number([1,3,4,5])
print(output)