from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print('Woof!')

class Cat(Animal):

    def speak(self):
        print('Meow!')


cat = Cat()
dog = Dog()

print('stop')



class User:

    def __init__(self, name, age, email, phone):

        self.name = name
        self.age = age
        self.blocked = True
        self._email = email
        self.__phone = phone

    def is_deleted(self):
        pass

    def is_blocked(self):
        print(self.blocked)

    def check_age(self):
        pass


class Admin(User):

    def delete_post(self, post_id):
        pass

    def delete_user(self, user_id):
        print(user_id)


user_1 = User(name='Kirill', age=32, email='kirill@sirotinsky.com', phone='+79866666666')
admin_1 = Admin('Pavel', 16, email='pavel@sirotinsky.com', phone='+798555555555')


from datetime import datetime

class Contract:

    sides = []
    region = 77

    def __init__(self, side_1: str, side_2: str, region: int = None):
        self.dt = datetime.now()
        self.sides.append(side_1)
        self.sides.append(side_2)
        if region:
            self.region = region

    def __str__(self):
        return f'Договор между {self.sides[0]} и {self.sides[1]} в таком-то регионе {self.region}'

    def __repr__(self):
        pass

    def __add__(self, other):
        pass

    def when_created(self):
        print(self.dt)

    @classmethod
    def change_region(cls, region):
        cls.region = region

    @staticmethod
    def count_to_ten():
        for i in range(10):
            print(i+1)


contract_1 = Contract(side_1='Petya', side_2='Vasya', region=40)
print(str(contract_1))

contract_2 = Contract(side_1='Masha', side_2='Dasha')
print(contract_2.region)
contract_2.change_region(26)

contract_3 = Contract(side_1='123', side_2='321')
print(contract_3.region)


a = datetime.now()
print(str(a))
pass
list

b = [1,2,3]
c = [4,5,6]