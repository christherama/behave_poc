from api.models import User


class UserService:
    @classmethod
    def find(cls, email=None):
        user = User.objects.filter(email=email)
        if user.exists():
            return user.last()
        else:
            raise UserNotFoundException()


class UserNotFoundException(Exception):
    pass
