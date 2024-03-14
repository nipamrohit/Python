#1 
string = "HELLO"
string_rev = string[::-1]
print(string_rev)


#2
string_replace = string.replace("LLO"," IS GOOD")
print(string_replace)


#3

string = "Character in a string"
chars = " string"
if(chars in string):
    print("String Found")


#4
List = ["BMW", "GTR", "Porchse"]
Tuple = ("AUDI" , "MERCEDESE", "PAGANI")
Set = {"DODGE" , "CHEVEROLET" , "TOYOTA"}

print(str(List))
print(str(Tuple))
print(str(Set))


#5
str_upper = string.upper()
str_lower = string.lower()

print(str_upper)
print(str_lower)

string = " This  is  sample text"
split_string1 = string.split()
print(split_string1)
print(string[5:10])


#6
list_min = min(List)
list_max = max(List)
list_len = len(List)
list_sum = List + list(Tuple)

print("MIN = ",list_min, " MAX = ",list_max, " LENGTH = ",list_len, " SUM = ",list_sum)

Tuple_min = min(Tuple)
Tuple_max = max(Tuple)
Tuple_len = len(Tuple)
Tuple_sum = Tuple + tuple(List)

print("MIN = ",Tuple_min, " MAX = ",Tuple_max, " LENGTH = ",Tuple_len, " SUM = ",Tuple_sum)


#7
list_one = ["INDIA", "USA", "UAE", "GERMANY"]
list_two = list_one[:]

print(list_two)   


#8
student= {"Name" : "Ramesh",
          "Age" : "20",
          "Grade" : "AB"}

#1
print(student["Age"])
#2
student["Grade"] = "AA"
#3
if("gender" in student):
    print("Age is Present")
else:
    print("Gender is not provided")  


#9
set1 = {"1","2","3"}
set2 = {"3","4","5"}

#1 union
union_set = set1.union(set2)    
print(union_set)

#2 intersaction
intersec_set = set1.intersection(set2)
print(intersec_set)

#3 difference
diff_set = set1.difference(set2)
print(diff_set)

#4 subset
sub_set = set1.issubset(set2)
print(sub_set)


#10
subjects = {"Maths" : ["Raghav","Shivam","Om","Madhav"],
            "Science" : ["Sumit", "Shubham", "Nitin", "Darshan","Madhav","Om"]}

subjects["Maths"].append("Manthan")
subjects["Science"].remove("Shubham")

print(set(subjects["Science"]).intersection(set(subjects["Science"])))

world = {
    "India" : {"Suart" : "8300000", "vadodara" : "1800000", "junagdh" : "1000000"},
    "USA" : {"Washington" : "2500000", "New York City" : "8089689"},
    "UAE" : {"Dubai" : "1137347", "Abu Dhabi" : "603492", "Sharjah" : "543,733"}
}


#11
original_list = [1, 2, 3, 4, 5, 6, 7]
even_indices = original_list[::2]
odd_indices = original_list[1::2]
print(even_indices)
print(odd_indices)


#12
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)


#13
lst = [1, 2, 3, 2, 1]
print(lst == lst[::-1]) 


#14
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3=sum((tuple1, tuple2),())
print(tuple3,type(tuple3))



