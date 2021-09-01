from django.urls import path

from boardapp.views import BoardCreateView, BoardUpdateView, BoardDetailView, BoardListView, BoardDeleteView, \
    NoticeListView, ContestListView, KquestionListView, DsumListView, TutoringListView

app_name = "boardapp"

urlpatterns = [
    path('create/', BoardCreateView.as_view(), name='create'),
    path('update/<int:pk>', BoardUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', BoardDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BoardDeleteView.as_view(), name='delete'),

    path('list/', BoardListView.as_view(), name='list'),
    path('list/notice/', NoticeListView.as_view(), name='notice'),
    path('list/contest/', ContestListView.as_view(), name='contest'),
    path('list/kquestion/', KquestionListView.as_view(), name='kquestion'),
    path('list/dsum/', DsumListView.as_view(), name='dsum'),
    path('list/tutoring/', TutoringListView.as_view(), name='tutoring'),
]