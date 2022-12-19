
class MyFirstClass:
    class_attribute = 7


print("A direct view of class_attribute on the MyFirstClass class")
print(MyFirstClass.class_attribute)
my_class_instance = MyFirstClass()

print("\nA view of class_attribute on my_class_instance instance of MyFirstClass")
print(my_class_instance.class_attribute)

my_class_instance.class_attribute += 5

print("\nA view of class_attribute on my_class_instance after adding 5")
print(my_class_instance.class_attribute)

print("\nA view of class_attribute on the MyFirstClass after adding 5 to my_class_instance.class_attribute")
print(MyFirstClass.class_attribute)

print("A direct view of class_attribute on the MyFirstClass class after adding 7")
MyFirstClass.class_attribute += 7

print("\nA view of class_attribute on my_class_instance after adding 7 to MyFirstClass.class_attribute")
print(my_class_instance.class_attribute)
print(MyFirstClass.class_attribute)


my_class_instance = MyFirstClass()
print("\nA view of my_class_instance.class_attribute after adding 7 to " +
      "MyFirstClass.class_attribute and redeclaring")
print(my_class_instance.class_attribute)


print("\nA view of my_class_instance.something after adding \"something\" " +
      "to my_class_instance as a new attribute")
my_class_instance.something = 17
print(my_class_instance.something)


print("\nA view of my_class_instance.something after adding \"something\" " +
      "to MyFirstClass as a new attribute and redeclaring my_class_instance")
MyFirstClass.something = 12
my_class_instance = MyFirstClass()
print(my_class_instance.something)
