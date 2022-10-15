"""
Тізімдердегі, кортеждердегі, жиындардағы
және сөздіктердегі әдістерді қарастырып,
барлығына ортақ 5 әдісті және ерекшеленетін
бірнеше (2-3) әдістерді қолдананатын бағдарлама жаз.
"""
lists = ["A", "B", "C"]
tuples = (1, 2, 3, 2)
sets = {"+", "-"}
dictionaries = {"university": "SU", "speciality": "computer science"}

second_list = ["D", "E", "F"]
second_tuple = (4,)
second_set = {"*", "/"}
second_dictionary = {"department": "programming engineering"}

print(lists + second_list)
print(tuples + second_tuple)

print(len(sets))
print(len(dictionaries))

print(min(lists))
print(min(tuples))

print(max(sets))
print(max(dictionaries))

print(tuples.count(2))

print(tuples.index(3, 0, 4))

"""
----------------------------------------------
"""

lists.extend(second_list)
print(lists)
print(lists.reverse())
print(lists.clear())

"""
----------------------------------------------
"""

print(tuples.count(2))
print(tuples.index(2, 0, 4))

"""
----------------------------------------------
"""

sets.discard("-")
print(sets)
sets.update(second_set)
print(sets)

"""
----------------------------------------------
"""

print(dictionaries.items())
print(dictionaries.get("university"))