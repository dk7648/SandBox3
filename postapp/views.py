from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentCreationForm
from postapp.decorators import post_ownership_required
from postapp.forms import PostCreationForm
from postapp.models import Post


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'postapp/create.html'

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.pk})

class PostDetailView(DetailView, FormMixin):
    model = Post
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'postapp/detail.html'

    # def get_context_data(self, **kwargs):
    #     post = self.object
    #     user = self.request.user
    #
    #     #if user.is_authenticated: #로그인 했는가?
    #        #join = Join.objects.filter(user=user, project=project)
    #     #object_list = Post.object(project=self.get_object())
    #     return super(PostDetailView, self).get_context_data(object_list=object_list, **kwargs)
    #     #return super(PostDetailView, self).get_context_data(join=join, **kwargs)



@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'target_post'
    form_class = PostCreationForm
    template_name = 'postapp/update.html'

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'target_post'
    success_url = reverse_lazy('postapp:list')
    template_name = 'postapp/delete.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'postapp/list.html'
    paginate_by = 25


#DetailView

# class DSumDetailView(DetailView):
#     model = DSum
#     context_object_name = 'target_dsum'
#     template_name = 'postapp/D-sum.html'
#
# class KQuestionDetailView(DetailView):
#     model = KQuestion
#     context_object_name = 'target_kquestion'
#     template_name = 'postapp/KQuestion.html'
#
# class ContestDetailView(DetailView):
#     model = Contest
#     context_object_name = 'target_contest'
#     template_name = 'postapp/contest.html'
#
# class MajorDetailView(DetailView):
#     model = Major
#     context_object_name = 'target_major'
#     template_name = 'postapp/major-tutoring.html'

#ListView
