1
names = ['Akneta', 'Azen', 'Yasmin', 'Molokosos', 'Angelina Jolie']
names.clear()
print(names)

2
names = ['Akneta', 'Azen', 'Yasmin', 'Molokosos', 'Angelina Jolie']
3
print(len(names))
4
names = ['Akneta', 'Azen', 'Yasmin', 'Molokosos', 'Angelina Jolie']
first_name, *rest, prelast_name, last_name = names
print(first_name)
print(prelast_name)
print(last_name)
5
mixed_data_types =['Simbochka', '15', '180', ]
6
IT = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
7
print(IT)
8
print(len(IT))
9
first_item,*rest, middle_item, last_item = IT
print(first_item)
print(middle_item)
print(last_item)
10
IT[2]='Yandex'
print(IT)
11
IT.append('it')
print(IT)
12
IT.insert(3, 'IT')
print(IT)
13
IT = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(IT.title())
15
IT = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Java-Scrip' in IT)
16
IT.sort()
print(IT)
# 17
IT.sort(reverse=True)
print(IT)

18
print(IT[0:3])
19
print(IT[-3:])
20
print(IT[4])
21
IT.pop(0)
print(IT)
22
IT.pop(3)
print(IT)
23
IT.pop()
print(IT)
24-25
IT.clear()
print(IT)
26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
27
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(2, 'Python')
full_stack.insert(4, 'SQL')
full_stack.insert(5,'Redux')
print(full_stack)