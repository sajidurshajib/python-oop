import abc
# Class and Encapsulation


class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    __passcode: str = ''

    def set_passcode(self, code: str):
        self.__passcode = code

    def get_passcode(self):
        return self.__passcode

    def __repr__(self) -> str:
        return "{}".format('repr: name, age')

    def __str__(self) -> str:
        return "name: {}, age: {}".format(self.name, self.age)


# p = Person(name='Sajidur Rahman', age=28)
# print(repr(p))
# print(str(p))

# print("Name: {}, Age: {}".format(p.name, p.age))

# p.set_passcode(code='zdd1t')
# print(p.get_passcode())


# Inheritance

class Student(Person):

    def __init__(self, name: str, age: int, id: int):
        super().__init__(name, age)
        self.__id = id

    def get_id(self):
        return self.__id

    def __repr__(self) -> str:
        return "{}".format('repr: id')

    def __str__(self) -> str:
        return "name: {}, age: {}, id: {}".format(self.name, self.age, self.__id)

# s = Student(name='Sajidur Rahman Shajib', age=28, id=2441)

# print("Name: {}, Age: {}".format(s.name, s.age))
# print("ID: {}".format(s.get_id()))


# polymorphism with abstraction (also interface)

class LanguageAbs(abc.ABC):
    @abc.abstractmethod
    def name(self):
        pass


class Bangla(LanguageAbs):
    def name(self):
        print('Bangla')


class English(LanguageAbs):
    def name(self):
        print('English')


class Math(LanguageAbs):
    def name(self):
        print('Math')


# common interface
def subject(sub_obj):
    sub_obj.name()


# b = Bangla()
# e = English()
# m = Math()


# subject(b)
# subject(e)
