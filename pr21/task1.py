class Person:
    __slots__ = ('name', 'age')

p = Person()
p.name = "Alex"
p.age = 20

print(p.name, p.age)