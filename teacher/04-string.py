# Строки - неизменяемые объекты

# Строки заключаются в кавычки
# '..'
# ".."
# '''..'''
# """.."""

a = 'something'
print(a)
a = 'something\''
print(a)
a = '"something\''
print(a)

a = "something"
print(a)
a = "something'"
print(a)
a = "something\""
print(a)

a = '''line0
line1
line2
'''
print(a)
a = '''line0
'line1
''line2
'''
print(a)
a = """line0
line1
line2
"""
print(a)
a = """line0
"line1
""line2
"""
print(a)

# форматирование строк
name = 'Alex'
print('Hello, {}'.format(name))
age = 20
print('Hello, {} ({} years old)'.format(name, age))
print('Hello, {0} ({1} years old)'.format(name, age))
print('Hello, {1} ({0} years old)'.format(name, age))
print('Hello, {name1} ({age1} years old)'.format(name1 = name, age1 = age))

name = 'alex'
print('{} ({})'.format(name, id(name)))
name = name.capitalize()
print('{} ({})'.format(name, id(name)))

