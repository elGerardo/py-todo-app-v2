from rest_framework_simplejwt.tokens import AccessToken

class GetAccessToken():
    def __init__(self, bearer):
        self.bearer = bearer
        self.access_token = AccessToken(bearer[7:])
        