from tkinter import N


class person():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

person_1 = person("Fry", "fry@planetexpress.com", "111-111-1111")
person_2 = person("Lela", "lela@planetexpress.com", "222-222-2222")
person_3 = person("Bender", "bender@momcorp.com", "333-333-3333")

planet_express = [person_1, person_2, person_3]


def print_people(people):
    print("------------")
    for person in people:
        print(f"Name: {person.name}\nEmail: {person.email}\nNumber: {person.phone}\n")
    print("------------")

print_people(planet_express)

person_3.email = "bender@planetexpress.com"

print_people(planet_express)