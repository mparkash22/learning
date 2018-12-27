#raise the value1 to value2
def raise_both(value1, value2):    #function header
    """Raise value1 to the power of value 2 and vice versa"""  #docstring

    new_value1= value1 ** value2  #function body
    new_value2= value2 ** value1

    new_tuple = (new_value1, new_value2)

    return new_tuple


#we can print the tuple value using index
powr = raise_both(2,5) #function call
print(powr[0])
print(powr[1])

#we can unpack the tuple and print the value
power1,power2 = raise_both(2,5)
print(power1)
print(power2)