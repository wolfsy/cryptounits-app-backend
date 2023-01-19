from django.conf import settings
import jwt, datetime, json
from rest_framework.exceptions import AuthenticationFailed

def create_access_token(UserId):
    payload = {
            'UserId': UserId,
            'Expiration': json.dumps(datetime.datetime.utcnow() + datetime.timedelta(minutes = 60), indent=4, sort_keys=True, default=str),
            'TokenCreationTime': json.dumps(datetime.datetime.utcnow(), indent=4, sort_keys=True, default=str)
        }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm = 'HS256')

def decode_access_token(accessToken):
    try:
        payload = jwt.decode(accessToken, settings.SECRET_KEY, algorithms = ['HS256'])
        return payload['UserId']
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('User unauthenticated!')
    