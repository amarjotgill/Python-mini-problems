"""
File: files_and_folders.py
Author: Amarjot Gill
Date: 12/10/2020
Lab Section: 44
Email:  agill3@umbc.edu
Description:  This program will use Classes to mimic the UMBC
Gl server. It can create directories and files and navigate through them
using cd. It can also write to files only if they are open.
"""


class CommandLine:
    def __init__(self):
        self.root = Directory('', None)
        self.current_path = self.root

    def run(self):
        command = input('>>> ')
        while command.strip().lower() != 'exit':
            split_command = command.split()
            if len(split_command):
                if split_command[0] == 'ls':
                    self.current_path.display()
            if len(split_command) >= 2:
                if split_command[0] == 'cd':
                    self.change_directory(split_command[1])
                elif split_command[0] == 'makedir':
                    self.current_path.create_directory(split_command[1])
                elif split_command[0] == 'fcreate':
                    self.current_path.create_file(split_command[1])
                elif split_command[0] == 'fwrite':
                    self.current_path.file_write(split_command[1])
                elif split_command[0] == 'fread':
                    self.current_path.file_read(split_command[1])
                elif split_command[0] == 'fclose':
                    self.current_path.close_file(split_command[1])
                elif split_command[0] == 'fopen':
                    self.current_path.open_file(split_command[1])

            command = input('>>> ')

    def change_directory(self, dir_name):
        # checks if the entered name is a parent directory and sets it to that if it is
        if self.current_path.parent:
            if self.current_path.parent.name == dir_name:
                self.current_path = self.current_path.parent
        else:
            # if it's not a parent directory it will check if it is a current
            # directory in this one and set the current_path to that
            for i in range(len(self.current_path.made_directory)):
                if self.current_path.made_directory[i].name == dir_name:
                    self.current_path = self.current_path.made_directory[i]


class Directory:
    def __init__(self, name, parent):
        # file_list has all files made in this directory
        self.file_list = []
        # contains all made directories
        self.made_directory = []
        self.name = name
        # this will set the parent directory = to self.parent
        self.parent = parent

    def display(self):
        # simple display, display's the directories and files
        print("Directories in", self.name + ":")
        for directory in self.made_directory:
            print(directory.name)

        print("Files in", self.name + ":")
        for file in self.file_list:
            print(file.name)

    def create_file(self, file_name):
        file_exist = False
        # checks too see if file with the name entered already exist in this directory
        for i in range(len(self.file_list)):
            if self.file_list[i].name == file_name:
                print("This file has already been created")
                file_exist = True
        # if the file does not already exist it will be created
        if not file_exist:
            new = File(file_name, opened=False)
            self.file_list.append(new)

    def create_directory(self, dir_name):
        dir_exist = False
        # checks to see if a directory with the name entered already exist in this directory
        for i in range(len(self.made_directory)):
            if self.made_directory[i].name == dir_name:
                print("The directory already exist")
                dir_exist = True
        # if it does not a new directory will be made
        if not dir_exist:
            new = Directory(dir_name, self)
            self.made_directory.append(new)

    def file_write(self, file_name):
        file_exist = False
        # searchs file list to find name
        for i in range(len(self.file_list)):
            if self.file_list[i].name == file_name:
                file_exist = True
                # if the file is opened you can write to it
                if self.file_list[i].opened:
                    writing = input("What would u like to write?")
                    self.file_list[i].contents.append(writing)
                # will let user know file has to be opened
                elif not self.file_list[i].opened:
                    print("File must be opened before you can write in it")
        # will let user know file does not exist if it was not found
        if not file_exist:
            print("The file does not currently exist in this directory")

    def file_read(self, file_name):
        file_exist = False
        for i in range(len(self.file_list)):
            # finds the file
            if self.file_list[i].name == file_name:
                file_exist = True
                # checks if the contents list has words in it
                if self.file_list[i].contents:
                    for line in self.file_list[i].contents:
                        # reads the contents
                        print(line)

        if not file_exist:
            print("The file does not currently exist in this directory")

    def close_file(self, file_name):
        file_exist = False
        for i in range(len(self.file_list)):
            # finds file name and sets it opened to false
            if self.file_list[i].name == file_name:
                self.file_list[i].opened = False
                file_exist = True

        if not file_exist:
            print("The file does not currently exist in this directory")

    def open_file(self, file_name):
        file_exist = False
        for i in range(len(self.file_list)):
            # finds file, sets it open to true and resets all it's contents
            if self.file_list[i].name == file_name:
                file_exist = True
                self.file_list[i].opened = True
                self.file_list[i].contenets = []

        if not file_exist:
            print("The file does not currently exist in this directory")


class File:
    def __init__(self, name, opened):
        self.name = name
        self.opened = opened
        # this list will mimic the file io
        self.contents = []


if __name__ == '__main__':
    cmd_line = CommandLine()
    cmd_line.run()
