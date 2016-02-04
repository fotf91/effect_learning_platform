from account_app.models import EmailBasedUser

class EmailAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """
    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        try:
            user = EmailBasedUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except EmailBasedUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = EmailBasedUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except EmailBasedUser.DoesNotExist:
            return None