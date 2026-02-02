print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Slicing

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[2:])

#Modify Strings

#UPPERCASE
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)