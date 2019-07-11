from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Rushee

# Application Views


# Home Page
class HomePageView(TemplateView):
    template_name = "website/home_page.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            'rushees': Rushee.objects.filter(status="FIRST").order_by('total_score')
        }
        return context


class SecondRoundView(LoginRequiredMixin, TemplateView):
    template_name = 'website/second_round.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'rushees': Rushee.objects.filter(status="SECOND")
        }
        return context


class BidView(LoginRequiredMixin, TemplateView):
    template_name = 'website/bids.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'accepted': Rushee.objects.filter(status="ACCEPTED"),
            'holding': Rushee.objects.filter(status="HOLDING"),
            'denied': Rushee.objects.filter(status="DENIED"),
        }
        return context


class CreateRushee(CreateView):
    template_name = 'website/sign_up.html'
    model = Rushee
    fields = ['name', 'phone_number', 'grade']


class UpdateRusheeStatus(UpdateView):
    model = Rushee
    fields = ['status']
    template_name = 'website/change_status.html'


class DeleteRushee(DeleteView):
    model = Rushee


class ViewRushee(DetailView):
    template_name = 'website/rushee_detail.html'
    model = Rushee
