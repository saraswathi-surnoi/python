# list
# it is a collection of values
# in list again we listed is called as nested list

# Method	Purpose
# append	Adds an element to the end of the list.
# clear	    Removes all elements from the list.
# copy	    Creates a shallow copy of the list.
# count   	Counts occurrences of an element.
# extend	Adds elements of another iterable.
# index	    Returns the index of an element.
# insert	Inserts an element at a specific index.
# pop	    Removes and returns an element by index.
# remove	Removes the first occurrence of an item.
# reverse	Reverses the list order.
# sort	    Sorts the list in ascending/descending.


l = [1, 2, 3, "abc", True, [10, 20, 30, "abcd", False]]
# print(l, type(l))

# l1 = l[3]
# print(l1)

# l2 = l[5][0]
# print(l2)

# l3 =l[-1][-3]
# print(l3)

# print(len(l))

# print(l[len(l) -1][0])
# print(dir(l))

"""
'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort'
"""
# l = [10, 20, 30, "abcd", False]

#add an element to the end of this

# l.append(True)
# print(l)

# l.append([10, 20, 30, "abcd", False])
# print(l)

# l.insert(4, "abc")
# print(l)

#these operations are inplace operations no return value

# l.extend([1, 2, 3, "abc", True])
# print(l)
#extend will give the elemewnts not in list it will give as a individual elements 

# l = [2, 3, 1]
# # l.sort() # inplace operation(effects the original list)
# l1 = sorted(l) #this returns a new list (it will effect the original list)
# print(l, l1)

#list is a mutable datatype
l = [10,20,30, "abcd", False]
l[0] = 100
print(l)
