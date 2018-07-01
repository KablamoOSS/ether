import sys
import logging
import secretsmanager
import uuid
import awsinputs
import kmstasks
from botocore.exceptions import ClientError


class secretsmanagertasks:

    def __init__(self, session):
        self.sm = secretsmanager.secretsmanager(session)
        self.kms = kmstasks.kmstasks(session)

    def generatePassword(self):
        password = self.sm.get_random_password()
        print(password)

    def upsertSecretString(self, name, secret, description, kmskey="aws/secretsmanager", token=None):
        if !awsinputs.IsKMSArn(kmskey):
            kmskey = self.kms.getKeyARNbyAlias(kmskey)
        if token is None:
            token = self.generateClientToken()
        exists = self.getSecretbyName(name)
        if exists:
            response = self.sm.update_secret_string(
                SecretId=name,
                SecretString=secret,
                ClientRequestToken=token,
                Description=description, 
                KmsKeyId=kmskeyid
            )
        else:
            response = self.sm.update_secret_string(
                SecretId=name,
                SecretString=secret,
                ClientRequestToken=token,
                Description=description,
                KmsKeyId=kmskeyid
            )

        print


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
    
    def generateClientToken(self):
        token = uuid.uuid4()
        
        return str(token)