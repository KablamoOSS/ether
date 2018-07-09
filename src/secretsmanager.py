
class secretsmanager:

    def __init__(self, session):
        self.smClient = session.client('secretsmanager')

    def cancel_rotate_secret(self, SecretId):
        response = self.smClient.cancel_rotate_secret(
            SecretId=SecretId
        )

        return response["VersionId"]

    def create_secret_binary(self, Name, ClientRequestToken, Description, SecretBinary, Tags=None, KmsKeyId=None):
        if Tags == None:
            Tags = self.generate_tags(Name)
        if KmsKeyId == None:
            KmsKeyId = ""
        response = self.smClient.create_secret(
            Name=Name,
            ClientRequestToken=ClientRequestToken,
            Description=Description,
            KmsKeyId=KmsKeyId,
            SecretBinary=SecretBinary,
            Tags=Tags
        )

        return response["ARN"], response["Name"]

    def create_secret_string(self, Name, ClientRequestToken, Description, SecretString, Tags=None, KmsKeyId=None):
        if Tags == None:
            Tags = self.generate_tags(Name)
        if KmsKeyId == None:
            KmsKeyId = ""
        response = self.smClient.create_secret(
            Name=Name,
            ClientRequestToken=ClientRequestToken,
            Description=Description,
            KmsKeyId=KmsKeyId,
            SecretString=SecretString,
            Tags=Tags
        )

        return response["ARN"], response["Name"]

    def delete_resource_policy(self, SecretId):
        response = self.smClient.delete_resource_policy(
            SecretId=SecretId
        )

        return response["ARN"], response["Name"]

    def delete_secret(self, SecretId, RecoveryWindowInDays=30):
        response = self.smClient.delete_secret(
            SecretId=SecretId,
            RecoveryWindowInDays=RecoveryWindowInDays
        )

        return response

    def describe_secret(self, SecretId):
        response = self.smClient.describe_secret(
            SecretId=SecretId
        )

        return response

    def get_random_password(self, PasswordLength=32, ExcludeCharacters="\/0!^&`", ExcludeNumbers=False, ExcludePunctuation=True, ExcludeUppercase=False, ExcludeLowercase=False, IncludeSpace=False, RequireEachIncludedType=True):
        response = self.smClient.get_random_password(
            PasswordLength=PasswordLength,
            ExcludeCharacters=ExcludeCharacters,
            ExcludeNumbers=ExcludeNumbers,
            ExcludePunctuation=ExcludePunctuation,
            ExcludeUppercase=ExcludeUppercase,
            ExcludeLowercase=ExcludeLowercase,
            IncludeSpace=IncludeSpace,
            RequireEachIncludedType=RequireEachIncludedType,
        )

        return response["RandomPassword"]

    def get_resource_policy(self, SecretId):
        response = self.smClient.get_resource_policy(
            SecretId=SecretId
        )

        return response["ResourcePolicy"]

    def get_secret_value(self, SecretId, VersionId=None, VersionStage=None):
        if VersionId:
            response = self.smClient.get_secret_value(
                SecretId=SecretId,
                VersionId=VersionId
            )
        else:
            response = self.smClient.get_secret_value(
                SecretId=SecretId
            )

        return response
    
    def list_secret_version_ids(self, SecretId, IncludeDeprecated=False):
        versions = []
        response = self.smClient.list_secret_version_ids(
            SecretId=SecretId,
            IncludeDeprecated=IncludeDeprecated
        )
        versions.extend(response["Versions"])
        while "NextToken" in response:
            response = self.smClient.list_secret_version_ids(
                SecretId=SecretId,
                IncludeDeprecated=IncludeDeprecated,
                NextToken=response["NextToken"]
            )
            versions.extend(response["Versions"])
        
        return versions
    
    def list_secrets(self):
        secrets = []
        response = self.smClient.list_secrets()
        secrets.extend(response["SecretList"])
        while "NextToken" in response:
            response = self.smClient.list_secrets(
                NextToken=response["NextToken"]
            )
            secrets.extend(response["SecretList"])
        
        return secrets
    
    def put_resource_policy(self, SecretId, ResourcePolicy):
        response = self.smClient.put_resource_policy(
            SecretId=SecretId,
            ResourcePolicy=ResourcePolicy
        )

        return response["ARN"], response["Name"]

    def put_secret_value_binary(self, SecretId, ClientRequestToken, SecretBinary, VersionStages):
        response = self.smClient.put_secret_value(
            SecretId=SecretId,
            ClientRequestToken=ClientRequestToken,
            SecretBinary=SecretBinary,
            VersionStages=VersionStages
        )

        return response

    def put_secret_value_string(self, SecretId, ClientRequestToken, SecretString, VersionStages):
        response = self.smClient.put_secret_value(
            SecretId=SecretId,
            ClientRequestToken=ClientRequestToken,
            SecretString=SecretString,
            VersionStages=VersionStages
        )

        return response

    def restore_secret(self, SecretId):
        response = self.smClient.restore_secret(
            SecretId=SecretId
        )

        return response["ARN"], response["Name"]
    
    def rotate_secret(self, SecretId, ClientRequestToken, RotationRules):
        response = self.smClient.rotate_secret(
            SecretId=SecretId,
            ClientRequestToken=ClientRequestToken,
            RotationRules=RotationRules
        )

        return response

    def rotate_secret_lambda(self, SecretId, ClientRequestToken, RotationLambdaARN, RotationRules):
        response = self.smClient.rotate_secret(
            SecretId=SecretId,
            ClientRequestToken=ClientRequestToken,
            RotationLambdaARN=RotationLambdaARN,
            RotationRules=RotationRules
        )

        return response

    def tag_resource(self, SecretId, Tags):
        self.smClient.tag_resource(
            SecretId=SecretId,
            Tags=self.generate_tags(name=SecretId)
        )

    def untag_resource(self, SecretId, TagKeys):
        self.smClient.untag_resource(
            SecretId=SecretId,
            TagKeys=TagKeys
        )

    def update_secret_binary(self, SecretId, ClientRequestToken, Description, SecretBinary, KmsKeyId=None):
        if KmsKeyId == None:
            KmsKeyId = ""
        response = self.smClient.update_secret(
            SecretId=SecretId,
            ClientRequestToken=ClientRequestToken,
            Description=Description,
            SecretBinary=SecretBinary,
            KmsKeyId=KmsKeyId
        )

        return response

    def update_secret_string(self, SecretId, ClientRequestToken, Description, SecretString, KmsKeyId=None):
        if KmsKeyId == None:
            KmsKeyId = ""
        response = self.smClient.update_secret(
            SecretId=SecretId,
            ClientRequestToken=ClientRequestToken,
            Description=Description,
            SecretString=SecretString,
            KmsKeyId=KmsKeyId
        )

        return response

    def update_secret_version_stage(self, SecretId, VersionStage, MoveToVersionId):
        response = self.smClient.update_secret_version_stage(
            SecretId=SecretId,
            VersionStage=VersionStage,
            MoveToVersionId=MoveToVersionId
        )

        return response["ARN"], response["Name"]
    
    def generate_tags(self, name):
        tags = [
            {
                'Key': 'Name',
                'Value': name
            }
        ]

        return tags
