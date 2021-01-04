"""
File: houses_and_people.py
Author: Amarjot Gill
Date: 10/31/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will use classes in order to determine
which created person is in which house, it will keep track if they leave
or enter each house using booleans

"""


class Person:
    def __init__(self, name):
        self.name = name
        # used to see if someone is already in the house
        self.already_inside = False
        self.the_house = None

    def go_in(self, the_house):
        self.the_house = the_house
        # if they are not in the house they will be set to True so in the house
        # and their name will be appended into the people list
        if not self.already_inside:
            self.already_inside = True
            the_house.people.append(self)
        # if self.inside is True that means they are already in the House
        else:
            return 'the person is already in the house'

    def leave(self, the_house):
        self.the_house = the_house
        # if they are already inside then they will be removed from people list
        # also already inside will be set to False so they will no longer be inside
        if self.already_inside:
            the_house.people.remove(self)
            self.already_inside = False
            self.the_house = None
        # if they are not inside then this will print to let then know
        else:
            return 'the person is not in the house'


class House:
    def __init__(self, address):

        self.address = address
        self.house = address
        # list for people in a house
        self.people = []

    def display(self):
        # will display all created houses and a list of people in each house
        print('The house is at: {} '.format(self.address))
        for name in self.people:
            print(name.name)
        return self


if __name__ == '__main__':
    print('The options are:\n\tcreate <person name>\n\tperson-name enter house-address\n\tperson-name exit house-address\n\tdisplay')
    in_string = input('What do you want to do? ')
    people_list = []
    house_list = []
    while in_string.strip().lower() not in ['quit', 'q']:
        enter_string = in_string.split('enter')
        exit_string = in_string.split('exit')
        if in_string.split()[0:2] == ['create', 'person']:
            people_list.append(Person(' '.join(in_string.split()[2:])))
            print('Person {} created'.format(people_list[-1].name))
        elif in_string.split()[0:2] == ['create', 'house']:
            house_list.append(House(' '.join(in_string.split()[2:])))
            print('House {} created'.format(house_list[-1].address))
        elif len(enter_string) == 2:
            if not any(enter_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(enter_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == enter_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == enter_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.go_in(the_house)
                else:
                    print('Something went wrong.  ')
        elif len(exit_string) == 2:
            if not any(exit_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(exit_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == exit_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == exit_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.leave(the_house)
                else:
                    print('Something went wrong.  ')
        elif in_string.lower().strip() == 'display':
            for house in house_list:
                house.display()
            print('These people aren\'t in a house')
            for person in people_list:
                if not person.the_house:
                    print(person.name)

        in_string = input('What do you want to do? ')
