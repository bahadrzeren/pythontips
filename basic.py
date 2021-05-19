
#STRING

firstName = " bahadır ";
lastName = " zeren ";

fullName = firstName.lstrip().capitalize() + lastName.lstrip().rstrip().capitalize();

print(fullName);

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

#TUPLE (Immutable and fixed size static array)

a = ()
b = (1, 23, 45, 67)
c = (2, 4, "Musa")
d = ("G", b, c)

print(d)

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

