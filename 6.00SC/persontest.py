import person
import datetime

Person = person.Person
me = Person('Bob Smith')
him = Person('Jo Mo')
her = Person('Jenny')
print him.getLastName()
him.setBirthday(datetime.date(1980, 4, 2))
her.setBirthday(datetime.date(1980, 4, 10))
print 'he is', him.getAge(), 'old'
print 'there are', Person.ID, 'people'
