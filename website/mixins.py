from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Code


class AccessCodeRequired(UserPassesTestMixin):
    login_url = "website:enter_code"

    def test_func(self):
        try:
            return self.request.session['access'] == str(Code.objects.get(pk=1).code)
        except KeyError as e:
            if self.request.user.is_active:
                return True
            else:
                return False
