number = input()
n = []
while number != "End":
    n.append(int(number))
    number = input()
my_dict = {}
for i in n:
    a = n.count(i)
    my_dict[i] = a
print(my_dict)