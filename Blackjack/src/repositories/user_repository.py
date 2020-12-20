import os
from pathlib import Path
from config import USER_REPOSITORY_FILE_PATH


class UserRepository:
    def __init__(self):
        self.file_path = USER_REPOSITORY_FILE_PATH

    def init_user_settings(self):
        # Use touch to see if file exists
        Path(self.file_path).touch()

    def read_user_settings(self):
        # Read Player settings data from reposition.
        file_open = ""
        try:
            file_open = open(self.file_path, "r")
        except IOError:
            print("File not found!")
        data_read = file_open.read()
        file_open.close()
        user, cash = data_read.split(",")
        return user, cash

    def write_user_settings(self, data):
        # Write Player settings data to reposition.
        file_write = ""
        try:
            file_write = open(self.file_path, "w+")
        except IOError:
            print("File not found!")
        file_write.write('{0},{1}\n'.format(data[0], data[1]))
        file_write.close()
