from django.conf.urls import url

from .views import *

# Application Routes (URLs)


app_name = "website"

urlpatterns = [
    # Home Page
    url(r"^$", HomePageView.as_view(), name="home_page"),
    url(r"^upstairs/$", SecondRoundView.as_view(), name="second_round"),
    url(r"^bids/$", BidView.as_view(), name="bid_status"),
    url(r"^register$", CreateRushee.as_view(), name="register"),
    url(r"^change-status/(?P<pk>\d+)/$", UpdateRusheeStatus.as_view(), name="change_status"),
    url(r"^rushee/(?P<pk>\d+)/$", ViewRushee.as_view(), name="rushee_detail"),
]
