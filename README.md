# Ether
Programatically manage secrets in AWS secrets manager.

## Build

`docker built -t ether .`

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
TOKEN=123456
docker run \
    -v ~/.aws:/root/.aws \
    -v /tmp:/tmp \
    -e ASSUMED_ROLE='arn:aws:iam::167464XXXXXX:role/StackCreator' \
    -e MFA_SERIAL='arn:aws:iam::623551XXXXXX:mfa/IAM-F.Last' \
    -e TOKEN=${TOKEN} \
    ether upsertSecretFile myLoginFileName /tmp/secret.json "Login details for my secret cool interweb thing"
```

To retrieve:
```
TOKEN=123456
docker run \
    -v ~/.aws:/root/.aws \
    -v /tmp:/tmp \
    -e ASSUMED_ROLE='arn:aws:iam::167464XXXXXX:role/StackCreator' \
    -e MFA_SERIAL='arn:aws:iam::623551XXXXXX:mfa/IAM-F.Last' \
    -e TOKEN=${TOKEN} \
    ether getSecret myLoginFileName
ewogICJ1c2VybmFtZSI6ICJKb21teUpvSm8iLAogICJwYXNzd29yZCI6ICJQYXNzd29yZDEyIgp9Cg==
```
