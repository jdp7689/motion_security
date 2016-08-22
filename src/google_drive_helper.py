#!/usr/bin/python

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleDriveHelper():
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, filename):
        file = self.drive.CreateFile()
        file.SetContentFile(filename)
        file.Upload()

def main():
    drive = GoogleDriveHelper()
    drive.upload_file("test.txt")
    print "Upload successful!"

if __name__ == '__main__':
    main()
