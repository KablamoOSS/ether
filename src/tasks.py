from invoke import task
import auth
import secretsmanagertasks


@task
def generateRandPassword(ctx):
    session = getBaseSession()
    smtasks = secretsmanagertasks.secretsmanagertasks(session)
    smtasks.generatePassword()

def getBaseSession(region='ap-southeast-2'):
    authentication = auth.authenticate(region)
    session = authentication.getSession()
    return session
