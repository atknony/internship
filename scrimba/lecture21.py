#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

if 'Jhon' and 'Eric' in friends:
    check = True

all_friends = friends.union(my_friends)
same_friends = friends.intersection(my_friends)
only_in_friends = friends.difference(my_friends)
fifth = friends.symmetric_difference(my_friends)
new_cars = list(set(cars))
print(all_friends)
print(same_friends)
print(only_in_friends)
print(fifth)
print(new_cars)
