from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Code


class AccessCodeRequired(UserPassesTestMixin):
    login_url = "website:enter_code"

    def test_func(self):
        if self.request.user.is_active:
            return True
        else:
            return self.request.session.get('access', False)
