class kms:

    def __init__(self, session):
        self.kmsClient = session.client('kms')

    def list_keys(self):
        keys = []
        response = self.kmsClient.list_keys()
        keys.append(response["Keys"])
        while "NextToken" in response:
            response = self.kmsClient.list_keys(
                NextToken=response["NextToken"]
            )
            keys.append(response["Keys"])
        
        return keys

    def list_aliases(self):
        aliases = []
        response = self.kmsClient.list_aliases()
        aliases.append(response["Aliases"])
        while "NextToken" in response:
            response = self.kmsClient.list_aliases(
                NextToken=response["NextToken"]
            )
            aliases.append(response["Aliases"])
        
        return aliases
    
    def describe_key(self, KeyId):
        response = self.kmsClient.describe_key(
            KeyId=KeyId
        )
        if "KeyMetadata" in response:
            return response["KeyMetadata"]
        else:
            return None
