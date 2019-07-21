from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView , FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import View
from django.contrib import messages
from .mixins import AccessCodeRequired

from .forms import CodeForm
from .models import Rushee, Comment

# Application Views


# Home Page
class HomePageView(AccessCodeRequired, TemplateView):
    template_name = "website/home_page.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            'rushees': Rushee.objects.filter(status="FIRST")
        }
        return context


class SecondRoundView(TemplateView):
    template_name = 'website/second_round.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'rushees': Rushee.objects.filter(status="SECOND")
        }
        return context


class BidView(TemplateView):
    template_name = 'website/bids.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'accepted': Rushee.objects.filter(status="ACCEPTED"),
            'holding': Rushee.objects.filter(status="HOLDING"),
            'denied': Rushee.objects.filter(status="DENIED"),
        }
        return context


class CreateRushee(SuccessMessageMixin, CreateView):
    template_name = 'website/sign_up.html'
    model = Rushee
    fields = ['name', 'phone_number', 'grade']
    success_url = reverse_lazy('website:register')
    success_message = 'Thank you for registering!'


class UpdateRusheeStatus(UpdateView):
    model = Rushee
    fields = ['status']
    template_name = 'website/change_status.html'
    success_url = reverse_lazy("website:home_page")


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

class PostVoteView(View):
    def post(self, *args, **kwagrs):
        data = {
            'success': False
        }
        try:
            print(self.request.POST.get('pk'))
            rushee = Rushee.objects.get(pk=self.request.POST.get('pk'))
            comment = self.request.POST.get('comment')
            new_brother = self.request.POST.get('new-brother')
            self.request.POST.get('')
            if comment:
                new_comment = Comment(comment=comment, rushee=rushee)
                new_comment.save()
            rushee.currently_talking_to = new_brother
            rushee.save()
        except Exception as e:
            print(str(e))
            messages.error(self.request, 'Error: ' + str(e))
        return JsonResponse(data)



class Vote(View):
    def post(self, *args, **kwargs):
        if self.request.is_ajax:
            data = {
                'success': False
            }
            try:
                rushee = Rushee.objects.get(pk=self.request.POST.get('pk'))
                vote = int(self.request.POST.get('vote'))
                try:
                    self.request.session[rushee.name]
                except KeyError:
                    rushee.total_score += vote
                    rushee.save()
                    data['success'] = True
                    self.request.session[rushee.name] = 'voted'
                    data['score'] = rushee.total_score
            except Exception as e:
                messages.error(self.request, 'Unable to vote on rushee at this time')
            return JsonResponse(data)


class AccessCode(FormView):
    template_name = 'website/code.html'
    form_class = CodeForm
    success_url = reverse_lazy('website:home_page')

    def form_valid(self, form):
        self.request.session['access'] = form.data['code']
        return super().form_valid(form)
