from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

from .models import Rushee, Comment


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
    success_url = reverse_lazy("webiste:home_page")

class UpdateRusheeScore(UpdateView):
    model = Rushee
    fields = ['total_score']
    template_name = 'website/change_status.html'
    success_url = reverse_lazy("website:home_page")

class DeleteRushee(DeleteView):
    model = Rushee


class ViewRushee(DetailView):
    template_name = 'website/rushee_detail.html'
    model = Rushee

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        rushee = Rushee.objects.get(pk=self.kwargs.get('pk'))
        context['comments'] = Comment.objects.filter(rushee=rushee)
        return context

class AddComment(CreateView):
    model = Comment
    fields = ['brother', 'comment']
    template_name = 'website/change_status.html'

    def form_valid(self, form):
        rushee = Rushee.objects.get(pk=self.kwargs.get('pk'))
        self.object = form.save(commit=False)
        self.object.rushee = rushee
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
