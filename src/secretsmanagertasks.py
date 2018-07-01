import sys
import logging
import secretsmanager
from botocore.exceptions import ClientError


class secretsmanagertasks:

    def __init__(self, session):
        self.sm = secretsmanager.secretsmanager(session)

    def generatePassword(self):
        password = self.sm.get_random_password()
        print(password)

    def upsertSecret(self, name, secret):
        exists = self.getSecretbyName(name)
        if exists:
            self.sm.update_secret_binary


    def getSecretbyName(self, name):
        secretslist = self.sm.list_secrets()
        for obj in secretslist:
            if name in obj["Name"]:
                return True
        return False

    def getSecretbyARN(self, arn):
        secretslist = self.sm.list_secrets()
        for obj in secretslist:
            if arn in obj["ARN"]:
                return True
        return False      