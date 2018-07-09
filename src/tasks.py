from invoke import task
import auth
import secretsmanagertasks


@task
def generateRandPassword(ctx):
    session = getBaseSession()
    smtasks = secretsmanagertasks.secretsmanagertasks(session)
    smtasks.generatePassword()

@task
def upsertSecretString(ctx, name, secret, description, kmskey=None, logoutput=None):
    session = getBaseSession()
    smtasks = secretsmanagertasks.secretsmanagertasks(session)
    smtasks.upsertSecretString(name=name, secret=secret, description=description, logoutput=logoutput)

@task
def upsertSecretFile(ctx, name, secretfile, description, kmskey=None, logoutput=None):
    session = getBaseSession()
    smtasks = secretsmanagertasks.secretsmanagertasks(session)
    smtasks.upsertSecretsFile(name=name, secretfile=secretfile, description=description, logoutput=logoutput)

@task
def rotateSecret(ctx, name, rotationdays, logoutput=None):
    session = getBaseSession()
    smtasks = secretsmanagertasks.secretsmanagertasks(session)
    smtasks.rotateSecret(name=name, rotationdays=rotationdays, logoutput=logoutput)

@task
def rotateSecretbyLambda(ctx, name, rotationdays, lambdaarn, logoutput=None):
    session = getBaseSession()
    smtasks = secretsmanagertasks.secretsmanagertasks(session)
    smtasks.rotateSecretbyLambda(name=name, rotationdays=rotationdays, lambdaarn=lambdaarn, logoutput=logoutput)

@task
def getSecret(ctx, name, logoutput=None):
    session = getBaseSession()
    smtasks = secretsmanagertasks.secretsmanagertasks(session)
    smtasks.getSecret(name=name, logoutput=logoutput)

def getBaseSession(region='ap-southeast-2'):
    authentication = auth.authenticate(region)
    session = authentication.getSession()
    return session
