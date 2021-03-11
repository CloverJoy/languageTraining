from collections import namedtuple
from abc import ABC, abstractmethod

# polymorphism, common behavior with children
# duck typing, doesnt really need ui control base


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("Dropdownlist")


# polymorphism
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()

draw([ddl, tb])


class Text(str):
    def duplicate(self):
        return self + self


yoo = Text("yoo")
print(yoo.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")

# kalo mau equality pass by reference, pake magic method __eq__
# mau tau address memory, pake id()


Point = namedtuple("Point", ["x", "y"])
# immutable, tapi gak perlu magic method __eq__ lagi
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
