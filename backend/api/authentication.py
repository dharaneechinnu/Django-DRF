from rest_framework.authentication import TokenAuthentication as BaseToken
from rest_framework.authtoken.models import Token

class TokenAuthentication(BaseToken):
    keyword = 'bearer'