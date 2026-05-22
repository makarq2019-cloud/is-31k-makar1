class Descriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("_value")

    def __set__(self, instance, value):
        instance.__dict__["_value"] = value

class Test:
    value = Descriptor()

t = Test()
t.value = 10
print(t.value)