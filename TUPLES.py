### Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()
print("Empty Tuple Is : ", empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Rangiku', 'Youroichi')
brothers = ('Ichigo', 'Aizen')
print("\nSisters Tuple Is : ", sisters)
print("Brothers Tuple Is : ", brothers)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("\nSiblings Tuple Is : ", siblings)

# 4. How many siblings do you have?
num_siblings = len(siblings)
print("\nNumber of Siblings : ", num_siblings)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ('Papa', 'Mumma') + siblings
print("\nFamily Members Tuple Is : ", family_members)

### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
parents = family_members[:2]
siblings = family_members[2:]
print("\nParents : ", parents)
print("Siblings : ", siblings)

# 2. Create fruits, vegetables, and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Mango', 'pinapple', 'Banana')
vegetables = ('Tomato', 'Broccoli', 'Potato')
animal_products = ('Chicken', 'Meat', 'Eggs')
food_stuff_tp = fruits + vegetables + animal_products
print("\nFood Stuff Tuple Is : ", food_stuff_tp)

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("\nFood Stuff List Is : ", food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index] if len(food_stuff_lt) % 2 != 0 else (food_stuff_lt[middle_index - 1], food_stuff_lt[middle_index])
print("\nMiddle Item(s) : ", middle_item)

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("\nFirst Three Items : ", first_three)
print("Last Three Items : ", last_three)

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:

# if not food_stuff_tp:
#     print("The tuple is empty.")
# else:
#     print("The tuple is not empty.")
# Error Tuple not defined

# Check if 'Estonia' is a nordic country
nordic_countries = ('Svalbard', 'Finland', 'Åland Islands', 'Jan Mayen ', 'Sweden' , 'Iceland')
is_estonia_nordic = 'Estonia' in nordic_countries
print("\nIs Estonia a Nordic Country? : ", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is Iceland a Nordic Country? : ", is_iceland_nordic)