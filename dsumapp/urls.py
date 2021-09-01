from django.urls import path

from dsumapp.views import DsumCreateView, DsumUpdateView, DsumDetailView, DsumListView, DsumDeleteView

app_name = "dsumapp"

urlpatterns = [
    path('create/', DsumCreateView.as_view(), name='create'),
    path('update/<int:pk>', DsumUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', DsumDetailView.as_view(), name='detail'),
    path('list/', DsumListView.as_view(), name='list'),
    path('delete/<int:pk>', DsumDeleteView.as_view(), name='delete'),
]