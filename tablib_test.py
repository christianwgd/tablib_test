from dataclasses import dataclass

import tablib
import faker
import bs4


@dataclass
class Person:
    first_name: str
    last_name: str
    zip: str
    city: str
    street: str

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def address(self):
        return f"{self.zip} {self.city}, {self.street}"

    def as_list(self):
        return [self.last_name, self.first_name, self.zip, self.city, self.street]


def tablib_test():
    persons = tablib.Dataset()
    persons.headers = list(Person.__annotations__)

    fake = faker.Faker('de_DE')
    for _ in range(10):
        person = Person(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            zip=fake.postcode(),
            city=fake.city(),
            street=fake.street_address(),
        )
        persons.append(person.as_list())
    print('test')
    print(persons)
    print('dict')
    print(persons.dict)
    print('csv')
    print(persons.export('csv'))
    print('json')
    print(persons.export('json'))
    print('html')
    formatter = bs4.formatter.HTMLFormatter(indent=4)
    soup = bs4.BeautifulSoup(persons.export('html'), features="html.parser")
    print(soup.prettify(formatter=formatter))


if __name__ == '__main__':
    tablib_test()