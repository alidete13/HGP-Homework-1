def my_filter(lst,x,y): #filter takes a list.
    hi = max(x,y)
    low = min(x,y)
    new_list = [elem for elem in lst if low <= elem <= hi] #list comprehension is used to iterate through each element of our list 
    return new_list                                 

#test 1
print(my_filter([1,2,3,4,5,6,7], 3, 6))

#test 2
print(my_filter([98,99,101,102,103], 102, 98))