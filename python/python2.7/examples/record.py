
class Record(object):
    __slots__= "attribute1", "attribute2", "attribute3",

    def items(self):
        "dict style items"
        return [(field_name, getattr(self, field_name)
                for field_name in self.__slots__)]

    def __iter__(self):
        "iterate over fields tuple/list style"
        for field_name in self.__slots__:
            yield getattr(self, field_name)

    def __getitem__(self, index):
        "tuple/list style getitem"
        return getattr(self, self.__slots__[index])

r= Record()
r.attribute1= "hello"
r.attribute2= "there"
r.attribute3= 3.14