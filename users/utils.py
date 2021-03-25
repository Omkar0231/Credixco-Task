from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        if not user.password_change_request:
            timestamp = None
        return text_type(user.pk) + text_type(timestamp) + text_type(user.email)

token_generator = AppTokenGenerator()