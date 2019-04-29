from api.models import User


class UserService:

    @classmethod
    def find(cls, email=None):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise UserNotFoundException()


class UserNotFoundException(Exception):
    pass
