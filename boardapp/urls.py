from django.urls import path

from boardapp.views import BoardCreateView, BoardUpdateView, BoardDetailView, BoardDeleteView, BoardListView

app_name = "reviewapp"

urlpatterns = [
    path('create/', BoardCreateView.as_view(), name='create'),
    path('update/<int:pk>', BoardUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', BoardDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BoardDeleteView.as_view(), name='delete'),

    path('list/', BoardListView.as_view(), name='list'),
]