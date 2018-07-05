import os
import sys
import json

class fileutil:

    def __init__(self):
        pass
    
    def readSecret(self, file_name):
        directory = os.path.dirname(__file__)

        path = file_name

        content = []
        try:
            with open(os.path.join(directory + "/data", path), 'r') as file_name:
                content = file_name.read()
        except IOError as err:
            print err
            sys.exit(1)
        
        return content

    def readSecretBinary(self, file_name):
        directory = os.path.dirname(__file__)

        path = file_name

        content = []
        try:
            with open(os.path.join(directory + "/data", path), 'rb') as file_name:
                content = file_name.read()
        except IOError as err:
            print err
            sys.exit(1)
        
        return content

    def writeSecret(self, data, name, directory, logging=None):
        filedirectory = os.path.dirname(os.path.realpath(__file__))
        targetdirectory = os.path.join(
            filedirectory, directory)

        if not os.path.exists(targetdirectory):
            os.makedirs(targetdirectory)
        
        path = '{directory}/{file_name}'.format(file_name=name, directory=directory)

        with open(os.path.join(filedirectory, path), "wb") as fh:
            fh.write(json.dumps(data))