from django.urls import path

from postapp.views import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, PostListView

app_name = "postapp"

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('list/', PostListView.as_view(), name='list'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]