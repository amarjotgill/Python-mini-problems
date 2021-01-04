"""
File: smart_house.py
Author: Amarjot Gill
Date: 11/16/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will use classes and file io
in order to create a smart house, this smart house keeps track
of which devices are on and off, you also are allowed to save and load files
when saving a file you will overwrite any previosue file
"""
FALSE = "False"


class Device:
    def __init__(self, name, toggle):
        self.name = name
        self.toggle = toggle


class SmartHouse:
    def __init__(self, address):
        self.address = address
        # this list will keep track of all devices created
        self.device_list = []

    def add_device(self, device):
        # adds device too device list
        self.device_list.append(device)

    def get_device(self, the_id):
        for i in range(len(self.device_list)):
            # checks if the_id entered exist in the list will return the device if it does
            if self.device_list[i].name == the_id:
                return self.device_list[i]

    def save_house(self, file_name):
        # creates the file
        file_namer = open(file_name, "w")

        for device in self.device_list:
            # adds device name and if they are toggled to each line
            file_namer.write("device {} toggle {}".format(device.name, device.toggle) + "\n")

        file_namer.close()

    def load_house(self, file_name):
        open_file = open(file_name, "r")

        for line in open_file:
            split_line = line.split()
            # if the device is toggled off then it will be created with
            # the toggle set to false
            if split_line[3] == FALSE:
                # split_line[1] is the device name
                device = Device(split_line[1], False)
            else:
                device = Device(split_line[1], True)
            # appends device to the list
            self.device_list.append(device)

        open_file.close()

    def display(self):
        print("For the house at", self.address)
        for device in self.device_list:
            # if the device toggle is True it will print it is on
            if device.toggle:
                print(device.name, "is on")
            # if the device toggle is False it will print it is off
            if not device.toggle:
                print(device.name, "is off")


if __name__ == '__main__':
    address = input('What is the address of the house?')
    house = SmartHouse(address)

    command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
    while command != 'quit':
        if command == 'add' or command == 'add device':
            the_id = input('What is the device id?')
            if not house.get_device(the_id):
                yes_no = input('Is the device on? (yes/no)')
                if yes_no == 'yes':
                    house.add_device(Device(the_id, True))
                elif yes_no == 'no':
                    house.add_device(Device(the_id, False))
            else:
                print('There is no device id: {} in the ')
        elif command == 'toggle' or command == 'toggle device':
            the_id = input('What is the device id?')
            the_device = house.get_device(the_id)
            if the_device:
                on_off_toggle = input('On, Off or Toggle? ').lower()
                if on_off_toggle == 'on':
                    the_device.toggle = True
                elif on_off_toggle == 'off':
                    the_device.toggle = False
                elif on_off_toggle == 'toggle':
                    the_device.toggle = not the_device.toggle
            else:
                print('There is no device id: {} in the ')
        elif command == 'load':
            file_name = input('What is the filename to load from? ')
            house.load_house(file_name)
            print('The house has been loaded from {}'.format(file_name))
        elif command == 'save':
            file_name = input('What is the filename to save as? ')
            house.save_house(file_name)
            print('The house has been saved in {}'.format(file_name))
        elif command == 'display':
            house.display()
        else:
            print('unknown command', command)

        command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
