from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from boardapp.models import Board

has_ownership = [account_ownership_required, login_required]

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView


def index(request):
    return render(request, 'accountapp/index.html')

class AccountIndexView(ListView):
    model = Board
    context_object_name = 'post_list'
    template_name = 'accountapp/index.html'

    def get_context_data(self):
        max = 9
        notice_list = Board.objects.filter(type='notice').order_by('-id')[:max]
        dsum_list = Board.objects.filter(type='dsum').order_by('-id')[:max]
        kquestion_list = Board.objects.filter(type='kquestion').order_by('-id')[:max]
        contest_list = Board.objects.filter(type='contest').order_by('-id')[:max]
        tutoring_list = Board.objects.filter(type='tutoring').order_by('-id')[:max]

        return super().get_context_data(notice_list=notice_list, dsum_list=dsum_list, kquestion_list=kquestion_list, contest_list=contest_list, tutoring_list=tutoring_list)

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

