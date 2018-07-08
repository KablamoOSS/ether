# Ether
Programatically manage secrets in AWS secrets manager.

## Build

`docker build -t ether .`

## Basic Usage

To store a secrets file:
```
cat /tmp/secret.json
{
  "username": "JimmyJoJo",
  "password": "Password12"
}
```

```
ASSUMED_ROLE='arn:aws:iam::167464XXXXXX:role/StackCreator'
MFA_SERIAL='arn:aws:iam::623551XXXXXX:mfa/IAM-F.Last'
TOKEN=123456
docker run \
    -v ~/.aws:/root/.aws \
    -v /tmp:/tmp \
    -e ASSUMED_ROLE=${ASSUMED_ROLE} \
    -e MFA_SERIAL=${MFA_SERIAL} \
    -e TOKEN=${TOKEN} \
    ether upsertSecretFile myLoginFileName /tmp/secret.json "Login details for my secret cool interweb thing"
```

To retrieve:
```
TOKEN=123456
docker run \
    -v ~/.aws:/root/.aws \
    -v /tmp:/tmp \
    -e ASSUMED_ROLE=${ASSUMED_ROLE} \
    -e MFA_SERIAL=${MFA_SERIAL} \
    -e TOKEN=${TOKEN} \
    ether getSecret myLoginFileName
{
  "username": "JommyJoJo",
  "password": "Password12"
}
```

