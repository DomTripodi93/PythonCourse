
class GenericClass:
    pass


GenericClass.random_attribute = 7

generic_instance = GenericClass()

generic_instance.new_attribute = 12
generic_instance.random_attribute = 15


print("The random_attribute attribute on the generic_instance instance of GenericClass")
print(generic_instance.random_attribute)

print("\nThe new attribute added to an instance of GenericClass")
print(generic_instance.new_attribute)
