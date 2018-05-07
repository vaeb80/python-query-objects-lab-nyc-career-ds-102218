class Query:

    @classmethod
    def sort_by(cls, attr, otherClass):
        return otherClass.all().sort(key = lambda obj: getattr(obj, attr))

    @classmethod
    def sort_by_name(cls, otherClass):
        return sorted(otherClass.all(), key = lambda x: x.name)

    @classmethod
    def count(cls, otherClass):
        return len(otherClass.all())

    @classmethod
    def find_by_name(cls, otherClass, name):
        for person in otherClass.all():
            if person.name == name:
                return person
            else:
                return "Sorry, couldn't find a person with the name, {}".format(name)

    @classmethod
    def name_starts_with(cls, otherClass, letter):
        people = []
        for person in otherClass.all():
            if person.name.startswith(letter):
                people.append(person)
        return people

    @classmethod
    def is_older_than(cls, otherClass, age):
        people = []
        for person in otherClass.all():
            if person.age > age:
                people.append(person)
        return people

    @classmethod
    def mean_age(cls, otherClass):
        people = otherClass.all()
        num = len(people)
        ages = [person.age for person in people]
        total_age = sum(ages)
        return total_age/num

    @classmethod
    def mean_age(cls, otherClass):
        people = otherClass.all()
        num = len(people)
        ages = [person.age for person in people]
        total_age = sum(ages)
        return total_age/num
