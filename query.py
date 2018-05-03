class Query:

    @classmethod
    def sort_by(cls, attr, otherClass):
        return otherClass.all().sort(key = lambda obj: getattr(obj, attr))

    @classmethod
    def sort_by_name(cls, otherClass):
        return sorted(otherClass.all(), key = lambda x: x.name)
