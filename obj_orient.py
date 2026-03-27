from abc import ABC, abstractmethod

#create basic class
# class Pockemon:
#     # an attribute for this class
#     class_vers = 0.1
#
#     # function which creates fields for a certain instance
#     def __init__(self, name, skin_id, level=1, power=1):
#         self.name = name
#         self.type = 'general'
#         self.skin = skin_id
#         self.level = level
#         self.power = power
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#
#     @property
#     def level(self):
#         return self._level
#
#     @level.setter
#     def level(self, new_level):
#         self._level = new_level
#
#     @property
#     def mon_info(self):
#         return {"name": self.name, "type": self.type, "skin": self.skin, "level": self.level}
#
#     @property
#     def power(self):
#         return self._power
#
#     @power.setter
#     def power(self, new_power):
#         if 1 <= new_power <= 100:
#             self._power = new_power
#         else:
#             raise AttributeError('Power can only be in range 1-100')
#
#     def attack(self):
#         print(f'{self.name} attacks with power {self._power}!')
#
#     def power_up(self):
#         if self._power < 100:
#             self._power += 1
#         else:
#             raise ValueError("Max power is obtained! Can't be increased")
#
# #create class with inheritance
# class WaterPockemon(Pockemon):
#     def __init__(self, name, skin_id, level=1, power=1):
#         super().__init__(name, skin_id, level, power)
#         self.type = "water"
#
#     def attack(self):
#         print(f"{self._name} throws waterballs with power {self._power}!")
#
#
# # inherit from two classes and see how MRA works
# class C1:
#     def func1(self):
#         print("Метод func1 класса C1")
#
# class C2(C1):
#     def func2(self):
#         print("Метод func2 класса C2")
#
# class C3(C1):
#     def func1(self):
#         print("Метод func1 класса C3")
#     def func2(self):
#         print("Метод func2 класса C3")
#     def func3(self):
#         print("Метод func3 класса C3")
#
# class C4(C2, C3):
#     def func4(self):
#         print("Метод func4 класса C4")
#
# instance = C4()
# instance.func1()

#try operator overloading

# class PalMon:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#         self.hp = 95
#     def __add__(self, other):
#         if isinstance(other, PalMon):
#             first_half = self.name[:(len(self.name)//2)+1]
#             second_half = other.name[:(len(other.name)//2)+1]
#             new_name = f"{first_half}-{second_half}"
#             new_level = (self.level + other.level) / 2
#             return PalMon(new_name,new_level)
#         else:
#             NotImplemented
#
#     def __eq__(self, other):
#         if isinstance(other, PalMon):
#             if self.level == other.level:
#                 return True
#             else:
#                 return False
#         else:
#             NotImplemented
#
#     def __ne__(self, other):
#         if isinstance(other, PalMon):
#             if self.level != other.level:
#                 return True
#             else:
#                 return False
#         else:
#             NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, PalMon):
#             if self.level < other.level:
#                 return True
#             else:
#                 return False
#         else:
#             NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, PalMon):
#             if self.level > other.level:
#                 return True
#             else:
#                 return False
#         else:
#             NotImplemented
#
#     def __le__(self, other):
#         if isinstance(other, PalMon):
#             if self.level <= other.level:
#                 return True
#             else:
#                 return False
#         else:
#             NotImplemented
#
#     def __ge__(self, other):
#         if isinstance(other, PalMon):
#             if self.level >= other.level:
#                 return True
#             else:
#                 return False
#         else:
#             NotImplemented
#
#     def _up_hp(self, new_hp):
#         curr_hp = self._hp
#         for i in range(new_hp + 1):
#             if curr_hp < 100:
#                 curr_hp += 1
#             else:
#                 break
#         return curr_hp
#
#     @property
#     def hp(self):
#         return self._hp
#
#     @hp.setter
#     def hp(self, new_hp):
#         if type(new_hp) is int:
#             self._hp = new_hp
#             print(f"{self.name}'s HP is {self.hp} now.")
#         else:
#             raise TypeError(f"Please, use int only. The type passed is {type(new_hp)}")
#
#
#     def __call__(self, *args, **kwargs):
#         for key, value in kwargs.items():
#             if key == "food":
#                 print(f"Omnomnom.... Delicious {value}!")
#             if key == "medicine":
#                 try:
#                     self.hp = self._up_hp(value)
#                 except TypeError as err:
#                     print(err)
#
#
#
#
#     def __str__(self):
#         return f"Palmon {self.name} (lvl {self.level})"
#
#
# first = PalMon("Battrice", 5)
# second = PalMon("Bigos", 8)
# third = first + second
# third(food="banana", medicine="3")
# print("Success!")

class AbstractClass(ABC):
    def __init__(self, name,):
        self.calc_name = name

    @abstractmethod
    def calculate(self):
        raise NotImplementedError("Abstract method cannot be called")

class Multiplyer(AbstractClass):
    def __init__(self, name):
        super().__init__(name)

    def calculate(self):
        print(f"{self.calc_name} is instance of Mulriplyer. It Multiplyes.")

class Devidor(AbstractClass):
    def __init__(self, name):
        super().__init__(name)

    def calculate(self):
        print(f"{self.calc_name} is instance of Devidor. It Devides.")


devide = Devidor("Splitter")
mult = Multiplyer("Procreat")

def call_calculate(obj):
    obj.calculate()

for elem in (devide, mult):
    call_calculate(elem)