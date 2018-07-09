import sys
import logging
import secretsmanager
import uuid
import awsinputs
import kmstasks
import json
import fileutil
import base64
import botocore.errorfactory
from botocore.exceptions import ClientError


class secretsmanagertasks:

    def __init__(self, session):
        self.sm = secretsmanager.secretsmanager(session)
        self.kms = kmstasks.kmstasks(session)
        self.fs = fileutil.fileutil()

    def generatePassword(self):
        password = self.sm.get_random_password()
        print(password)

    def upsertSecretString(self, name, secret, description, kmskey=None, tags=None, token=None, logoutput=None):
        #if not awsinputs.IsKMSArn(kmskey) or kmskey=="aws/secretsmanager":
        #    kmskey = self.kms.getKeyARNbyAlias(kmskey)
        if token is None:
            token = self.generateClientToken()
        exists = self.getSecretbyName(name)
        if exists:
            try:
                response = self.sm.update_secret_string(
                    SecretId=name,
                    SecretString=secret,
                    ClientRequestToken=token,
                    Description=description,
                    KmsKeyId=kmskey
                )
            except ClientError as err:
                print err
                sys.exit(1)
        else:
            try:
                response = self.sm.create_secret_string(
                    Name=name,
                    SecretString=secret,
                    ClientRequestToken=token,
                    Description=description,
                    KmsKeyId=kmskey,
                    Tags=tags
                )
            except ClientError as err:
                print err
                sys.exit(1)
        if logoutput:
            print json.dumps(response, default=str, sort_keys=True, indent=4, separators=(',', ': '))
        print response

    def upsertSecretsFile(self, name, secretfile, description, kmskey=None, tags=None, token=None, logoutput=None):
        #if not awsinputs.IsKMSArn(kmskey) or kmskey=="aws/secretsmanager":
        #    kmskey = self.kms.getKeyARNbyAlias(kmskey)
        content = self.fs.readSecret(secretfile)
        if token is None:
            token = self.generateClientToken()
        exists = self.getSecretbyName(name)
        if exists:
            try:
                response = self.sm.update_secret_binary(
                    SecretId=name,
                    SecretBinary=content.encode(),
                    ClientRequestToken=token,
                    Description=description,
                    KmsKeyId=kmskey
                )
            except ClientError as err:
                print err
                sys.exit(1)
        else:
            try:
                response = self.sm.create_secret_binary(
                    Name=name,
                    SecretBinary=content.encode(),
                    ClientRequestToken=token,
                    Description=description,
                    KmsKeyId=kmskey,
                    Tags=tags
                )
            except ClientError as err:
                print err
        if logoutput:
            print json.dumps(response, default=str, sort_keys=True, indent=4, separators=(',', ': '))

    def rotateSecret(self, name, token=None, rotationdays=60, logoutput=None):
        if token is None:
            token = self.generateClientToken()
        exists = self.getSecretbyName(name)
        if exists:
            try:
                response = self.sm.rotate_secret(
                    SecretId = name,
                    ClientRequestToken=token,
                    RotationRules=self.generateRotationRules(rotationdays)
                )
            except ClientError as err:
                print err
                sys.exit(1)
        else:
            print "Secret: " + name + " does not exist, cannot rotate secret"
            sys.exit(1)
        
        if logoutput:
            print json.dumps(response, default=str, sort_keys=True, indent=4, separators=(',', ': '))
    
    def rotateSecretbyLambda(self, name, lambdaarn, token=None, rotationdays=60, logoutput=None):
        if token is None:
            token = self.generateClientToken()
        exists = self.getSecretbyName(name)
        if exists:
            try:
                response = self.sm.rotate_secret_lambda(
                    SecretId = name,
                    ClientRequestToken=token,
                    RotationRules=self.generateRotationRules(rotationdays),
                    RotationLambdaARN=lambdaarn
                )
            except ClientError as err:
                print err
                sys.exit(1)
        else:
            print "Secret: " + name + " does not exist, cannot rotate secret"
            sys.exit(1)
        
        if logoutput:
            print json.dumps(response, default=str, sort_keys=True, indent=4, separators=(',', ': '))

    def getSecret(self, name, versionid=None, logoutput=None):
        try:
            response = self.sm.get_secret_value(
                SecretId=name,
                VersionId=versionid
            )
        except ClientError as err:
            print err
            sys.exit(1)

        if logoutput:
            print json.dumps(response, default=str, sort_keys=True, indent=4, separators=(',', ': '))

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            if "SecretString" in response:
                print response["SecretString"]
            else:
                print response["SecretBinary"]
            sys.exit(0)


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

    def generateRotationRules(self, days=60):
        rules = {
           'AutomaticallyAfterDays': days
        }

        return rules
