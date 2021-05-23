#READ CONSPOLE INPUT

name = input("Enter name\n")
age = int(input("Enter age\n"))
print("Name is ", name ," and age is ", age)

#OPERATORS

i = 5;
j = 3;
print("Sum : ", i+j)
print("Diff : " , i-j)
print("Product : " , i*j)
print("Modulo : " , i%j)
print("Floor Division : " , i//j)
print("Float Division : " , i/j)

#STRING

firstName = " bahadır ";
lastName = " zeren ";
age = 43;

fullName = firstName.lstrip().capitalize() + lastName.lstrip().rstrip().capitalize();

print(fullName);
print(str(age));

fullName = fullName.replace("Bahadır", "Musa Giray");

midNameNdx = fullName.find("Giray");

print(midNameNdx);
print(fullName);


#BOOLEAN

name = None
sayi = 0
metin = ""
kume = ()
dizi = []

if (not name):
    print(str(name) + " is False")
if (not sayi):
    print(str(sayi) + " is False")
if (not metin):
    print(metin + " is False")
if (not kume):
    print(str(kume) + " is False")
if (not dizi):
    print(str(dizi) + " is False")

#LIST

a = []
b = [1, 23, 45, 67]
c = [2, 4, "Musa"]
d = ["G", b, c]

print(d)

list_of_ints = [int(i) for i in ["34", "9", "06"]]

print(list_of_ints)

#TUPLE (Immutable and fixed size static array)

a = ()
b = (1, 23, 45, 67)
c = (2, 4, "Musa")
d = ("G", b, c)

print(d)

#SET

set_of_words1 = set() # create a new set. Note that we do not use {}, as that is for the dict
set_of_words1.add("The") # add values
set_of_words1.add("A")
set_of_words1.add("Boat")
print("Boat" in set_of_words1) # True
set_of_words2 = {"Anchor","A","Coast"} # create another set and populate it
print(set_of_words1.intersection(set_of_words2)) # intersection
print(set_of_words1.union(set_of_words2)) # union
for value in set_of_words2 : # all values
    print(value)


#DICTIONARY (Key-value pairs: Java Map)

roomNum = {"Musa": 0, "Zeynep": 6}
roomNum["Musa"] = 1
print(roomNum["Musa"])
roomNum["Funda"] = 35
roomNum["Bahadır"] = 43
print(roomNum)
print("Zeynep" in roomNum)
print(roomNum.keys())
print(roomNum["Bahadır"] == 43)
print(roomNum["Bahadır"] is 43)

#LOOPS

for i in range(0, 5):
    print(str(i))

for i in range(0, 10, 2):
    print(str(i))

for i in range(10, 0, -2):
    print(str(i))

for c in "Manish" :
  print(c)


list = ["A", "B", "C", 7]

for item in list:
    print(item)


tuple = ("A", "B", "C", 7)

for item in tuple:
    print(item)


dict = {"A": 1, "B": 2, "C": 3, 7: 4}

for key in dict:
    print(str(key) + ": " + str(dict[key]))

for k, v in dict.items():
    print(str(k) + ": " + str(v))


def square(n):
    for i in range(n):
        yield i**2
for i in square(10):
    print(i)
