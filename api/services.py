from api.models import User


class UserService:
    def __init__(self, user_model=User):
        self.user_model = user_model

    def find(self, email=None):
        user = self.user_model.objects.get(email=email)
        if user:
            return user
        else:
            raise UserNotFoundException()


class UserNotFoundException(Exception):
    pass
