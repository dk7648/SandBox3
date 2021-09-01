from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from boardapp.models import Board
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.board = Board.objects.get(pk=self.request.POST['board_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        board = get_object_or_404(Board, pk=self.request.POST['board_pk'])
        return reverse('boardapp:detail', kwargs={'pk': board.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    #success_url = reverse_lazy('commentapp:list')
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('home')
