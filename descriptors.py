class Descriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name
        print(self.public_name)

    def __get__(self, instance, owner):
        print("Getting value!")
        value = getattr(instance, self.private_name)
        return value

    def __set__(self, instance, value):
        print("Setting value!")
        setattr(instance, self.private_name, value)

    def __delete__(self, instance):
        print("Deleting value!")
        delattr(instance, self.private_name)

class SomeClass:
    name = Descriptor() #პირველი დესკრიპტორი
    age = Descriptor() #მეორე დესკრიპტორი

    def __init__(self, name, age):
        self.name = name #იძახებს პირველ დესკრიპტორს
        self.age = age #იძახებს პირველ დესკრიპტორს

obj1 = SomeClass("Elene", 22)

del obj1.name
print(obj1.name)


#
#
#
# class Descriptor:
#     def __get__(self, instance, owner):
#         print("Getting value!")
#         return instance.value
#
#     def __set__(self, instance, value):
#         print("Setting value!")
#         instance.value = value
#
#     def __delete__(self, instance):
#         print("Deleting value!")
#         del instance.value
#
# class SomeClass:
#     def __init__(self, value):
#         self.value = value
#
#     descriptor = Descriptor()
#
#
# obj1 = SomeClass(15)
# obj1.value = 3
# desc = obj1.descriptor
# obj1.descriptor = 3
# print(obj1.value)
# del obj1.descriptor
# print(obj1.descriptor)
#
#




#
# # ფუნქცია property()
# class Alphabet:
#     def __init__(self, value):
#         self._value = value
#
#         # getting the values
#
#     def getValue(self):
#         print('Getting value')
#         return self._value
#
#         # setting the values
#
#     def setValue(self, value):
#         print('Setting value to ' + value)
#         self._value = value
#
#         # deleting the values
#
#     def delValue(self):
#         print('Deleting value')
#         del self._value
#
#     value = property(getValue, setValue, delValue, )
#
#
#
# x = Alphabet('Elene')
# x.value = 'Nika'
# del x.value
# print(x.value)
