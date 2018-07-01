import sys
import logging
import kms
import uuid
from botocore.exceptions import ClientError


class kmstasks:

    def __init__(self, session):
        self.kmstask = kms.kms(session)
    
    def getKeyARNbyAlias(self, keyalias):
        response = self.kmstask.list_aliases()
        for alias in response:
            if keyalias in alias["AliasName"]:
                keyid = alias["TargetKeyId"]
                keymetadata = self.kmstask.describe_key(KeyId=keyid)
                return keymetadata["Arn"]
            else:
                return None
