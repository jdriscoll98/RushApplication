from django.contrib.auth.mixins import UserPassesTestMixin


class AccessCodeRequired(UserPassesTestMixin):
    login_url = "website:enter_code"

    def test_func(self):
        try:
            self.request.session['access']
        except KeyError as e:
            print(e)
            return False
        return True
