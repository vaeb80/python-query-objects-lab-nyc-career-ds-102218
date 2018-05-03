from query import Query

class Person:

    _all = []

    def __init__(self, name):
        self._name = name
        Person._all.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def sorted_names(cls):
        sorted = Query.sort_by_name(cls)
        for person in sorted:
            print(person.name)

    @classmethod
    def name_oh(cls):
        print(cls)
