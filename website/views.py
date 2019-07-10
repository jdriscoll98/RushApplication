from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Rushee

# Application Views


# Home Page
class HomePageView(TemplateView):
    template_name = "website/home_page.html"


# Profile Page
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "website/profile.html"


class CreateRushee(CreateView):
    model = Rushee
    fields = ['name','phone_number','email','grade','brothers_known']

class UpdateRushee(UpdateView):
    model = Rushee

class DeleteRushee(DeleteView):
    model = Rushee

class ViewRushee(DetailView):
    model = Rushee
