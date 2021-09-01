from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from dsumapp.decorators import dsum_ownership_required
from dsumapp.forms import DsumCreationForm
from dsumapp.models import Dsum


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class DsumCreateView(CreateView):
    model = Dsum
    form_class = DsumCreationForm
    template_name = 'dsumapp/create.html'

    def form_valid(self, form):
        temp_dsum = form.save(commit=False)
        temp_dsum.writer = self.request.user
        temp_dsum.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dsumapp:detail', kwargs={'pk': self.object.pk})

class DsumDetailView(DetailView):
    model = Dsum
    context_object_name = 'target_post'
    template_name = 'dsumapp/detail.html'



    # def get_context_data(self, **kwargs):
    #     post = self.object
    #     user = self.request.user
    #
    #     #if user.is_authenticated: #로그인 했는가?
    #        #join = Join.objects.filter(user=user, project=project)
    #     #object_list = Post.object(project=self.get_object())
    #     return super(PostDetailView, self).get_context_data(object_list=object_list, **kwargs)
    #     #return super(PostDetailView, self).get_context_data(join=join, **kwargs)



@method_decorator(dsum_ownership_required, 'get')
@method_decorator(dsum_ownership_required, 'post')
class DsumUpdateView(UpdateView):
    model = Dsum
    context_object_name = 'target_post'
    form_class = DsumCreationForm
    template_name = 'dsumapp/update.html'

    def get_success_url(self):
        return reverse('dsumapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(dsum_ownership_required, 'get')
@method_decorator(dsum_ownership_required, 'post')
class DsumDeleteView(DeleteView):
    model = Dsum
    context_object_name = 'target_post'
    success_url = reverse_lazy('dsumapp:list')
    template_name = 'dsumapp/delete.html'

class DsumListView(ListView):
    model = Dsum
    context_object_name = 'post_list'
    template_name = 'dsumapp/list.html'
    paginate_by = 25

    ordering = ['-id']

