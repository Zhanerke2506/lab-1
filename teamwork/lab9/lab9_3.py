def the_list(arr):
   list = [arr]
   for i in arr :
      # adding a new value to the end of the list
      list.append(i+" welcome")
   return list

list1 = ["Aruzhan","Aliya","Zhanerke","Almash"]
print ('The returnes list is:',the_list(list1))



# “kwargs” stands for keyword arguments. It is used for passing advanced 
# data objects like dictionaries to a function because in such functions one doesnt 
# have a clue about the number of arguments, 
# hence data passed is be dealt properly by adding “**” to the passing type.

# Python program to demonstrate
# passing dictionary as kwargs

def display(**name):
    print (name["fname"]+" "+name["mname"]+" "+name["lname"])

print(display(fname ="John",
        mname ="F.", 
        lname ="Kennedy"))


