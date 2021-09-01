from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from boardapp.decorators import board_ownership_required, LoginRequired
from boardapp.forms import BoardCreationForm
from boardapp.models import Board
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class BoardCreateView(CreateView):
    model = Board
    form_class = BoardCreationForm
    template_name = 'boardapp/create.html'

    def form_valid(self, form):
        temp_board = form.save(commit=False)
        temp_board.writer = self.request.user
        temp_board.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})

# class BoardDetailView(LoginRequired, DetailView, FormMixin):
class BoardDetailView(DetailView, FormMixin):
    login_url = '/accounts/login/'
    model = Board
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'boardapp/detail.html'

    def get_context_data(self, **kwargs):
        comment_list = Comment.objects.filter(board=self.object.pk).order_by('-created_at')
        # if user.is_authenticated: #로그인 했는가?
        # join = Join.objects.filter(user=user, project=project)
        # object_list = Post.object(project=self.get_object())
        return super(BoardDetailView, self).get_context_data(comment_list=comment_list, **kwargs)


@method_decorator(board_ownership_required, 'get')
@method_decorator(board_ownership_required, 'post')
class BoardUpdateView(UpdateView):
    model = Board
    context_object_name = 'target_post'
    form_class = BoardCreationForm
    template_name = 'boardapp/update.html'

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(board_ownership_required, 'get')
@method_decorator(board_ownership_required, 'post')
class BoardDeleteView(DeleteView):
    model = Board
    context_object_name = 'target_post'
    success_url = reverse_lazy('boardapp:list')
    template_name = 'boardapp/delete.html'

# class BasicListView(LoginRequired, ListView):

class BasicListView(ListView):
    login_url = '/accounts/login/'
    model = Board
    context_object_name = 'post_list'
    ordering = ['-id']


class BoardListView(BasicListView):
    template_name = 'boardapp/list.html'

    def get_queryset(self):
        all_list = Board.objects.filter().order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(all_list, 4)
        queryset = paginator.get_page(page)

        return queryset


class NoticeListView(BasicListView):
    template_name = 'boardapp/notice.html'

    def get_queryset(self):
        notice_list = Board.objects.filter(type='notice').order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(notice_list, 4)
        queryset = paginator.get_page(page)

        return queryset


class ContestListView(BasicListView):
    template_name = 'boardapp/contest.html'

    def get_queryset(self):
        contest_list = Board.objects.filter(type='contest').order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(contest_list, 4)
        queryset = paginator.get_page(page)

        return queryset


class KquestionListView(BasicListView):
    template_name = 'boardapp/kquestion.html'

    def get_queryset(self):
        kquestion_list = Board.objects.filter(type='kquestion').order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(kquestion_list, 4)
        queryset = paginator.get_page(page)

        return queryset


class TutoringListView(BasicListView):
    template_name = 'boardapp/tutoring.html'

    def get_queryset(self):
        tutoring_list = Board.objects.filter(type='tutoring').order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(tutoring_list, 4)
        queryset = paginator.get_page(page)

        return queryset


class DsumListView(BasicListView):
    template_name = 'boardapp/dsum.html'

    def get_queryset(self):
        dsum_list = Board.objects.filter(type='dsum').order_by('-id')

        page = int(self.request.GET.get('page', 1))
        paginator = Paginator(dsum_list, 4)
        queryset = paginator.get_page(page)

        return queryset
