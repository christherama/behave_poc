from api.models import User


class UserService:
    def __init__(self, user_model=User):
        self.user_model = user_model

    def find(self, email=None):
        try:
            user = self.user_model.objects.get(email=email)
        except User.DoesNotExist:
            raise UserNotFoundException()
        else:
            return user


class UserNotFoundException(Exception):
    pass
